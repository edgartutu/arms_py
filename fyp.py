##<<<<<<< HEAD
##p=[]
##def even_or_odd(a=min,b=max,c=str):
##    for i in range (a,b+1):
##        if(c=='even' and  i%2==0):
##            p.append(i)
##        elif(c=='odd' and i%2!=0):
##            p.append(i)    
##even_or_odd(2,10,'even')
##print(len(p))
##
##p=[]
##def odd_even(a,b,category=str):
##    for i in range (a-1,b):
##        i=i+1
##        if (category=='even' and i%2==0):
##            p.append(i)
##
##        elif(category == 'odd' and i%2!=0):
##            p.append(i)
##        
##odd_even(2,10,'even')
##print(len(p))
''''
def new_even_or_odd(minimum, maximum, category):
    if category == 'even':
        return len([number for number in range(minimum, maximum + 1) if number % 2 == 0])
    elif category == 'odd':
        return len([number for number in range(minimum, maximum + 1) if number % 2 == 0])
    return None

new_even_or_odd(2, 10, 'even')
'''


def even_or_odd(minimum, maximum, category):
    even_counter = 0
    odd_counter  = 0
    for number in range(minimum, maximum + 1):
        if category == 'even' and number % 2 == 0 : even_counter +=1
        elif category == 'odd' and number % 2 != 0 : odd_counter +=1
    print ('The number of odd numbers is', odd_counter)
    print ('The number of even numbers is', even_counter)

even_or_odd(2, 10, 'odd')


def odd_even(minimum,maximum,category = None):
    even_counter = 0
    odd_counter = 0
    for number in range(minimum, maximum + 1):
        even_counter +=1 if number % 2 == 0  else 0
        odd_counter +=1 if number % 2 != 0  else 0
    print('The number of even numbers is', even_counter)
    print('The number of odd numbers is', odd_counter)
    
odd_even(2,10,'even')




