# coding=utf-8
import datetime
import socket
import time
import traceback
import sys

def get_client(host='127.0.0.1', textport=51500, timeout=15):
    # 如果超时一般都是交易端有故障，抛出异常，邮件提示
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        port = int(textport)
    except ValueError:
        port = socket.getservbyname(textport, 'udp')
    s.connect((host, port))
    s.settimeout(timeout)
    return s


class client:
    def __init__(self, host):
        self.client = get_client(host=host)

    def exec_order(self, order):
        self.client.sendall(order)
        buf = self.client.recv(2048)
        if not len(buf):
            return "No data"
        return str(buf)

c = client(host="127.0.0.1")
while 1:
    try:
        print "Enter data to transmit: stop, get_position, buy, sell"
        data = sys.stdin.readline().strip()
        # time.sleep(5)
        # data = "get_position 0001"
        # data = "buy 000001 10.0 2000000"
        print data
        print datetime.datetime.now().strftime("%H:%M:%S")
        c.exec_order(data)
        print datetime.datetime.now().strftime("%H:%M:%S")

        # time.sleep(5)
        # data = "sell 300072 10.0 200000"
        # print data
        # print datetime.datetime.now().strftime("%H:%M:%S")
        # c.exec_order(data)
        # print datetime.datetime.now().strftime("%H:%M:%S")
        #
        # time.sleep(5)
        # data = "sell 000001 10.0 200000"
        # print data
        # print datetime.datetime.now().strftime("%H:%M:%S")
        # c.exec_order(data)
        # print datetime.datetime.now().strftime("%H:%M:%S")
    except :
        traceback.print_exc()