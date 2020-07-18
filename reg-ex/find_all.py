import re


"""
Purpose: findall method of re

Link: https://www.w3schools.com/python/python_regex.asp
Date: 17/06/2020
"""


txt = 'Hello bro, Hello sis'

matches = re.findall('Hello', txt)

for match in matches:
	print(match)