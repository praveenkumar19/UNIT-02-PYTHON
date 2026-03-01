sp = set("!@#$%^&*()_+-=[]{}|;:',.<>?/")
while True:
    a = input("Enter your password: ")
    has_digit = set(a) & set("0123456789")
    has_upper = set(a) & set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    has_special = set(a) & sp
    if len(a) >= 16 and has_digit and has_upper and has_special:
        print("Password is strong.")
        break
    else:
        print("Password is weak. Try again.")
