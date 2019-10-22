import random
import os 
import sys
import time
EwordList = [
"lion","cat","mouse","bat"
         ]
guess_word = []
cguess = random.choice(EwordList)#The computer picks the random options
lengthw = len(cguess)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letterS = []
