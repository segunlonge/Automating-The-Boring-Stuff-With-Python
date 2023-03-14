import pyautogui
pyautogui.size()

while True:
    pyautogui.moveRel(100,100,duration=0.25)
    print("moved")
    pyautogui.sleep(5)
    print("slept")
