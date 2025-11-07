import os
os.environ['DISPLAY'] = ':0'
os.environ['XAUTHORITY']='/home/nans/.Xauthority'

import pyautogui
import serial

# Constants
MOUSE_DELAY = 0.2
STEP = 70
# Enter your screen resolution here
HORIZONTAL_SCREEN_SIZE = 1920
VERTICAL_SCREEN_SIZE   = 1080


def main():
    # Serial port configuration
    ser = serial.Serial('/dev/ttyUSB0', 9600, writeTimeout=1)

    # Center mouse at start
    x = HORIZONTAL_SCREEN_SIZE / 2
    y = VERTICAL_SCREEN_SIZE / 2
    pyautogui.moveTo(x, y, MOUSE_DELAY)

    while True:
        try :
            # Read command from serial
            msg = ser.readline().strip()
            msg = msg.decode('utf-8')
            
            # Execute command
            match msg:
                case "FUP":
                    pyautogui.press('up')
                case "FDOWN":
                    pyautogui.press('down')
                case "FLEFT":
                    pyautogui.press('left')
                case "FRIGHT":
                    pyautogui.press('right')
                case "OK":
                    pyautogui.click()
                case "RETURN":
                    pyautogui.hotkey('alt','left')
                case "DISPLAY":
                    pyautogui.press('f')
                case "TITLE":
                    x = HORIZONTAL_SCREEN_SIZE / 2
                    y = VERTICAL_SCREEN_SIZE / 2
                    pyautogui.moveTo(x, y, MOUSE_DELAY)
                case "UP":
                    y = y - STEP
                    pyautogui.moveTo(x, y, MOUSE_DELAY)
                case "DOWN":
                    y = y + STEP
                    pyautogui.moveTo(x, y, MOUSE_DELAY)
                case "LEFT":
                    x = x - STEP
                    pyautogui.moveTo(x, y, MOUSE_DELAY)
                case "RIGHT":
                    x = x + STEP
                    pyautogui.moveTo(x, y, MOUSE_DELAY)
                case "MUP":
                    pyautogui.scroll(10)
                case "MDOWN":
                    pyautogui.scroll(-10)
                case "STOP":
                    pyautogui.hotkey('alt','f4')
                case "SKIP":
                    pyautogui.press('s')
                case "ENTER":
                    pyautogui.press('enter')
                case "PLAY" | "PAUSE":
                    pyautogui.press('space')
                case "MENU":
                    pyautogui.hotkey('alt','tab')
                case "POWER":
                    os.system('shutdown now')
                case _:
                    print(f"Unknown command: {msg}")

        except serial.serialutil.SerialException:
            pass

if __name__ == "__main__":
    main()
