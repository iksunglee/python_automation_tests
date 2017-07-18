import pyautogui

pyautogui.PAUSE =1
pyautogui.FAILSAFE = True


#my system size is: 1336,768

#width, height = pyautogui.size()

# target position 702, 753

print('press Ctrl-C to quit')
try:
	while True:
		x, y = pyautogui.position()
		#rjust() method will right-justify them so that they take up the same amount of space
		positionStr = 'X: '+ str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
		""" positionstr will be printed
			end='' prevents default newline character to be added to the end of the printed line
			only for the most recent line of text once print a newline character you can't erase printed before it
			to erase text, \b space char. is used
			flush=True, to print calls that print \b backspaces characters // might not update the next characters
			

		"""
		print(positionStr, end='')
		print('\b' * len(positionStr), end='', flush = True)
except KeyboardInterrupt:
	print('\n Done.')		