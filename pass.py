'''Write a function that uses list comprehension to return whether a password 
meets a minimum threshold: it contains a mixture of upper- and lowercase 
letters, and at least one number'''

def passCheck(password):
    upper = [char for char in password if char.isupper()]
    lower = [char for char in password if char.islower()]
    num = [char for char in password if char.isdigit()]
    if (len(upper) > 0 and len(lower) > 0 and len(num) > 0):
        print "VALID PASSWORD"
    else:
        print "INVALID PASSWORD"

passCheck("123") #invalid
passCheck("hello") #invalid
passCheck("Hello123") #valid

'''Write a function that uses list comprehension to return a password's 
strength rating. This function should return a lower integer for a weak 
password and a higher integer for a stronger password.'''

def passStrength(password):
    upper = [char for char in password if char.isupper()]
    lower = [char for char in password if char.islower()]
    num = [char for char in password if char.isdigit()]
    other = [char for char in password if (char not in upper and char not in lower and char not in num)]
    strength = 0
    if len(password) > 7:
        strength += 1
    if len(upper) > 0:
        strength += 2
    if len(lower) > 0:
        strength += 2
    if len(num) > 0:
        strength += 2
    if len(other) > 0:
        strength += 3
    print "Strength: " + str(strength)

passStrength("123") #2
passStrength("12345678") #3
passStrength("hello") #2
passStrength("asdf1234") #5
passStrength("ASdf1234") #7
passStrength("ASdf1234!") #10
