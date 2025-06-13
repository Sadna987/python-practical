def prime_no(n):
    assert n>0
    flg=0
    for i in range(2,n):
        if n%i==0:
            print(n, "is not a prime number")
            flg=1
            break
    if flg==0:
        print(n, "is a prime number")

def all_prime(n):
    print()
    assert n>0
    print("FOLLOWING ARE THE PRIME NUMBER TILL", n)
    for i in range(2,n+1):
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag=1
                break
        if flag==0:
            print(i, end=" ")
    print()
def first_prime(n):
    print()
    print()
    print("FIRST",n,"PRIME NUMBERS ARE:")
    assert n>0
    c=0
    a=2
    while c!=n:
        flag=0
        for i in range(2,a):
            if (a%i)==0:
                a=a+1
                flag=1
                break
        if (flag==0):
            print(a, end=" ")
            c=c+1
            a=a+1
    print()
def main():
    ch="y"
    while ch=="y":
        print("1)CHECK IF “n” IS PRIME")
        print("2)GENERATE ALL THE PRIME TILL “n”")
        print("3)GENERATE FIRST “n” PRIME NUMBERS")
        choice=int(input("ENTER YOUR CHOICE:"))
        n=int(input("ENTER THE NUMBER:"))
        if choice==1:
            prime_no(n)
        elif choice==2:
            all_prime(n)
        elif choice==3:
            first_prime(n)
        else:
            print("INVALID INPUT")
        ch=input("ENTER TO CONTINUE y:")
if __name__=="__main__":
    main()
