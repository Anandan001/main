List = [1,2,3,4,5,6]
target=int(input("enter number"))
print(List)
ind = []
for i in range(0,len(List)) :
    for j in range(0,len(List)) :
       sums= List[i] + List[j]
       if sums == target :
         ind.append(i)
         ind.append(j)
for i in range(0,len(ind),2) :
   print(ind[i],ind[i+1])

