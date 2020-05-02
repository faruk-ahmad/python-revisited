"""
Reading from file & writing to file
"""

file_path = './sample_input.txt'

# reading the whole content of file at a time
with open(file_path, 'r') as rf:
    data = rf.read()

print(data)


