def format_name():
    f_name = input("What's your first name ?")
    l_name = input("What's your last name ?")
    format_f = f_name.title()
    format_l = l_name.title()
    return f"{format_f} {format_l}"
print(format_name())