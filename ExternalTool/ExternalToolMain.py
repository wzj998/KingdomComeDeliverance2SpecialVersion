import keyboard
import time

caps_lock_state = False

def on_esc_press():
    # 当检测到 Esc 键按下时，延迟 0.2 秒
    time.sleep(0.2)
    # 然后模拟按下 F3 键
    keyboard.press_and_release('f3')
    print("按下 f3")

def on_caps_lock_press_event(e):
    global caps_lock_state
    if not caps_lock_state:
        # 首次按下时，模拟按住 w 和 shift
        keyboard.press('w')
        keyboard.press('shift')
        caps_lock_state = True
        print("按住 w+shift")
    else:
        # 再次按下时，释放 w 和 shift
        keyboard.release('w')
        keyboard.release('shift')
        caps_lock_state = False
        print("释放 w+shift")

keyboard.on_press_key('caps lock', on_caps_lock_press_event)
keyboard.on_press_key('esc', lambda _: on_esc_press())

# 确保程序持续运行以监听按键
keyboard.wait()