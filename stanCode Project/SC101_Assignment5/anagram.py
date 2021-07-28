"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variable
python_list = []              # (lst) to contain all the words in the FILE


def main():
    """
    TODO:
    """
    print(f'Welcome to stanCode \"Anagram Generator\" (or {EXIT} to quit) ')
    read_dictionary()
    while True:
        word = input('Find anagrams for: ')                 # input the word for finding its anagrams
        start = time.time()
        if word == EXIT:
            break
        else:
            print('Searching...')
            all_ana = find_anagrams(word)                   # (list) contain all the anagrams of the word input
            count = len(all_ana)                            # the number of the anagrams the word input has
            print(str(count) + ' anagrams: ', end='')
            print(all_ana)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    global python_list
    with open(FILE, 'r') as f:
        for line in f:
            python_list.append(line.strip())                # to store all the word in the FILE in the python_list


def find_anagrams(s):
    """
    :param s: (str) the word input to find the anagrams
    :return: (lst) all the anagrams s(word input) has
    """
    s_split = []                                            # (lst) to store every alphabet in s
    order = []                                              # (lst) to give every alphabet in s an order
    for i in range(len(s)):
        s_split.append(s[i])
        order.append(i)
    all_anagrams = find_anagrams_helper(s_split, '', [], order, [])
    return all_anagrams


def find_anagrams_helper(s_split, anagram, lst_of_anagrams, order, lst_of_order):
    if len(anagram) == len(s_split):                        # base case
        if anagram not in lst_of_anagrams and anagram in python_list:
            lst_of_anagrams.append(anagram)
            print('Found: ' + anagram)
            print('Searching...')

    else:
        for i in range(len(order)):
            if order[i] not in lst_of_order:
                # choose
                lst_of_order.append(order[i])
                anagram += s_split[i]
                # explore
                if has_prefix(anagram):
                    find_anagrams_helper(s_split, anagram, lst_of_anagrams, order, lst_of_order)
                # un-choose
                lst_of_order.pop()
                anagram = anagram[:len(anagram)-1]

    return lst_of_anagrams


def has_prefix(sub_s):
    """
    :param sub_s: the word to see if it has the same prefix with the element in the python list
    :return: (Boolean) if the element in the python list has the same prefix with the sun_s
    """
    for word in python_list:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
