def format_name(f_name,l_name):
    return f_name.title() +" "+ l_name.capitalize()



f = input("What is your first name: ")
l = input("What is your last name: ")

name = format_name(f,l)


print(name)
def is_leap (year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
            else:
                print("Not leap year")
        else:
            print("Leap year")
    else:
        print("Not leap year")

# TODO: Add more code here 👇
def days_in_month():
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]