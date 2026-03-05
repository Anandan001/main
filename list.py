mylist = [1,2,3,4,5,6]
for i in mylist :
 print(i)
n = int(input("enter a number"))
mylist.append(n)
for i in mylist :
 print(i)
print("sum of list is ",sum(mylist))