def name():
    name = input('enter your name: \n')
    c = 0
    s = '"[@_!#$%^&*()<>?/\|}{~:]"'
    for i in range(len(name)):
        if name[i] in s or name[i].isdigit():
            c=c+1
    if c==0:
        print("your name is " + name)
    else:
        try:
            raise Exception('Invalid character')
        except Exception as e:
            print(e)
def main():
    name()
if __name__=="__main__":
    main()
