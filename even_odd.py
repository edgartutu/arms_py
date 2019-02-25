# p=[]
# def even_or_odd(a=min,b=max,c=str):
#     for i in range (a,b+1):
#         if(c=='even' and  i%2==0):
#             p.append(i)
#         elif(c=='odd' and i%2!=0):
#             p.append(i)    
# even_or_odd(-3,10,'even')
# print(len(p))


p=[]
def odd_even(a,b,category=str):
    for i in range (a-1,b):
        i=i+1
        if (category=='even' and i%2==0):
            p.append(i)

        elif(category == 'odd' and i%2!=0):
            p.append(i)
        
odd_even(-4,10,'even')
print(len(p))

##new function for odd and even counters
def odd_even(a,b,category=None):
    even_counter=0
    odd_counter=0
    for x in range(a,b+1):
        even_counter +=1 if x%2==0  else 0
        odd_counter+=1 if x%2!=0  else 0
    print(even_counter)
    print(odd_counter)
odd_even(2,10,'even')
