import pyautogui
import time
import pyperclip

'''
Position of the link bar in chrome for my lap screen 
(665, 81)
'''

# Giving time for the user to open the chrome tab and place the cursor on the address bar

# time.sleep(5)
# print(pyautogui.position())


'''

When you are running the script for the first time
then comment the below part of the code completely to get the
position of the address bar of the chrome browser
on your screen, and uncomment the above 2 lines of code
and place the cursor on the chorme tab's address bar
to retrieve the x and y coordinates.

The index values of the cursor would be printed in the console
and use them in the code below for the click function

'''


# Specify the path for the text file containing the links
path = r"D:\Coding files\PYTHON\Chrome Automation\links.txt"

# Wait for some time to change to the chrome browser
time.sleep(5)
links = []

# This number defines the max number of duplicate tabs allowed to be saved
thresh = 5

# Keeps the count of the duplicate tabs found so far
count = 0
total = 0
while True:

	pyautogui.click(665, 81)
	# Select all the text in the link box in the chrome
	pyautogui.hotkey("ctrl", "a")

	# Copy the selected link
	pyautogui.hotkey("ctrl", "c")

	link = pyperclip.paste().strip()
	
	"""
	If there is an empty string in the
	clipboard the string pyperclip.paste()
	gets returned, so the condition is framed on top of that
	"""

	# If there is a new tab neglect it
	if link == "pyperclip.paste()":
		pass

	else:
		# Check if the link already exists in the existing links or not
		if link in links:
			count += 1
			if count == thresh:
				break

		else:
			total += 1
			links.append(link)		
			pyautogui.hotkey("ctrl", "tab")
			

f = open(path, "w+")

for i in links:
	f.write(str(i) + "\n")

f.close()

print(f"\nTotally {total} link(s) were saved")
print("Successfully saved the all links!!!")