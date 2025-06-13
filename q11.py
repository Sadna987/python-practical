# 11) WRITE A FUNCTION THAT PRINTS A DICTIONARY WHERE THE KEYS ARE NUMBERS BETWEEN 1 AND 5
# AND THE VALUES ARE CUBES OF THE KEYS.

def dictfunc():
    d={}
    for i in range(1,6):
        d[i]=i**3
    print("The dictionary is:",d)
def main():
    dictfunc()
if __name__=="__main__":
    main()

