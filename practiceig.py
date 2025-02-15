"""Challenge: Word Frequency Counter
Write a Python program that takes a sentence as input and counts how many times each word appears in the sentence. 
The program should:
Ignore punctuation and case (i.e., treat "Hello" and "hello" as the same word).
Print the count for each word in the sentence.
Return the word(s) that appear the most (i.e., the most frequent word(s))."""

import string #imports string 

sentence = input("Enter a sentence.") #lets the user type a sentence 
sentence = sentence.lower() #turns all the letters into lowercase so theres no interruptions with the code
#it means that "HIIII" is the same as "hiiii"
sentence = sentence.translate(str.maketrans('', '', string.punctuation))
#removes all the punctuation 
#sentence.translate modifies a string based on a translation table (needs the next part) 
#str.maketrans sets up a translation table 
#(x,y,z), x is what ur replacing, y is what ur replacing x with, z is what u wanna delete
#in this case, we're replacing nthn with nthn and we're deleting all the punctuation
#this means that "hi!" is the same as "hi" 


words = sentence.split() #splits the sentence into individual words 
#the words all function as their own things

wordcounts = {} #sets up a dictionary so the wordcounts can be put in it later
#keeps track of how many times a word appears





for word in words: #for every word in "words" (the sentence after splitting), the following happens:
    if word in wordcounts: #if the word is already in the dictionary
        wordcounts[word] += 1 #then we gyatta increase its count 
    else:   #if its not already in the dictionary
        wordcounts[word] = 1 #then we gyatta add it ;-;
        #everytime we encounter a word for the 1st time, u gyatta add it with 1 
        #1 is like the default count

maxcount = max(wordcounts.values()) #finds the highest out of the values in the dictionary
mostfrequentwords = [word for word, count in wordcounts.items() if count == maxcount]
#creates a list comprehension, here its used to build a list of the most frequent words in the dictionary
#.items() says again the key values in the dictionary
#count in wordcounts.items() extracts each key-value pair
#if count == maxcount  filters the words based on the highest count
#word for... creates a new list 

print("Word counts:") #prints "word counts:"
for word, count in wordcounts.items(): #for every word count in the key-value pair 
    print(f"{word}: {count}")        #print the pair