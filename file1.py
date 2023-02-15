#! /usr/bin/python3

myfile = "file1.txt"

try:
    file = open(myfile, 'r')
except FileNotFoundError as e:
    print("No file")
    print(e)
    exit(1)

for line in file:
    print(line) 
