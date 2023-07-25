##a=[10,15,20,23,44,56]
##b=[]
##for i in a:
##    if i%2==0:
##       b.append(i)
##print(b)


mylist=[10,15,20,23,44,56]
def even(n):
    if(n%2==0):
        return True
    else:
        return False

x=list(filter(even,mylist))
print(x)
        
