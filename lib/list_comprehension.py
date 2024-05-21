#!/usr/bin/env python3

def return_evens(num_list):
    even_lc =[n for n in num_list if n % 2 == 0]
    print(even_lc)
    return even_lc
    
    return_evens([0, 1, 3, 5, 7, 8, 9])


def make_exclamation(sentence_list):
    exclamation=[ sentence + '!' for sentence in sentence_list]
    print(exclamation)
    return exclamation
    
make_exclamation(["Hello", "I'm doing great", "Python is fun"])  
    