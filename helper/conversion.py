'''
TODO

Given either a string or a list of strings as input, return
a number (int or float) which is equal to the monetary value

money_conversion("$12.2 million") --> 12200000 ## word syntax
money_conversion("$790,000") --> 790000 # vakue syntax

use test_money_conversion.py to test your solution
'''
import re

amounts = r"thousand|million|billion"

number =r"\d+(,\d{3})*\.*\d*" 

value_re = rf"\${number}"
word_re = rf"\${number}(-|\sto\s)?({number})?\s({amounts})"


# this functions returns the word value 
def word_to_value(word):
	value_dict = {"thousand": 1000, "million": 1000000, "billion": 1000000000}
	return value_dict[word]

# this function converts the string_numerical with word (eg: $1 million into 1000000 ) to actual value 
def parse_word_syntax(string):
	value_string = re.search(number, string).group()
	value = float(value_string.replace(',',''))
	word = re.search(amounts, string, flags=re.I).group().lower() #re.I ignores casing lower/upper
	word_value = word_to_value(word)
	return value*word_value

# this converts the numerical string into actual value
def parse_value_syntax(string):
	value_string = re.search(number, string).group()
	# striping out the comma before solution
	value = float(value_string.replace(',',''))
	return value

# it is the main function that controls the overall procedures
# take both value and words and gets  acutal integer value
def money_conversion(money):

	# if the money value is list
	if isinstance(money,list):
		money = money[0]


	# if money contains words like million|billion|thousand
	word_syntax = re.search(word_re, money, flags=re.I) 
	
	# if there is only value followed by $
	value_syntax = re.search(value_re, money)

	if word_syntax:
		return parse_word_syntax(word_syntax.group())

	elif value_syntax:
		return parse_value_syntax(value_syntax.group())


print(money_conversion("$790 Million"))