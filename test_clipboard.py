import win32clipboard
# win32clipboard.OpenClipboard()
try:
#     win32clipboard.GetOpenClipboardWindow()
    content = win32clipboard.GetClipboardData()
    print content
except Exception, e:
    print e


