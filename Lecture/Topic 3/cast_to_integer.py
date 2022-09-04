"""
Program: cast_to_integer.py
Author: Alex Sargent
Last date modified: 09/03/2022

The purpose of this program is to accept any input,
convert to a integer type and output the integer.
"""
#get input and assign to variable
cups_consumed = input("Please enter number of Reese's Potato Chips Big Cups eaten: ")

#cast input to integer
calories_consumed = int(cups_consumed) * 180
#print
print("You have consumed " + " " + str(calories_consumed) + " " +"calories")
