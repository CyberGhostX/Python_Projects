#!/usr/bin/python3
#!bin/python3

import pdftotext

def convert(filename):

    with open(filename,"rb") as file:
        pdf = pdftotext.PDF(file)

    with open("converted.txt","w") as f:
        f.writelines(pdf)

    print("Done")

i = input("Enter your filename : ")

print(convert(i))
