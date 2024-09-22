input(f"hi how are you today?")

age = input(f"okay! to sign up, please enter your age!: ")

if isinstance(age, int):
    age = int(age)
    if age >= 18:
        print("congratulations! you are now signed up.")
    elif age  < 18:
        print("sorry! you have to be 18+ to sign up!")
else:
    print("please enter your age in numerical form")