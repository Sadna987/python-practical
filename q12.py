# 12) CONSIDER A TUPLE t1=(1,2,5,7,9,2,4,6,8,10). WAP TO PERFORM FOLLOWING OPERATIONS:
# A) PRINT HALF THE VALUES OF TUPLE IN ONE LINE AND THE OTHER HALF IN NEXT LINE.
# B) PRINT ANOTHER TUPLE WHOSE VALUES ARE EVEN NUMBERS IN THE GIVEN TUPLE.
# C) CONCATENATE A TUPLE t2=(11,13,15) WITH t1.
# D) RETURN MAXIMUM AND MINIMUM VALUE FROM THIS TUPLE.

def halfvalues(t1):
    lgth=int((len(t1))/2)
    half=t1[0:lgth]
    full=t1[lgth:]
    return half,full
def eventup(t1):
    t2=tuple()
    for i in t1:
        if i%2==0:
            t2=t2+(i,)
    return t2
def concatinate(t1,t2):
    t3=t1+t2
    return t3
def maxmin(t3):
    maxm=max(t3)
    minm=min(t3)
    return maxm,minm
def main():
    t1=(1,2,5,7,9,2,4,6,8,10)
    t2=(11,13,15)
    ch="y"
    while ch=="y":
        print("1. TO PRINT HALF THE VALUES OF TUPLE IN ONE LINE AND THE OTHER HALF IN NEXT LINE ")
        print("2. TO PRINT ANOTHER TUPLE WHOSE VALUES ARE EVEN NUMBERS IN THE GIVEN TUPLE.")
        print("3. TO CONCATENATE A TUPLE t2=(11,13,15) WITH t1")
        print("4. TO RETURN MAXIMUM AND MINIMUM VALUE FROM THIS TUPLE")
        choice=int(input("ENTER YOUR CHOICE:"))
        if choice==1:
            rs,rslt=halfvalues(t1)
            print("THE RESULT IS:")
            print(rs,"\n",rslt)
        elif choice==2:
            rs=eventup(t1)
            print("THE EVEN NUMBERS IN TUPLE ARE:",rs)   
        elif choice==3:
            rs=concatinate(t1,t2)
            print("THE CONCATINATED LIST IS:",rs)
        elif choice==4:
            rs,rslt=maxmin(rs)
            print("THE MAXIMUM VALUE IS:",rs)
            print("THE MINIMUM VALUE IS:",rslt)
        ch=input("ENTER TO CONTINUE y:")
if __name__=="__main__":
    main()
    
