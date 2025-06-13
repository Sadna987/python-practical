# 8. WAP TO CREATE A LIST OF CUBES OF ONLY THE EVEN INTEGERS APPEARING IN THE INPUT LIST USING
# A) FOR LOOP
# B) LIST COMPREHENSION

def cubelist(l):
    nl=[]
    for i in l:
        if i.isdigit():
            n=int(i)
            if n%2==0:
                n=n**3
                nl.append(n)
    return nl

def listcom(l):
    nl=[(int(x))**3 for x in l if x.isdigit() if (int(x))%2==0]
    return nl

def main():
    l=[]
    c="y"
    while c=="y":
        n=int(input("ENTER THE NUMBER OF ELEMENTS YOU WANT IN THE LIST:"))
        print("ENTER YOUR CHOICE FROM THE FOLLOWING:")
        print("1- FOR LOOP")
        print("2- List COMPREHENSION")
        CH=int(input("ENTER YOUR CHOICE:"))
        for j in range(n):
            a=input("ENTER THE ELEMENTS OF LIST: ")
            l.append(a)
        if CH==1:
            rslt=cubelist(l)
        elif CH==2:
            rslt=listcom(l)
        print("THE RESULTED LIST IS: ", rslt)
        c=input("DO YOU WANT TO CONTINUE y/n:")
if __name__=="__main__":
    main()
    
