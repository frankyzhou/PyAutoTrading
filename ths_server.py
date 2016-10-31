from Tkinter import *
import tkMessageBox
from ttk import *
import datetime
import threading
import pickle
import time

import win32con
import tushare as ts
import socket
from winguiauto import (dumpWindows, clickButton, click, setEditText,
                        findSubWindows, closePopupWindow, clickWindow,
                        findTopWindow, getTableData, sendKeyEvent, restoreFocusWindow)
from pyautotrade_ths import *
COLLECTION = "yjb_operation"
GET_POSITION = "get_position"
BUY = "buy"
SELL = "sell"
STOP = "stop"
READ_SIZE = 8192
def get_server(host='', port=51500):
    # host = '' # Bind to all interfaces
    # port = 51500
    # Step1: 创建socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Step2: 设置socket选项(可选)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Step3: 绑定到某一个端口
    s.bind((host, port))
    return s

class ThsTrade:
    def __init__(self):
        self.server = get_server()
        # self.logger = get_logger(COLLECTION)

    def judge_opera(self, msg):
        msg = msg.split()
        type= msg[0]

        if type == STOP:
            return STOP

        code = msg[1]
        if type == GET_POSITION:
            print "查询仓位：" + code
            return self.get_position_by_stock(code)

        price, amount = msg[2], msg[3]
        if type == BUY:
            print "买入：" + code
            return self.yjb.buy(stock_code=code, price=price, amount=amount)
        elif type == SELL:
            print "卖出：" + code
            return self.yjb.sell(stock_code=code, price=price, amount=amount)

        return "Nothing."

    def get_position_by_stock(self, code):
        position_yjb = self.operation.getPosition()
        # while not isinstance(position_yjb, list):
        #     self.yjb.autologin()
        #     time.sleep(5)
        #     print "获取持仓失败，重连中"
        #     position_yjb = self.yjb.get_position()


    def main(self):
        top_hwnd = findTopWindow(wantedText=u'网上股票交易系统5.0')
        if top_hwnd == 0:
            tkMessageBox.showerror('错误', '请先打开华泰证券交易软件，再运行本软件')
        else:
            self.operation = Operation(top_hwnd)

        while 1:
            # try:
            request, address = self.server.recvfrom(READ_SIZE)
            print "Got data from ", address

            response = self.judge_opera(request)
            self.server.sendto(str(response), address)
            if str(response) == STOP: break
            # except Exception, e:
            #    print e


if __name__ == '__main__':
