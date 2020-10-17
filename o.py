file1=open("C:\\Users\\Hamrah System\\Desktop\\m.txt","r+")
file1.writelines(input("enter strings"))
file1=open("C:\\Users\\Hamrah System\\Desktop\\m.txt","a+")
file1.readline()
b=input("entar char")
c=0
for i in file1:
    if i==b:
        c+=1
        file1.readline() 
print("repeat is",c)        
file1.close()
      
