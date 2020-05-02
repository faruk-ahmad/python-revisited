"""
Writing to a file
"""

file_path = './sample_output.txt'

data = "Happy Birthday to you\n And how are you doing today?"

with open(file_path, 'w') as wf:
    wf.write(data)