1.Write a Python program to read an entire text file

What is python language?
Python is a widely used high-level,general-purpose,interpreted,dynamic programming language.Its design philosophy emphasizes code readability,and its syntax allows programs to express concepts in fewer lines of code than possib;le in languages such as C++ or Java.Python supports multiple programming paradigms,including object-oriented,imperative and functional programming or procedural styles.
It features a dynamic type system and automatic memory management and has a large and comprehensive standard library.The best way we learn anything is by practice and exercise questions.We have started this section for those (beginner to intermediate) who are familiar with python.

Code:
def file_read_tuba(fname):
    txt = open(fname)
    print(txt.read())
file_read_tuba('Python.txt')  

Output:
 

2.Write a python program to append text to the file and display the text
 
Big data primarily refers to data sets that are too large or complex to be dealt with by traditional data-processing application software. 
Data with many entries (rows) offer greater statistical power, while data with higher complexity (more attributes or columns) may lead to a higher false discovery rate.

Code:
def file_read_tuba(fname):
    with open(fname,"w") as myfile:
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises")
    txt = open(fname)
    print(txt.read())
file_read_tuba('abc.txt')

Outpuṭ:
3.Write a python program to read a file line by line and store it into the list.

Code:
First name: Tuba
Middle name: Jagdish
Last name: Shukla
Roll no.: 11
Class : MSC Big Data

def file_read_tuba(fname):
    with open(fname) as f:
        #Content_list is the list that contains the read lines.
        content_list = f.readlines()
        print(content_list)
file_read_tuba('test.txt') 

Output:
4.Write  a Program to read a file line by line tore it into a variable

Big data primarily refers to data sets that are too large or complex to be dealt with by traditional data-processing application software. 
Data with many entries (rows) offer greater statistical power, while data with higher complexity (more attributes or columns) may lead to a higher false discovery rate.

Code:
def file_read_tuba(fname):
    with open(fname,"r") as myfile:
        data = myfile.readlines()
        print(data)
file_read_tuba('Python.txt')

Output:
5.Write a Python program to read a file line by line store it  into an array

Big data primarily refers to data sets that are too large or complex to be dealt with by traditional data-processing application software. 
Data with many entries (rows) offer greater statistical power, while data with higher complexity (more attributes or columns) may lead to a higher false discovery rate.

Code:
def file_read_tuba(fname):
    content_array =[]
    with open(fname) as f:
        #Content_list is ther list that contain the read lines.
        for line in f:
            content_array.append(line)
        print(content_array)        
file_read_tuba('Python.txt')

Output:
6.Write a Python program to find the longest words.

Code:
apple banana cherry
dog elephant giraffe
python programming language
open artificial intelligence

def longest_word_tuba(filename):
    with open(filename,'r') as infile:
        words = infile.read().split()
    max_len = len(max(words,key = len))
    return[word for word in words if len(word) == max_len]
print(longest_word_tuba('Data.txt'))

Output:
7. Write a python program to count the frequency of words in a file.

Big data primarily refers to data sets that are too large or complex to be dealt with by traditional data-processing application software. 
Data with many entries (rows) offer greater statistical power, while data with higher complexity (more attributes or columns) may lead to a higher false discovery rate.

Code:
from collections import Counter
def word_count_tuba(fname):
    with open(fname) as f:
        return Counter(f.read().split())
print("Number of words in the file:",word_count_tuba("Python.txt"))

Output:
8.Write a Python program to assess if a file is closed or not.

Big data primarily refers to data sets that are too large or complex to be dealt with by traditional data-processing application software. 
Data with many entries (rows) offer greater statistical power, while data with higher complexity (more attributes or columns) may lead to a higher false discovery rate.

Code:
f_tuba = open('abc.txt','r')
print(f_tuba.closed)
f_tuba.close()
print(f_tuba.closed)

Output:
9.Write a python program using open command which will open the file in the read mode and the loop which will print each line present in the file.

Code:
Arts: BA in Philosophy ,BA in History
Commerce: B.COM, BAF, BMS, BMM
Science: Bsc in CS, Bsc in Physics, Bsc in Maths

# a file named "geek", will be opened with the reading mode.
file = open('Khalsa.txt', 'r')
# This will print every line one by one in the file
for each in file:
	print (each)

Output:
10.Write a Python program to split the lines while reading file in Python.The
Split function will split the variable when the space is encountered

Code:
GN Khalsa College of Arts ,Science ,Commerce
NMIMS
Ramnivas Ruia Junior College
Somaiya College
SIES College

# Python code to illustrate split() function
with open("College.txt", "r") as file:
	data = file.readlines()
	for line in data:
		word = line.split()
		print (word)

Output:
