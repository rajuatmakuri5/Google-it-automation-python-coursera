#! /usr/env/bin python3

def format_username(first_name, last_name):
    if first_name!="" and last_name!="":
        return 'Your formatted user name is {},{}'.format(last_name,first_name)
    elif first_name == "" or last_name =="":
        return 'Your formatted user name is {}{}'.format(last_name,first_name)
    else:
        return ""

print(format_username("Ernest", "Hemingway"))
print(format_username("", "Madonna"))
print(format_username("", ""))
