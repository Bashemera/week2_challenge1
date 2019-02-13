from datetime import datetime
def ageBracket():
    try:
        this_year=datetime.now().year
        inputyear=int(input("Please enter your year of Birth \n"))
        if(inputyear<0):
            print("Your year of Birth cannot be a negative")
        elif (inputyear>this_year):
            print("Your year of birth cannot be greater than the current year")
        else:
            person_age = this_year - inputyear
            if(person_age <18):
                print("You are a minor")
            elif(person_age>18 and person_age<36):
                print("You are a youth")
            else:
                print("You are an elder")
    except ValueError:
        print("This is not a valid year")

if __name__=="__main__":
    ageBracket()
