"""
Reading from file & writing to file
"""

file_path = './sample_input.txt'

# reading the whole content of file at a time
print('Reading whole content at a time:')
with open(file_path, 'r') as rf:
    data = rf.read()

print(data)

# reading line by line
print('\n\nReading line by line:')
with open(file_path, 'r') as rf:
    for line in rf:
        print(line) 


