age = input("Are you a cigarette addict older than 75 years old? (please answer yes or no) :")
if age == "yes" :
    age = True
elif age == "no":
    age = False

chronic = input("Do you have a severe chronic disease? (please answer yes or no) :")
if chronic == "yes" :
    chronic = True
elif chronic == "no":
    chronic = False

immune = input("Is your immune system too weak? (please answer yes or no) :")
if immune == "yes" :
    immune = True
elif immune == "no":
    immune = False

if age or chronic or immune == True :
    print("You are in risky group")
elif age or chronic or immune == False :
    print("You are not in risky group")
