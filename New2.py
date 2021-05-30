'''
from pynput import keyboard
import time

break_program = False
def on_press(key):
    print(key)
    global break_program
    if key == keyboard.Key.end:
        print('end pressed')
        break_program = True
        return False       

with keyboard.Listener(on_press=on_press) as listener:
    while break_program == False:
        print('program running')
        time.sleep(2)
    listener.join()
'''



# from pynput.keyboard import Key, Controller

# keyboard = Controller()

# keyboard.press('a')
# #keyboard.release('a')
# with keyboard.pressed(Key.caps_lock):
#     keyboard.type('hello')



# from pynput import keyboard
# import sys


# def on_press(key):
# 	if str(key) == 'Key.end':
# 		sys.exit()

# def on_activate_h():
#     print('<ctrl>+<alt>+h pressed')

# def on_activate_i():
#     print('<ctrl>+<alt>+i pressed')

# with keyboard.GlobalHotKeys({
#         '<ctrl>+<alt>+h': on_activate_h,
#         '<ctrl>+<alt>+i': on_activate_i}) as h:
#     h.join()









