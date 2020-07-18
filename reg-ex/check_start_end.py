"""
Purpose: Checks if a text starts and ends with specific pattern.

Link: https://www.w3schools.com/python/python_regex.asp
Date: 17/06/2020
"""
import re


txt_1 = 'The rain in Spain'
txt_2 = 'The rain in Hola Spain'
txt_3 = 'The rain in Spain Hola'

matched = re.search(r'^The.*Spain$', txt_3)

if matched:
	print("Match found.")
else:
	print("No match.")