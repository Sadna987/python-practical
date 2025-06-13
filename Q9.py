def totalchar():
    f=open("poem.txt","r")
    s=f.read()
    c=0
    d={}
    for i in s:
        c=c+1
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
    f.close()
    return c,d
def wordcount():
    f=open("poem.txt","r")
    l=f.readlines()
    c=0
    d=0
    s=""
    for i in l:
        c=c+1
        for j in i:
            d=d+1
        s=i[0:]+s
    f.close()
    return c,d,s
def copyfile():
    f=open("poem.txt","r")
    File1=open("File1.txt","w")
    File2=open("File2.txt","w")
    l=f.readlines()
    for i in range(len(l)):
        if i%2==0:
            File2.write(l[i])
        else:
            File1.write(l[i])
    f.close()
    File1.close()
    File2.close()
    print("..............FILE COPIED............")
def main():
    ch="y"
    while ch=="y":
        print("1. TO PRINT THE TOTAL NUMBER OF CHARACTERS, WORDS, LINES IN THE FILE ")
        print("2. TO CALCULATE THE FREQUENCY OF EACH CHARACTER IN THE FILE AND REMAIN A COUNT IN A DICTIONARY")
        print("3. TO PRINT THE WORDS IN REVERSE ORDER")
        print("4. TO COPY EVEN LINES OF THE FILE TO A FILE NAMED 'File1' AND ODD LINES TO 'File2'")
        choice=int(input("ENTER YOUR CHOICE:"))
        if choice==1:
            rs,rd=totalchar()
            fs,fd,ft=wordcount()
            print(" The number of characters in the file including spaces is : ",rs)
            print(" The number of words in the file is : ",fs)
            print(" The number of lines in the file is : ",fd)           
        elif choice==2:
            rs,rd=totalchar()
            print(" The frequency of each character in the file is : \n ",rd)
        elif choice==3:
            fs,fd,ft=wordcount()
            print("The words in reverse order are: \n", ft)
        elif choice==4:
            copyfile()           
        ch=input("ENTER TO CONTINUE y:")
if __name__=="__main__":
    main()
    


    
        
        
    
