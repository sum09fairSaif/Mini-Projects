# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:06:22 2024

@author: saifs
"""
from datetime import date
import os

def is_leap_year(today_year):
    """ Returns True if the current year passed in as a parameter to this function is in a leap year, and False otherwise."""
    if today_year % 400 == 0:
        return True
    elif today_year % 100 == 0:
        return False
    elif today_year % 4 == 0:
        return True
        
    return False



def days_in_month(today_month, today_year):
    """ Returns the number of days in the month passed in as a parameter into this function (today_month)"""
    numdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(today_year) == True:
        numdays[2] = 29
        
    return numdays[today_month] 



def is_two_week_dates_there(today1, two_week_dates_lst):
    """checks whether the present date falls within the two-week period of car park space booking; if it does, nothing happens and the dates are simply pulled from the text file in which it is stored, to be used for booking; if it does not, then all data are erased, and a new two-week period is started, with new visitors' booking information stored"""
    if os.stat("Two-Week Dates Available.txt").st_size == 0:
        file = open("Two-Week Dates Available.txt", "w")
        two_week_dates_lst = dates_available_for_booking(two_week_dates_lst)
        file.write(str(two_week_dates_lst))
        file.close()
        car_parking_spaces_booked_lst = ["0"] + [[["0"] + ["N"] * 20] for q in range(1, 15)]
        return 0
    else:
        file = open("Two-Week Dates Available.txt", "r")
        for line in file:
            line = line[:-1]
        file.close()
        two_week_dates_lst = line
        if today1 not in two_week_dates_lst:
            with open("Two-Week Dates Available.txt", "w") as file1:
                file1.truncate(0)
            file1.close()
            with open("Visitors Booking Details.txt", "w") as file3:
                file3.truncate(0)
            file3.close()
            return -1
        else:
            return 1
                
        
        
def dates_available_for_booking(two_week_dates_lst):
    """gets today's date by using the today() method of the date class from the datetime Python library"""
    two_week_dates_lst = ["0"]
    today = date.today()
    today = str(today)
    today = today.replace("-", "/")
    two_week_dates_lst.append(today)
    
    """then computes and displays a set of dates within 2 weeks that are available for booking a car parking space"""
    dates_count = 0
    while dates_count < 13:
        today_year_month_day_lst = today.split("/")
        today_year = today_year_month_day_lst[0]
        today_year = int(today_year)
        today_month = today_year_month_day_lst[1]
        today_month = int(today_month)
        today_day = today_year_month_day_lst[-1]
        today_day = int(today_day)
        if today_month == 12 and today_day == 31:
            today_month = 1
            today_day = 1
            today_year += 1
        elif today_day == days_in_month(today_month, today_year):
            today_day = 1
            today_month += 1
        else:
            today_day += 1
            
        today_year = str(today_year)
        today_month = str(today_month)
        today_day = str(today_day)
        
        today = (today_year+"/"+today_month+"/"+today_day)
        two_week_dates_lst.append(today)
        
        dates_count += 1
        
    print()
    print("The following dates are available for booking:- ")
    for i in range(1, len(two_week_dates_lst)):
        print(str(i)+".   "+two_week_dates_lst[i])
        
    print()
    return two_week_dates_lst   
  


def is_two_week_parking_spaces_full(car_parking_spaces_booked_lst):
    """checks whether there are anymore vacant car parking spaces left within the entirety of the 2 weeks; if it is so, it returns True, and False otherwise"""
    for a in range(1, len(car_parking_spaces_booked_lst)):
        for h in range(1, len(car_parking_spaces_booked_lst[1])):
            if car_parking_spaces_booked_lst[a][h] == "N":
                return True
            
    return False



def car_parking_spaces_available(car_parking_spaces_booked_lst, visitor_booking_date):
    """checks whether there are any vacant car park spaces left to book on any particular day chosen by the visitor; if it is so, it returns True, and False otherwise"""
    for h in range(1, len(car_parking_spaces_booked_lst[1])):
        if car_parking_spaces_booked_lst[visitor_booking_date][h] == "N":
            return True
        
    return False



def general_car_park_spaces_available(car_parking_spaces_booked_lst, visitor_booking_date):
    """checks for whether anymore general car parking spaces are available on that chosen day, and returns True if this is so, and False otherwise"""
    for b in range(6, len(car_parking_spaces_booked_lst[1])):
        if car_parking_spaces_booked_lst[visitor_booking_date][b] == "N":
            return True
        
    return False



def parking_spaces_type_booking(car_parking_spaces_booked_lst, visitor_booking_date, visitor_car_park_space):
    """asks the visitor if they want accessible car parking spaces or general car parking spaces, and allocates the booking of the park spaces accordingly"""
    while True:
        print("Y: Accessible Parking Space")
        print("N: General Parking Space")
        print()
        visitor_park_space_type = str(input("Do you want an accessible parking space? Type 'Y' for yes and 'N' for no: "))
        visitor_park_space_type = visitor_park_space_type.upper()
        if visitor_park_space_type == 'Y' or visitor_park_space_type == 'N':
            break
        else:
            print("Invalid input. Please try again.")
            print()
    

    is_car_park_space = car_parking_spaces_available(car_parking_spaces_booked_lst, visitor_booking_date)
    if is_car_park_space == False:
        print("Sorry, there are no more parking spaces available for booking. Choose another date.")
        print()
        return 0, "0"
    else:
        if visitor_park_space_type == 'Y':
            visitor_booking_type = "Accessible"
            for i in range(1, len(car_parking_spaces_booked_lst[1])):
                if car_parking_spaces_booked_lst[visitor_booking_date][i] == "N":
                    visitor_car_park_space = i
                    car_parking_spaces_booked_lst[visitor_booking_date][i] = "Y"
                    break
    
        else:
            visitor_booking_type = "General"
            if general_car_park_spaces_available(car_parking_spaces_booked_lst, visitor_booking_date) == True:
                for j in range(20, 5, -1):
                    if car_parking_spaces_booked_lst[visitor_booking_date][j] == "N":
                        visitor_car_park_space = j
                        car_parking_spaces_booked_lst[visitor_booking_date][j] = "Y"
                        break
            
            else:
                print("Sorry, we have no more general car parking spaces left for that day. All other parking spaces are reserved for visitors choosing accessible spaces.")
                print()
                return 0, "0"
        
    return visitor_car_park_space, visitor_booking_type
    
    
