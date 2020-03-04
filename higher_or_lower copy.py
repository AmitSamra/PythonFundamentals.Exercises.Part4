# Exercise 4
'''
Create a copy of the program called higher_or_lower.py from exercise 2 in Part 3.

Extend the functionality to meet the following requirements:

If a user's guess is incorrect, they get to keep guessing until they get it right.
'''

from random import randrange

def rand_num():
	global num
	num = randrange(0,10)
	print(f'This is the random number: {num}\nPretend like you cannot see it.')
rand_num()

print(' ')

def user_guess():
	global guess
	guess = int(input('Guess a number in [0,10]: '))

def compare():
	while True:
		user_guess()
		if num < guess:
			print('Too high!')
		elif num > guess:
			print('Too low!')
		else:
			print('You win!')
			break
	print('You lose!')
compare()
