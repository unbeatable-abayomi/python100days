# def format_name(f_name,l_name):
#     return f_name.title() +" "+ l_name.capitalize()



# f = input("What is your first name: ")
# l = input("What is your last name: ")

# name = format_name(f,l)


# print(name)

def is_leap (year):
    """ Returns True if year is a leap year and False if it's not """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                #print("Leap year")
                return True
            else:
                #print("Not leap year")
                return False
        else:
            #print("Leap year")
            return True
    else:
        #print("Not leap year")
         return False

# TODO: Add more code here 👇
def days_in_month(year,month):
    is_year_leaap = is_leap(year)
    month_of_year = month - 1
    #month -=1
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leaap and month_of_year == 1:
        return month_days[month_of_year] + 1
    else:
      return month_days[month_of_year]
    

ye = int(input("Input Year: "))
mo = int(input("Input Month: "))

print(days_in_month(ye,mo))
    
