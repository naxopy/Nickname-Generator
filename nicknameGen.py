"""
MIT License

Copyright (c) 2017 Pimoroni Ltd.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

@author:Théophile HINTZY

This small programm sends you a nickname when you want. 
Launch it in the terminal using python 3.+ 
You will have a list of 10 proposed nicknames. 
"""
import random as r

consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
vowel = ['a','e','i','o','u','y']
       
with open("save_syllabe.txt",'w') as f:
    for a in consonant:
        for b in vowel:
            syllabe = a+b
            f.write(syllabe+'\n')
            
with open("save_syllabe.txt",'r') as f:       
    x=f.readlines()
    
number_syllabe = int(input("Enter the neumber of syllabes \n"))
choice_syllabe = ""

if number_syllabe >5:
    print("The number of syllabes is too high, try under 5.")
else:
	for i in range(0,10):
		for a in range(0,number_syllabe):
			choice_syllabe+=r.choice(x)

		pseudo = choice_syllabe.replace('\n' ,"")
		choice_syllabe = ""

		print(pseudo)