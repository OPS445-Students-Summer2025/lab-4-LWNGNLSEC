#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(string):
    # Place code here - refer to function specifics in section below
    sub_string = string[:5]
    return sub_string

def last_seven(string):
    # Place code here - refer to function specifics in section below
    sub_string = string[-7:]
    return sub_string

def middle_number(num):
    # Place code here - refer to function specifics in section below
    string = str(num)
    sub_string = string[1:3]
    return sub_string

def first_three_last_three(string1, string2):
    # Place code here - refer to function specifics in section below
    sub_string = string1[:3] + string2[-3:]
    return sub_string

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))