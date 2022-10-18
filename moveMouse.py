import pyautogui
import time

def startLoop():
    val_y = 10 # coordinates movement for y-axis
    sleep = 30 # time to proceed with next movement in seconds
    up = 0
    while True:
        # move cursor up and down relative to its current position
        if up == 0:
            pyautogui.moveRel(0,val_y)
            up = 1
        else:
            pyautogui.moveRel(0,-val_y)
            up = 0
        time.sleep(sleep) # sleep time in seconds

if __name__ == '__main__':
    print("Moving mouse")
    print("Press ctrl + c to quit")
    startLoop()