"""
File: boggle.py
Name: Debby Chang
----------------------------------------
It's a boggle game for the player to enter 16 letters to create the game board. The player has to choose letters that
are all neighbors to each other and connected them(at least 4 letters) to become a word and see if it's a word
in the FILE.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# global variable
python_list = []


def main():
	"""
	Ask the users to enter 16 letters for the boggle game and find the answers of the game.
	The answer should be the word included in the FILE.
	"""
	start = time.time()

	# get all the words from FILE
	read_dictionary()

	# create game board
	board_list = []                # (lst) include all the 16 letters on boggle game board
	for i in range(4):		       # get every row of letters
		board_line = []            # (lst) include letters of line[i]
		while True:
			letters = input(str(i + 1) + ' row of letters: ').lower()
			letters = letters.split()
			if len(letters) == 4:
				for j in range(4):
					# check if letter[j] is one alphabet
					if len(letters[j]) == 1 and letters[j].isalpha():
						board_line.append(letters[j])
				board_list.append(board_line)

			# move to the next line to ask for letters input
			if len(board_line) == 4:
				break
			else:                  # if the letters are not 4 individual alphabet all separate by space
				print('Illegal input')

	# find the words(answer) for the boggle game
	ans = find_words(board_list)   # ans is a lst of all the answers of the boggle game returned from find_words func
	print('There are ' + str(len(ans)) + ' words in total.')

	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_words(board_list):
	"""
	:param board_list: the 16 letters of the boggle game
	:return: (lst) including all the answers of the boggle games
	"""
	ans = []                       # (lst) to get all the words from the helper function
	for x in range(4):             # like the x coordinate of the game board
		for y in range(4):         # like the y coordinate of the game board
			order_lst = [(x, y)]   # the lst to contain the x,y coordinate of each letter
			find_words_helper(x, y, board_list, board_list[x][y], order_lst, ans)
	return ans


def find_words_helper(x, y, board_list, word, order_lst, lst_of_words):
	"""
	:param x: the x coordinate of the alphabet
	:param y: the y coordinate of the alphabet
	:param board_list: (lst) including all the letters of the boggle game
	:param word: the word that have to find its neighbor
	:param order_lst: (lst) contain all the x,y coordinate of which has already find its neighbor
	:param lst_of_words: (lst) contain all the answers of the boggle game
	"""
	if len(word) >= 4:            # base case
		if word in python_list and word not in lst_of_words:
			print('Found ' + '"' + word + '"')
			lst_of_words.append(word)

	for i in range(-1, 2):         # for the letter to find the x coordinate of its neighbor
		for j in range(-1, 2):     # for the letter to find the y coordinate of its neighbor
			start_x = x + i        # the x coordinate of every letter that has to find its neighbor
			start_y = y + j		   # the y coordinate of every letter that has to find its neighbor
			if 0 <= start_x < 4 and 0 <= start_y < 4 and (start_x, start_y) not in order_lst:
				# choose
				word += board_list[start_x][start_y]
				order_lst.append((start_x, start_y))
				# explore
				if has_prefix(word):
					find_words_helper(start_x, start_y, board_list, word, order_lst, lst_of_words)
				# un-choose
				word = word[:-1]
				order_lst.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global python_list
	with open(FILE, 'r') as f:
		for line in f:
			python_list.append(line.strip())


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in python_list:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
