def format_name(f_name,l_name):
    return f_name.title() +" "+ l_name.capitalize()



f = input("What is your first name: ")
l = input("What is your last name: ")

name = format_name(f,l)


print(name)