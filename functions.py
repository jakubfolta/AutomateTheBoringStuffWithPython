#Keyword arguments and print
print('Hello')
print('World')

print('Hello', end = '')
print('World')

print('cats', 'dogs', 'mice')
print('cats', 'dogs', 'mice', sep = ',')

#Local and global scope
#Local variables cannot be used in the global scope
def spam():
    eggs = 3232

spam()

#print(eggs) #name error


