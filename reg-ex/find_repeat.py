import re


txt = "Repeat untill i greater than 5\n\ts = s + a\n\tprint s"


matches = re.findall(r"repeat.|for.|while.|loop.", txt.lower())

for match in matches:
	print(match)