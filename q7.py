# 7)WRITE A FUNCTION THAT ACCEPTS TWO STRINGS AND RETURNS THE INDICES OF ALL THE OCCURRENCES OF THE SECOND STRING
#   IN THE FIRST STRING AS A LIST. IF THE SECOND STRING IS NOT PRESENT IN THE FIRST STRING THEN IT SHOULD RETURN -1

def indexoccur(str1,str2):
    l=[]
    index=0
    j=0
    while(j!=-1):
       j= str1.find(str2,index)
       if(j!=-1):
           l.append(j)
           index=j+1
    if (len(l)==0):
      return -1
    else:
      return l
def main():               
    str1=input("ENTER THE FIRST STRING:")
    str2=input("ENTER THE SECOND STRING:")
    rslt=indexoccur(str1,str2)
    if rslt ==-1:
        print("RESULTED LIST  IS empty",rslt)
    else:
        print("RESULTED LIST :", rslt)
if __name__=="__main__":
    main()
