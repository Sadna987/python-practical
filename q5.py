def frequency_char(st,ch):
    c=0
    for i in st:
         if i==ch:
             c=c+1
    return c
def replace_char(st,a,b):
    nst=""
    for i in st:
        if i==a:
            nst=nst+b
        else:
            nst=nst+i
    return nst
def remove_first(st,cha):
    nsti=""
    for i in range (len(st)):
        if (st[i]==cha):
            break
    nsti=st[0:i]+ st[i+1:len(st)]
    return nsti
def remove_all(st,cha):
    nstn=""
    for i in st:
        if i==cha:
            continue
        nstn=nstn+i
    return nstn

def main():
    ch="y"
    while ch=="y":
        print("1. To get the frequency of a character in the string")
        print("2. To replace a character with another")
        print("3. To remove the first occurance of the character")
        print("4. To remove all the occurances of a character")
        choice=int(input("ENTER YOUR CHOICE:"))
        st=input("Enter the string: ")
        if choice==1:
            ch=input("Enter the character:")
            rs=frequency_char(st,ch)
            print("THE FREQUENCY OF THE CHARACTER",ch,"IS",rs)
        elif choice==2:
            a=input("Enter the character which you want to replace:")
            b=input("Enter the new character:")
            rslt=replace_char(st,a,b)
            print("THE NEW CHARACTER IS",rslt)
        elif choice==3:
            cha=input("Enter the character whose first occurance is to be removed:")
            rslt=remove_first(st,cha)
            print("THE NEW CHARACETR IS",rslt)
        elif choice==4:
            ch=input("Enter the character whose all occurances are to be removed:")
            rslt=remove_all(st,cha)
            print("THE NEW CHARACTER IS",rslt)
        ch=input("ENTER TO CONTINUE y:")
if __name__=="__main__":
    main()
