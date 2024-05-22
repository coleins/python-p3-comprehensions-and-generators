#!/usr/bin/env python3

#n for n in num_list: Iterates over each element n in the input list num_list
#if n % 2 == 0: Includes the element n in the new list only if it satisfies the condition n % 2 == 0, which means n is even.

def return_evens(num_list):
    return [n for n in num_list if n%2 == 0]
    
#uses a list comprehension to create a new list where each sentence from the input list sentence_list has an exclamation mark appended to it. 
def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]