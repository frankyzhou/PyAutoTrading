import pyautogui

# PyAutoGUI can simulate moving the mouse, clicking the mouse, dragging 
# with the mouse, pressing keys, pressing and holding keys, and pressing keyboard hotkey combinations.

# For example, here is the complete code to move the mouse to the middle of the screen on Windows, OS X, and Linux:
# screenWidth, screenHeight = pyautogui.size()
# pyautogui.moveTo(screenWidth / 3, screenHeight / 3)
#
# screenWidth, screenHeight = pyautogui.size()
# currentMouseX, currentMouseY = pyautogui.position()
# pyautogui.moveTo(50, 150)
# pyautogui.click()
# pyautogui.moveRel(None, 10)  # move mouse 10 pixels down
# pyautogui.doubleClick()
# pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.tweens.easeInOutQuad)  # use tweening/easing function to move mouse over 2 seconds.
# pyautogui.typewrite('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
# pyautogui.press('esc')
# pyautogui.keyDown('shift')
# pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])
# pyautogui.keyUp('shift')
# pyautogui.hotkey('ctrl', 'c')


# screenWidth, screenHeight = pyautogui.size()
# pyautogui.moveTo(screenWidth * 0.2, screenHeight * 0.6)
# pyautogui.click()
# pyautogui.hotkey('ctrl', 'c')
# pyautogui.moveTo(screenWidth * 0.5, screenHeight * 0.5)
# pyautogui.click()
# pyautogui.hotkey('ctrl', 'a')
# pyautogui.hotkey('ctrl', 'v')
# pyautogui.hotkey('ctrl', 's')
file = open("C:\\Users\\frankyzhou\\Documents\\Tencent Files\\752649673\FileRecv\\new 2.txt")
for line in file:
    print line
