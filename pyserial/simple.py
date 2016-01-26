#coding=utf-8
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.write("at+cmgf=1\r")
ser.write("at+cmgs=155xxxxxxxx\r")
t = ser.readall()
print('>>smgs set>> ',t)
ser.write('hello'+'\x1a')
t = ser.readall()
print(filter(lambda x: x is not '', t.split('\r\n')))
ser.close()

#
# from messaging import m
# import serial
#
# def send_text(number, text, path='/dev/ttyUSB0'):
#     # encode the SMS
#     p = messaging.PDU()
#     # notice how I get the first returned element, this does
#     # not deal with concatenated SMS.
#     pdu_length, pdu = p.encode_pdu(number, text)[0]
#     # open the modem port (assumes Linux)
#     ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
#     # write the PDU length and wait 1 second till the
#     # prompt appears (a more robust implementation
#     # would wait till the prompt appeared)
#     ser.write('AT+CMGS=%d\r' % pdu_length)
#     print(ser.readlines())
#     # write the PDU and send a Ctrl+z escape
#     ser.write('%s\x1a' % pdu)
#     ser.close()
#
# send_text('+86155xxxxxxxx', 'hey how are you?')

# from smspdu import SMS_SUBMIT
# pdu = SMS_SUBMIT.create('sender', 'recipient', 'hello, world')
# t=pdu.toPDU()
# print(t)

