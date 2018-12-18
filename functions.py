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

def spam():
    eggs = 54
    bacon()
    print(eggs)

def bacon():
    ham = 292
    eggs = 0

spam()

#Global variables can be read from local scope

def spam():
    print(eggs)

eggs = 54

spam()

print(eggs)





















