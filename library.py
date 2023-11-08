class multifunction():
    def subfield():
        list=('Sub-fields in AI are:','Machine Learning' ,"Neural Networks" , "Vision" ,"Robotics", "Speech Processing" , 
              "Natural Language Processing")
        for temp in list:
            print(temp) 
        return

    def oddeven():
        num=int(input("enter the number:"))    
        if(num%2)==0:
            print(num,"is even number")
        else:
            print(num,"is odd number")
        return

    def eligible():
        gender=input("enter your gender:")
        age=int(input("enter your age:"))
        if(gender=='male'and age>=24):
            print("your eligible for marriage")
        elif(gender=='female'and age>=18):
            print("your eligible for marriage")
        else:
            print("your  not eligible for marriage")
            return

    def percentage():
        a=int(input("subject1 :"))
        b=int(input("subject2 :"))
        c=int(input("subject3 :"))
        d=int(input("subject4 :"))
        e=int(input("subject5 :"))
        add=a+b+c+d+e
        print("total",add)
        ave=(add/5)
        print("percentage",ave)
        return 
    
    def triangle():  
        h=int(input("Height :"))
        b=int(input("Breath :"))
        print("area formla = (h*b)2")
        areaformula=((h*b)/2)
        print("area of triangle :",areaformula)
        h1=int(input("Height1 :"))
        h2=int(input("Height2 :"))
        b1=int(input("Breath :"))
        print("perimeter formla = h1+h2+b")
        perimeter=(h1+h2+b1)
        print("perimeter of triangle:",perimeter)
        return