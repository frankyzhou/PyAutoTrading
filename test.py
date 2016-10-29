# coding=utf-8
from winguiauto import (dumpWindows, dumpWindow, clickButton, click, setEditText,
                        findSubWindows, closePopupWindow, clickWindow,
                        findTopWindow, getTableData, sendKeyEvent, restoreFocusWindow)

# top_hwnd = findTopWindow(wantedText=u'同花顺(v8.60.20) - A股技术分析')
top_hwnd = findTopWindow(wantedText=u'网上股票交易系统5.0')
temp_hwnds = dumpWindows(top_hwnd)
control_hwnds = []
for window in temp_hwnds:
    childHwnd, windowText, windowClass = window
    if windowClass in ('Button', 'Edit'):
        print windowText.decode("gbk"), windowClass
        # if windowClass == "Button":
        #     print "click " + str(childHwnd) + windowText.decode("gbk")
        #     clickButton(childHwnd)

    # windowContent = dumpWindow(childHwnd)

    # if len(windowContent) > 0:
    #     print "-" * 20 + str(temp_hwnds.index(window))
    #     print len(windowContent)
    #     for hwnd, text_name, class_name in windowContent:
    #         print text_name.decode("gbk"), class_name
            # if class_name in ('Button', 'Edit'):
            #     print text_name.decode("gbk")
            #     control_hwnds.append((hwnd, text_name.decode("gbk"), class_name))

for c in control_hwnds:
    if c[2] == "Button":
        clickButton(c[0])
        print "click " + str(c[0]) + c[1]
