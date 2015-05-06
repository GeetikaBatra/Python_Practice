print "Enter the number upto which prime is to be found"
num=raw_input()
for i in range(2, 100): 
    status=True
    for j in range(2,i-1):
        if(i%j==0):
            status=False
    if(status):
        print i    
   
