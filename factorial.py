def fact(n):
    if n==0 :
        return 1
    else :
        return n*fact(n-1)
su=lambda a,b:a+b
print("factorial = ",fact(int(input("enter a number for fact :"))))
print(su(int(input("enter a number :")),int(input("enter another number :"))))