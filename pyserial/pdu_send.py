# coding=utf-8
from time import sleep


def unicode_hex(s):
    return ''.join(["%02X" % ord(c) if ord(c) > 127 else "%04X" % ord(c) for c in s])


def hex_len(s):
    return (len(s) // 2)


def message_convert(m, l):
    return ("%02X" % l) + m


def phone_convert(p):
    p = '86' + p + 'F'
    p_odd = p[::2]
    p_even = p[1::2]
    p_convert = [i + j for i, j in zip(p_even, p_odd)]
    return ''.join(p_convert)


def cmgs_code(l):
    print(l)
    return "%03d" % (15 + l)


def cmgs_body(p, m):
    fixed1 = '0011000D91'
    fixed2 = '000801'
    return fixed1 + p + fixed2 + m


def cmgs(phone, message):
    p_con = phone_convert(phone)
    m_hex = unicode_hex(message)
    print(m_hex)
    m_len = hex_len(m_hex)
    m_con = message_convert(m_hex, m_len)
    return cmgs_code(m_len), cmgs_body(p_con, m_con)


import serial

message = u'ttt'
phone = '136xxxxxxxx'
code, body = cmgs(phone, message)
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.write("at\r")
ser.write("at+cmgf=0\r")
ser.write("at+csq\r")
sleep(2)
t = ser.readall()
print(t)


ser.write("at+cmgs=" + code + "\r")
print('>>smgs set>> ', t)
ser.write(body + '\x1a')
sleep(2)
t = ser.readall()
print(filter(lambda x: x is not '', t.split('\r\n')))


phone2 = '155xxxxxxxx'
code, body = cmgs(phone2, message)
ser.write("at+cmgs=" + code + "\r")
print('>>smgs set>> ', t)
ser.write(body + '\x1a')
sleep(2)
t = ser.readall()
print(filter(lambda x: x is not '', t.split('\r\n')))
ser.close()
