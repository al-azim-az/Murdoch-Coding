attempt = 1
max_attempt = 3

while attempt <= max_attempt:
    password = input("Enter Password: ")

    if password == "python":
        print("Unlocked")
        break
    else:
        print("Try Again")

    attempt += 1