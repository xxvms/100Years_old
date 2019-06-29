#!/usr/bin/python3
import datetime;

name = input("Please provide your name: ")
age = input("Please provide year when you have been born: ")

user_input = int(age)
now = datetime.datetime.now()


def ageID(unser_input):
    result :int = 0
    result = 100 - user_input
    result += now.year
    return result


def frombirth(user_input_f, current_year):
    full_age :int = 0
    full_age = user_input_f + 100
    current_age: int = 0
    current_age = current_year - user_input_f
    dates = [full_age, current_age]

    return dates


print("Hello " + name + " we are in " + str(now.year))


user_age = frombirth(user_input, now.year)

print("and you will be 100 years old in: " + str(user_age[0]) + " and you are currently " + str(user_age[1]))




