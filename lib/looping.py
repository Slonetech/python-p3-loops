#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")


int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def square_integers(int_list):
    int_list_squared = [int_list[i]**2 for i in range(len(int_list))]
    return int_list_squared

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)
