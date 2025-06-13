def identifychar(char):
    if len(char)>=2:
        print("INVALID INPUT")
    else:
        asc=ord(char)
        if asc>=65 and asc<=90 or asc>=97 and asc<=123:
            print(char, "IS A LETTER")
        elif char in "0123456789":
            print(char, "IS A NUMERIC DIGIT")
        elif char in "!@#$%^&*~`?/+-*/.":
            print(char, "IS A SPECIAL CHARACTER")

def upper_lower(char):
    if len(char)>=2:
        print("INVALID INPUT")
    else:
        asc=ord(char)
        if asc>=65 and asc<=90:
            print(char, "IS UPPER CASE")
        elif asc>=97 and asc<=123:
            print(char, "IS LOWER CASE")
        else:
            print("INVALID INPUT")
def numeric_name(char):
    if len(char)>=2:
        print("INVALID INPUT")
    else:
        l=["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
        if char in "0123456789":
            NUM=int(char)
            print(l[NUM])
def main():
    ch="y"
    while ch=="y":
        print("1. TO IDENTIFY GIVEN CHARACTER")
        print("2. TO IDENTIFY IF LETTER IS UPPER OR NOT")
        print("3. TO GIVE THE NAME OF NUMERIC DIGIT")
        choice=int(input("ENTER YOUR CHOICE:"))
        char=input("ENTER A CHARACTER:")
        if choice==1:
            identifychar(char)
        elif choice==2:
            upper_lower(char)
        elif choice==3:
            numeric_name(char)
        ch=input("ENTER TO CONTINUE y:")
if __name__=="__main__":
    main()
