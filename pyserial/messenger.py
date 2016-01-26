# coding=utf-8
import re
from functools import wraps
from time import sleep
import serial


class CNPDUFormatter(object):
    @staticmethod
    def _unicode_hex(s):
        return ''.join(["%02X" % ord(c) if ord(c) > 127 else "%04X" % ord(c) for c in s])

    @staticmethod
    def _hex_len(s):
        return (len(s) // 2)

    @staticmethod
    def format_message(hex_message, hex_length):
        return ("%02X" % hex_length) + hex_message

    @staticmethod
    def format_number(number):
        number = '86' + number + 'F'
        number_odd = number[::2]
        number_even = number[1::2]
        number_formatted = [i + j for i, j in zip(number_even, number_odd)]
        # OD is the length without F
        # 91 is Type-of-Address. (91 indicates  international format of the phone number)
        number_formatted.insert(0, '91')
        number_formatted.insert(0, '0D')
        return ''.join(number_formatted)

    @staticmethod
    def _cmgs_code(message_length):
        fixed = 15
        return "%03d" % (fixed + message_length)

    @staticmethod
    def _cmgs_body(formatted_number, formatted_message):
        # for details see, http://www.gsm-modem.de/sms-pdu-mode.html
        return ''.join(['00',  # ignore length
                        '11',  # SMS_SUBMIT
                        '00',  # MESSAGE_REFERENCE
                        formatted_number,  #
                        '00',  # Protocol identifier
                        '08',  # Data coding scheme, 08 is UCS2	Default,
                        # see https://en.wikipedia.org/wiki/Data_Coding_Scheme
                        '01',  # Validity-Period.
                        # "AA" means 4 days, "01" is some time I don't know , however these bits are optional
                        formatted_message
                        ])

    @staticmethod
    def cmgs(number, message):
        formatted_number = CNPDUFormatter.format_number(number)
        hex_message = CNPDUFormatter._unicode_hex(message)
        hex_length = CNPDUFormatter._hex_len(hex_message)
        formatted_message = CNPDUFormatter.format_message(hex_message, hex_length)
        return CNPDUFormatter._cmgs_code(hex_length), CNPDUFormatter._cmgs_body(formatted_number, formatted_message)


def _connect(func):
    @wraps(func)
    def wrapper(self, *args):
        try:
            ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        except Exception as e:
            print('error happened')
            print(e)
        else:
            redirected_func = getattr(self, '_' + func.__name__)
            ret = redirected_func(ser, *args)
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            ser.close()
            return ret

    return wrapper


class Messenger(object):
    def __init__(self, tty='/dev/ttyUSB0', baud=9600, timeout=10):
        self._tty, self._baud, self._timeout = tty, baud, timeout

    def _response(self, ser):
        try:
            response = ser.readall()  # filter(lambda x: x is not '', ser.readall().split('\r\n'))
            print('response',response)
        except serial.SerialException as e:
            return [str(e), 'ERROR']
        except OSError as e:
            return [str(e), 'ERROR']
        return response

    ############################
    @_connect
    def at(self, *args):
        pass

    def _at(self, ser, *args):
        ser.write('at\r')
        return self._response(ser)

    ############################
    @_connect
    def csq(self, *args):
        pass

    def _csq(self, ser, *args):
        ser.write('at+csq\r')
        return self._response(ser)

    ############################
    @_connect
    def healthy(self, *args):
        pass

    def _is_healthy(self, response):
        response = response.replace('\r','_r_')
        response = response.replace('\n','_n_')
        print('healthy',response)
        result = re.search('(?P<status>\d{1,2})\,\d{1,2}', response)
        if not result:
            print(False)
            return False
        status = result.group('status')
        good = 16 <= int(status) <= 31
        print(status)
        if good:
            print(True)
        else:
            print(False)
        return good

    def _healthy(self, ser, *args):
        response = self._csq(ser)
        return self._is_healthy(response)

    ############################
    @_connect
    def send(self, *args):
        pass

    def _send(self, ser, number, message):
        code, body = CNPDUFormatter.cmgs(number, message)
        # count = 0
        # while not self._healthy(ser) and count < 10:
        #     count = count + 1
        #     print('waiting....' + str(count))
        # if count == 10:
        #     print('not healthy')
        #     return
        sleep(2)
        ser.write("AT+CMGF=0\r")
        response = self._response(ser)
        ser.write("AT+CMGS=" + code + "\r")
        response = self._response(ser)
        ser.write(body + '\x1a')
        response = self._response(ser)
        return response


if __name__ == '__main__':
    r = Messenger().send('133xxxxxx', u'网站被黑系统测试，http://www.bing.com,发现abc')
    print(r)
