#!/usr/bin/env python3

def return_evens(num_list):
  return [num for num in num_list if num % 2 ==0]
  
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(return_evens(numbers))

def make_exclamation(sentence_list):
  return [words + "!" for words in sentence_list]
sentence_list = [
            "I like computers",
            "I require coffee",
            "Live long and prosper",
        ]
print(make_exclamation(sentence_list))