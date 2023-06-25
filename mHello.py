n=int(input('Enter a no. '))
b=[]
for i in range(1,11):
   
    b.append(str(i*n))
vertical = " \n ".join(b)
print(vertical)
