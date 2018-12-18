#Chapter 3
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

#Local and global variables with the same name
#The global statement
def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'

spam()

print(eggs)

def spam():
    global eggs
    eggs = 'spam'

def bacon():
    eggs = 'bacon'

def ham():
    print(eggs)

eggs = 45

spam()

print(eggs)

#Exception handling

def spam(divideBy):
    return 43 / divideBy

print(spam(2))
print(spam(34))
#print(spam(0)) #cause an error
print(spam(1))

def spam(divideBy):
    try:
        return 43 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(34))
print(spam(0))
print(spam(1))

#Practice projects
#The collatz sequence

def collatz(number):
    if number % 2 == 0:
      return print(number // 2)
      
    else:
        return print(3 * number + 1)


number = int(input('Enter the number: '))

collatz(number)
    















