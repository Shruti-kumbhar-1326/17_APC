#27.	Email Validator 
	#Validate whether a given email address follows a valid format. 

email = input("Enter an email address: ")

if ("@" in email and
    email.count("@") == 1 and
    "." in email and
    email.index("@") < email.rindex(".") and
    email[0] != "@" and
    email[-1] != "."):
    print("Valid Email")
else:
    print("Invalid Email")