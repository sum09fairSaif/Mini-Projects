# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:00:41 2024

@author: saifs
"""

### ------------------------ Start of Program Code ----------------------------------------------------------------------------------------------------------------------------------- ###

from datetime import date

def today_date_store():
    """uses and calls the datetime function from the Python library to get today's date"""
    today = date.today()
    
    """uses the today's date obtained to store it permanently in memory, using a .txt file, as it will be used to check and update membership details for the following year"""
    file = open("Swimming Club Annual Audit Access Dates List.txt", "w")
    file.write(str(today))
    file.close



def membership_types_table():
    """displayes the table of membership types available"""
    membership_type_grid = [["Junior", "Ages 2 - 17", "$10.00"],
                            ["Adult", "Ages 18 - 49", "$20.00"],
                            ["Senior", "Ages 50 - 79", "$15.00"],
                            ["Golden", "Ages 80 and over", "Free ($0)"]]
    
    for row in range(len(membership_type_grid)):
        print(membership_type_grid[row][0]+"          "+membership_type_grid[row][1]+"          "+membership_type_grid[row][2])
        
    print()
    
    return membership_type_grid

    

def main(swimming_club_member_details):
    """takes inputs from the users about the membership details of members as well as non-members of the swimming club, and validates the entry of data to the system"""
    print()
    print("Hello! Welcome to the Swimming Club Annual Audit!")
    print()
    
    total_member_count = 0
    
    while total_member_count < 20:
        """taking down details about the members"""
        member_name = str(input("Enter your name: "))
        first_letter = member_name[0].upper()
        member_name = first_letter + member_name[1:]
        
        print()
        
        print("Welcome, "+member_name+"!")
        
        print()
        
        while True:
            member_age = int(input("Enter your age: "))
            if 2 <= member_age <= 150:
                break
            else:
                print("Invalid age input. Please try again.")
               
        print()
        
        while True:
            print("M : Male"+"\n"+"F : Female"+"\n"+"O : Other"+"\n"+"N : Prefer not to say")
            member_gender = str(input("Enter the letter that best tells your gender: "))
            member_gender = member_gender.upper()
            if member_gender in ["M", "F", "O", "N"]:
                break
            else:
                print("Invalid gender input. Please try again.")
                
        print()
        
        membership_grid = membership_types_table()
        
        if 2 <= member_age < 18:
            member_type = membership_grid[0][0]
        elif 18 <= member_age < 50:
            member_type = membership_grid[1][0]
        elif 50 <= member_age < 80:
            member_type = membership_grid[2][0]
        else:
            member_type = membership_grid[3][0]
             
        print("Since you are age "+str(member_age)+" , you are "+member_type+" member")
        
        print()
        
        while True:
            is_member = str(input("Are you a team member? Type 'Y' for Yes and 'N' for No: "))
            is_member = is_member.upper()
            if is_member == 'Y' or is_member == 'N':
                break
            else:
                print("Invalid input. Please try again.")
                
        print()
        
        if 2 <= member_age < 18:
            member_annual_fee = membership_grid[0][2]
        elif 18 <= member_age < 50:
            member_annual_fee = membership_grid[1][2]
        elif 50 <= member_age < 80:
            member_annual_fee = membership_grid[2][2]
        else:
            member_annual_fee = "$0.00"
            
        if is_member == "Y":
            member_annual_fee = member_annual_fee.replace("$", "")
            member_annual_fee = float(member_annual_fee)
            member_annual_fee *= 0.90
            member_annual_fee = str(member_annual_fee)
            member_annual_fee = "$" + member_annual_fee
            
            print("Since you are a team member, your annual fee is ", member_annual_fee)
            
        else:
            print("Since you are NOT a team member, your annual fee is ", member_annual_fee)
            
        print()
            
        while member_type != "Golden":
            is_member_fee_paid = str(input("Have you paid your annual fee? Type 'Y' for Yes and 'N' for No: "))
            is_member_fee_paid = is_member_fee_paid.upper()
            if is_member_fee_paid == 'Y' or is_member_fee_paid == 'N':
                break
            else:
                print("Invalid input. Please try again.")
                    
        print()
            
            
        if member_type != "Golden":
            swimming_club_member_details += [[str(total_member_count), member_name, member_age, member_gender, member_type, is_member, member_annual_fee, is_member_fee_paid]]
        else:
            swimming_club_member_details += [[str(total_member_count), member_name, member_age, member_gender, member_type, is_member, member_annual_fee, "Free ($0)"]]
            
        print("Thank you for giving us all the above details! Your annual membership number is: ", total_member_count)
        print()
        print()
        print()
        
        total_member_count += 1  
        
        
        
