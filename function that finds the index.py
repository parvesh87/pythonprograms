def search(a,b):
    if b in a:
        return a.index(b)
       
    else:
        return (-1)


print(search([1,5,3],5))
print(search([9,8,3],3))
print(search([1,2,3],4))
