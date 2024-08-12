"""
There are 6 file access modes
1. Read only - r
2. Read and write - r+
3. Write only - w
4. Write and Read - w+
5. Append only - a
6. Append and read - a+
"""

filename="test.txt"
myList = ["Hello\n", "Python!\n", "I'm\n", "Learning\n", "You!\n"]



file1=open(filename, 'w')
file1.writelines(myList)
file1.close()

file2=open(filename, "r")
#print(file2.read())
print(file2.readlines())

"""
Methods to read and write files in Python
For reading lines: read(), readline(), readlines()
For writing lines: write(), writelines()
"""

"""
Scenario: 1
Read content from file a and write it to file b.
"""

output_filename="output.txt"

with open(filename, 'r') as file_input:
  with open(output_filename, 'w') as file_output:
    for line in file_input:
      file_output.write(line)
