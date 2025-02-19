import keyboard
import time

def on_esc_press():
    # 当检测到 Esc 键按下时，延迟 0.2 秒
    time.sleep(0.2)
    # 然后模拟按下 F3 键
    keyboard.press_and_release('f3')

# 监听 Esc 键按下事件
keyboard.on_press_key('esc', lambda _: on_esc_press())

# 确保程序持续运行以监听按键
keyboard.wait()
