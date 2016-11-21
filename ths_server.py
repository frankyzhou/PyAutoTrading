# coding=utf-8
import socket
from pyautotrade_ths import *
import traceback

COLLECTION = "yjb_operation"
GET_POSITION = "get_position"
BUY = "buy"
SELL = "sell"
STOP = "stop"
READ_SIZE = 8192


def get_server(host='', port=51500):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    return s

class ThsTrade:
    def __init__(self):
        self.server = get_server()

    def judge_opera(self, msg):
        msg = msg.split()
        type= msg[0]

        if type == STOP:
            return STOP

        code = msg[1]

        self.operation.clickRefreshButton()

        if type == GET_POSITION:
            print u"查询仓位：" + code
            return self.get_position_by_stock(code)

        price, amount = msg[2], msg[3]
        if type == BUY:
            print u"买入：" + code
            return self.operation.order(code=code, price=price, direction="B", quantity=amount)
        elif type == SELL:
            print u"卖出：" + code
            return self.operation.order(code=code, price=price, direction="S", quantity=amount)

        return "Nothing."

    def get_position_by_stock(self, code):
        position_broker = self.operation.getPosition()
        rest_money = self.operation.getMoney()
        stock_money = 0.01
        if len(position_broker) > 0:
            for k in position_broker.keys():
                stock_money += position_broker[k]["turnover"]
        total_money = rest_money + stock_money
        enable = 0
        percent = 0.0
        if position_broker.has_key(code):
            enable = position_broker[code]["enable"]
            stock_turnover = position_broker[code]["turnover"]
            percent = stock_turnover / total_money
        return percent, enable, total_money

    def main(self):
        top_hwnd = findTopWindow(wantedText=u'网上股票交易系统5.0')
        if top_hwnd == 0:
            print u"无法找到客户端"
        else:
            self.operation = Operation(top_hwnd)
            print u"成功找到客户端"
        while 1:
            try:
                request, address = self.server.recvfrom(READ_SIZE)
                response = self.judge_opera(request)
                self.server.sendto(str(response), address)
                if str(response) == STOP:
                    print u"人工停止"
                    return False
            except:
                traceback.print_exc()
                print u"重新启动"
                return True

if __name__ == '__main__':
    result = True
    while result:
        ths = ThsTrade()
        result = ths.main()