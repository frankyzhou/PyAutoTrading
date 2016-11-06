# coding=utf-8
from winguiauto import *

# top_hwnd = findTopWindow(wantedText=u'同花顺(v8.60.20) - A股技术分析')
# getStaticText(395666)
top_hwnd = findTopWindow(wantedText=u'组合 - 360极速浏览器')
time.sleep(2)
dumpWindows(1048626)
print 1
