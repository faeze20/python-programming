# python-programming
a=input("enter list numbers")
a2=int(input("enter a number"))
b=a.split(" ")
c=0
l=len(b)
m,w=[],[]
for i in range (l):
    m.append(int(b[i]))
#print(m
for i in range(2,l):
    import itertools
    lst=list(itertools.combinations(m ,i))
    p=len(lst)
o=[]
for j in range(p):
    for s in range(i):
        w.append(lst[s])
        for R in range(i):
            c=int(w(R))+c
    if c==a2:
        print(w(R))    


#for j in range(i+1):
   # c=c+int(k[j])
   # if c==a2:
        #n.append(k[j])
       # c=0
    #print(n)    
                                     
             
    #if a2>int(b[i]):
        #c=int(b[i])+c
        #m.append(int(b[i]))
        #if c==a2:
           # for j in range(i+1):
               # print(b[j])
        #if c<a2:
            #for j in range(i+1):
                #c=c+int(b[j])
        #if c>a2:
           # break       
