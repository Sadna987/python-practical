def pyramid ():
    rows = int(input("Enter number of rows: ")) 
    k = 0
    for i in range(1, rows+1):
        for space in range(1, (rows-i)+1):
            print(end="  ")
        while k!=(2*i-1):
            print("* ", end="")
            k += 1   
        k = 0
        print()
def reversepyramid():
    rows = int(input("Enter number of rows: "))
    for i in range(rows, 1, -1):
        for space in range(0, rows-i):
            print("  ", end="")
        for j in range(i, 2*i-1):
            print("* ", end="")
        for j in range(1, i-1):
            print("* ", end="")
        print()
def main():
    ch="y"
    while ch=="y":
        print("1) To print the pyramid")
        print("2) To print the reverse pyramid")
        ch=int(input("ENTER THE CHOICE:"))
        if ch==1:
            pyramid()
        elif ch==2:
            reversepyramid()
        ch=input("DO YOU WANT TO CONTINUE:")
if __name__=="__main__":
    main()