def annual_audit_stats(swimming_club_member_details):
    
    """counts the number of current members by membership type"""
    total_junior_members = 0
    total_adult_members = 0
    total_senior_members = 0
    total_golden_members = 0
    
    """also counts the number of members of each type who did not pay the annual fee"""
    junior_members_not_paid = 0
    adult_members_not_paid = 0
    senior_members_not_paid = 0
    
    for row in range(len(swimming_club_member_details)):
        member = swimming_club_member_details[row]
        if "Junior" in member:
            total_junior_members += 1
        elif "Adult" in member:
            total_adult_members += 1
        elif "Senior" in member:
            total_senior_members += 1
        else:
            total_golden_members += 1
            
        if "Junior" in member and member[-1] == "N":
            junior_members_not_paid += 1
        elif "Adult" in member and member[-1] == "N":
            adult_members_not_paid += 1
        elif "Senior" in member and member[-1] == "N":
            senior_members_not_paid += 1
            
    """calculates the percentage of members of each type who haven't paid, and displays the information"""
    percent_not_junior_paid = (junior_members_not_paid / total_junior_members) * 100
    percent_not_adult_paid = (adult_members_not_paid / total_adult_members) * 100
    percent_not_senior_paid = (senior_members_not_paid / total_senior_members) * 100
    
    print(str(percent_not_junior_paid)+"% of the Junior members have not paid the annual fee.")
    print(str(percent_not_adult_paid)+"% of the Adult members have not paid the annual fee.")
    print(str(percent_not_senior_paid)+"% of the Senior members have not paid the annual fee.")
    
    """calculates and displays the expected total fees and the annual fees received"""
    expected_total_fees = (total_junior_members * 10) + (total_adult_members * 20) + (total_senior_members * 15)
    received_total_fees = ((total_junior_members - junior_members_not_paid)*10 + (total_adult_members - adult_members_not_paid)*20 + (total_senior_members-senior_members_not_paid)*15)
    print()
    print("An annual fee of $"+str(expected_total_fees)+" is expected to be received this year.")
    print("But an annual fee of $"+str(received_total_fees)+" has been received.")

    print()



def is_date_next_year(swimming_club_member_details):
    """gets today's date by using and calling the datetime function from the Python library"""
    today = date.today()
    today = str(today)
    print("Today's date is: ", today)
    today = today.split("-")
    
    """checks whether the date entered is in the same year or the following year"""
    file = open("Swimming Club Annual Audit Access Dates List.txt", "r")
    for line in file:
        line = line[:-1]
        fields = line.split('-')
        
    if int(fields[-3]) != int(today[0]):
        membership_update_next_year(swimming_club_member_details)
    elif int(fields[-3]) == int(today[0]):
        today_date_store()



def membership_update_next_year(swimming_club_member_details):
    """checks if any members have not paid for the previous year, outputs those members and removes them from the swimming club audit list"""
    members_not_paid_last_year_lst = []
    remove_indices = []
    membership_grid = membership_types_table()
    
    for i in range(len(swimming_club_member_details)):
        member = swimming_club_member_details[i]
        if member[-1] == "N":
            members_not_paid_last_year_lst += [member[1]]
            remove_indices += [i]
           
    print("The following members have not paid last year's annual membership fee:- ")
    for not_members in members_not_paid_last_year_lst:
        print(not_members)
        
    print()
    
    print("I'm sorry, but these members can no longer remain in our system.")
    print("If you are in the above list, my apologies. See you next time!")
    print()
    
    for i in remove_indices:
        swimming_club_member_details.pop(i)
        
    """updates the ages of the remaining members in the system"""
    for i in range(len(swimming_club_member_details)):
        member = swimming_club_member_details[i]
        member_age = member[2] + 1
        member[2] = member_age
        
    """checks whether the members are in the team, and then updates their type of membership and annual fee if required"""
    for i in range(len(swimming_club_member_details)):
        member = swimming_club_member_details[i]
        member_age = member[2]
        is_member = member[5]
        
        if 2 <= member_age < 18:
            member_type = membership_grid[0][0]
            member_annual_fee = membership_grid[0][2]
        elif 18 <= member_age < 50:
            member_type = membership_grid[1][0]
            member_annual_fee = membership_grid[1][2]
        elif 50 <= member_age < 80:
            member_type = membership_grid[2][0]
            member_annual_fee = membership_grid[2][2]
        else:
            member_type = membership_grid[3][0]
            member_annual_fee = "$0.00"
        
        if is_member == "Y":
            member_annual_fee = member_annual_fee.replace("$", "")
            member_annual_fee = float(member_annual_fee)
            member_annual_fee *= 0.90
            member_annual_fee = str(member_annual_fee)
            member_annual_fee = "$" + member_annual_fee
                 
        member[4] = member_type
        member[6] = member_annual_fee
            
        """sets every member's fee as not paid"""
        if member[4] != "Golden" and member[5] == "Y":
            member[-1] = "N"
            
    """displays members according to membership type"""
    print()
    print()
    print("Non-members this year:- ")
    for i in range(len(swimming_club_member_details)):
        member = swimming_club_member_details[i]
        if member[5] == "N":
            print(member[1])
            
    print()
    print("Juniors:- ")
    for i in range(len(swimming_club_member_details)):
        member = swimming_club_member_details[i]
        if member[4] == "Junior":
            print(member[1])
            
    print()
    print("Adults:- ")
    for i in range(len(swimming_club_member_details)):
        member = swimming_club_member_details[i]
        if member[4] == "Adult":
            print(member[1])
            
    print()
    print("Seniors:- ")
    for i in range(len(swimming_club_member_details)):
        member = swimming_club_member_details[i]
        if member[4] == "Senior":
            print(member[1])
            
    print()
    print("Golden Members:- ")
    for i in range(len(swimming_club_member_details)):
        member = swimming_club_member_details[i]
        if member[4] == "Golden":
            print(member[1])
            
    print()
    
    
    
swimming_club_member_details = []
today_date_store()
is_date_next_year(swimming_club_member_details)
main(swimming_club_member_details)
        
            
                