import pyautogui
import time

def startLoop():
    up = 0
    while True:
        # move cursor up and down
        if up == 0:
            pyautogui.moveRel(0,10)
            up = 1
        else:
            pyautogui.moveRel(0,-10)
            up = 0
        time.sleep(30) # sleep time in seconds
        

if __name__ == '__main__':
    print("Moving mouse")
    print("Press ctrl + c to quit")
    startLoop()