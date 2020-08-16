import pyautogui
import time
import pyperclip

# Giving time for the user to open a new chrome tab
time.sleep(3)
path = r"D:\Coding files\PYTHON\Chrome Automation\links.txt"

f = open(path,"r+")

links = [i.strip() for i in f.readlines()]

f.close()

for i in links:
	pyautogui.click(319, 74)

	# Enter the links in the chrome browser tab
	pyperclip.copy(i)
	# Paste the copied link and access the site
	pyautogui.hotkey("ctrl", "v")
	pyautogui.hotkey("enter")

	# Open the next tab
	pyautogui.hotkey("ctrl", "t")
	
print(f"\nRestored {len(links)} links")
print("Successfully opened all the links!!!")