def main(visitors_info, two_week_dates_lst, visitor_booking_date, visitor_car_park_space, visitor_booking_type):
    """takes in inputs from the visitor (user) regarding their names, their car license numbers, as well as the day within the two-week period within which they want to book the car parking space"""
    print("Visitor Car Parking Space Booking Website")
    print("Hello visitor! Welcome to this booking website!")
    print()
    while True:
        visitor_name = str(input("Enter your name: "))
        visitor_name = visitor_name[0].upper() + visitor_name[1:]
        print(visitor_name+", thank you for choosing to book a parking space at our organisation!")
        print()
        
        visitor_car_licence_num = str(input("Enter your car licence number: "))
        print()
        
        visitor_booking_date = 0
        while visitor_booking_date < 1 or visitor_booking_date > 14:
            two_week_dates_lst = dates_available_for_booking(two_week_dates_lst)
            visitor_booking_date = int(input("Enter any number from 1-14 to select the date of your parking space booking: "))
            start_booking_date = 0
            for c in range(1, len(two_week_dates_lst)):
                if today1 == two_week_dates_lst[c]:
                    start_booking_date = c
            if start_booking_date <= visitor_booking_date <= 14:
                print()
                break
            elif visitor_booking_date > 14:
                print("You can only book a maximum of 2 weeks in advance.")
                continue
            else:
                print("Invalid input. Please try again.")
        
        print()
        
        if is_two_week_parking_spaces_full(car_parking_spaces_booked_lst) == False:
            print("Sorry, there are no more parking spaces available for booking within this two-week period.")
            print("See you next time!")
            print()
            car_park_usage_statistics(visitors_info, two_week_dates_lst)
            return "done"
        elif is_two_week_parking_spaces_full(car_parking_spaces_booked_lst) == True:
            visitor_car_park_space, visitor_booking_type = parking_spaces_type_booking(car_parking_spaces_booked_lst, visitor_booking_date, visitor_car_park_space)
            if visitor_car_park_space == 0:
                main(visitors_info, two_week_dates_lst, visitor_booking_date, visitor_car_park_space, visitor_booking_type)
 
                
        print()
        print("Thank you for giving us all your details! The booking has been confirmed!")
        print("Your car parking space is Space ", visitor_car_park_space)
        print("See you on ", two_week_dates_lst[visitor_booking_date], "!")
        print()
        print()
        print()
        
        this_visitor_info = [visitor_name, visitor_car_licence_num, two_week_dates_lst[visitor_booking_date], visitor_car_park_space, visitor_booking_type]
        visitors_info.append(this_visitor_info)
        file2 = open("Visitors Booking Details.txt", "a")
        file2.write(str(visitors_info))
        file2.close()
        
    
        
def car_park_usage_statistics(visitors_info, two_week_dates_lst):
    """computes and outputs the numbers of each type of parking spaces used, as well as total spaces used, on any of the 14 days as well as the total time period"""
    for date1 in two_week_dates_lst:
        one_day_accessible_spaces = 0
        one_day_general_spaces = 0
        one_day_total_spaces = 0
        for visitor in visitors_info:
            if date1 in visitor:
                if visitor[-1] == "Accessible":
                    one_day_accessible_spaces += 1 
                else:
                    one_day_general_spaces += 1
                    
        one_day_total_spaces = one_day_accessible_spaces + one_day_general_spaces
        print()
        print("On ", date1, ":-")
        print("Number of accessible spaces used: ", one_day_accessible_spaces)
        print("Number of general spaces used: ", one_day_general_spaces)
        print("Total number of spaces used: ", one_day_total_spaces)
        print()
        print()
                
    two_week_accessible_spaces = 0
    two_week_general_spaces = 0
    two_week_total_spaces = 0
    
    for visitor in visitors_info:
        if visitor[-1] == "Accessible":
            two_week_accessible_spaces += 1 
        else:
            two_week_general_spaces += 1
            
    two_week_total_spaces = two_week_accessible_spaces + two_week_general_spaces
    print("Over the two-week period:-")
    print("Number of accessible spaces used: ", two_week_accessible_spaces)
    print("Number of general spaces used: ", two_week_general_spaces)
    print("Total number of spaces used: ", two_week_total_spaces)
    print()
    print()
        
    
    
    
    
visitors_info = []
two_week_dates_lst = ["0"]
car_parking_spaces_booked_lst = [["0"]] + [["0"] + ["N"] * 20 for q in range(1, 15)]
visitor_booking_date = 0
visitor_car_park_space = -1
visitor_booking_type = ''
today1 = date.today()
today1 = str(today1)
today1 = today1.replace("-", "/")
print("Today is ", today1)
if is_two_week_dates_there(today1, two_week_dates_lst) == -1:
    print("This is the starting of a new two-week booking period.")
    is_two_week_dates_there(today1, two_week_dates_lst)
    car_parking_spaces_booked_lst = ["0", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N"]
main(visitors_info, two_week_dates_lst, visitor_booking_date, visitor_car_park_space, visitor_booking_type)