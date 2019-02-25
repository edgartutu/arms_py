p=[]
def even_or_odd(a=min,b=max,c=str):
    for i in range (a,b):
        if(c=='even' and  i%2==0):
            p.append(i)
        elif(c=='odd' and i%2!=0):
            p.append(i)    
even_or_odd(2,10,'odd')
print(len(p))

            
        
        
    
        
 
    
