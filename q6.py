def swapstrings(s1,s2,n):
    ns1=s2[0:n]+s1[n:]
    ns2=s1[0:n]+s2[n:]
    return ns1,ns2
def main():
    s1=input("ENTER A STRING 1:")
    s2=input("ENTER A STRING 2:")
    n=int(input("ENTER THE NUMBER TILL WHICH SWAPPING HAS TO BE DONE:"))
    N1,N2=swapstrings(s1,s2,n)
    print("THE SWAPPED STRINGS ARE:", N1, N2)
if __name__=="__main__":
    main()
