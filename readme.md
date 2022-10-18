# Move Mouse
This is a simple project that will move your cursor to keep you in active state on your computer

## Running
Run the executable file by double clicking on the moveMouse.exe file

## Installation
Run the following to install the dependencies 
```bash
pip3 install -r requirements.txt 
```

## Customizing the cursor movement behaviour
1. Modify the variables value in moveMouse.py 
```python
    val_y = 10 # coordinates movement for y-axis
    sleep = 30 # time to proceed with next movement in seconds
```
2. Generate the executable file with the following command
```bash
pyinstaller --onefile moveMouse.py --hidden-import=pyautogui
```