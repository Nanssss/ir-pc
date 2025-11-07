import os
import platform
import pyautogui
import serial

# Constants
MOUSE_DELAY = 0.2
STEP = 70
BAUDRATE = 9600


def get_serial_port():
    serial_port = ''

    if platform.system() == "Linux":
        # Linux
        home_dir = os.path.expanduser("~")
        os.environ['DISPLAY'] = ':0'
        os.environ['XAUTHORITY'] = os.path.join(home_dir, '.Xauthority')

        serial_port = '/dev/ttyUSB0'  # <-- Change this to your actual serial port, see README
    else:
        # Windows
        serial_port = 'COM3'  # <-- Change this to your actual COM port, see README
    
    return serial_port


def move_mouse(x, y):
    pyautogui.moveTo(x, y, MOUSE_DELAY)


def main():
    SERIAL_PORT = get_serial_port()
    screen_width, screen_height = pyautogui.size()
    # Center mouse at start
    x = screen_width/ 2
    y = screen_height / 2
    move_mouse(x, y)

    try:
        with serial.Serial(SERIAL_PORT, BAUDRATE, writeTimeout=1) as ser:
            while True:
                try :
                    # Read command from serial
                    msg = ser.readline().decode('utf-8').strip()
                    if not msg:
                        continue

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
                            x = screen_width / 2
                            y = screen_height / 2
                            move_mouse(x, y)
                        case "UP":
                            y = y - STEP
                            move_mouse(x, y)
                        case "DOWN":
                            y = y + STEP
                            move_mouse(x, y)
                        case "LEFT":
                            x = x - STEP
                            move_mouse(x, y)
                        case "RIGHT":
                            x = x + STEP
                            move_mouse(x, y)
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
                            print("Shutting down...")
                            os.system('shutdown now')
                        case _:
                            print(f"Unknown command: {msg}")

                except serial.serialutil.SerialException:
                    print("Serial exception occurred. Retrying...")

    except serial.SerialException as e:
        print(f"Cannot open serial port: {e}")

if __name__ == "__main__":
    main()
