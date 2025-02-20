import keyboard
import time

b_auto_run = False

def set_b_auto_run(value_new):
    if value_new:
        keyboard.press('w')
        keyboard.press('shift')
        print("按住 w+shift")
    else:
        keyboard.release('w')
        keyboard.release('shift')
        print("释放 w+shift")
        
    global b_auto_run
    b_auto_run = value_new

def on_esc_press():
    # 当检测到 Esc 键按下时，延迟 0.2 秒
    time.sleep(0.2)
    # 然后模拟按下 F3 键
    keyboard.press_and_release('f3')
    print("按下 f3")

def on_caps_lock_press_event(e):
    global b_auto_run
    set_b_auto_run(not b_auto_run)

def on_m_press():
    global b_auto_run
    if b_auto_run:
        set_b_auto_run(False)

        time.sleep(0.1)

        keyboard.press_and_release('m')
        print("按下 m")

keyboard.on_press_key('caps lock', on_caps_lock_press_event)
keyboard.on_press_key('esc', lambda _: on_esc_press())
keyboard.on_press_key('m', lambda _: on_m_press())

# 确保程序持续运行以监听按键
keyboard.wait()