def quad_eq(a,b,c):
    rs=(b*b)-(4*a*c)
    if rs>0:
        root1=(-b)+(rs**0.5)/(2*a)
        root2=(-b)-(rs**0.5)/(2*a)
        return root1,root2
    else:
        inv="invalid input"
def main():
    a=int(input("ENTER A NUMBER:"))
    b=int(input("ENTER A NUMBER:"))
    c=int(input("ENTER A NUMBER:"))
    rslt=quad_eq(a,b,c)
    print(rslt)
    
if __name__=="__main__":
    main()
