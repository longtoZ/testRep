from pynput.keyboard import Controller
import time

keyboard = Controller()

string ="""And words were not just the pieces of speaking; they were the pieces of thinking. When you wrote them down, you could grasp your thoughts like bricks in your hands and push them into different arrangements.
"""
time.sleep(1)

for i in string:
	keyboard.type(i)
	keyboard.release(i)
	time.sleep(0.08)



