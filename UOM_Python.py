print("Hello World!")
name = input("Hello, what's your name? ")
print("Hello " + name)
Integer = 23
Float = 2.3
Complex = 23j
print(f"The type of {Integer} is {type(Integer)}")
print(f"The type of {Float} is {type(Float)}")
print(f"The type of {Complex} is {type(Complex)}")
BooL = False
bOOl = True
print(f"The type of {BooL} is given below: ")
print(type(BooL))
print("The type of {bOOl} is given below: ")
print(type(bOOl))
x = 34
y = x
print("Is x equal to y {x==y}")
print("Is x equal to y", x is y)
print(f"Id of x {id(x)}")
print(f"Id of y {id(y)}")
x = 35
print("Is x equal to y {x==y}")
print("Is x equal to y", x is y)
print(f"Id of x {id(x)}")
print(f"Id of y {id(y)}")
num = input("Enter an integer number: ")
odd_or_even = int(num)
module = odd_or_even % 2
if odd_or_even > 0:
    if module == 0:
        print(f"{odd_or_even} is even")
    else:
        print(f"{odd_or_even} is odd")
else:
    print("Sorry! You cannot input numbers less than zero")
mark = input("Enter your exam marks: ")
marks = int(mark)
if marks > 75:
    print("Your grade is A")
elif 60 <= marks < 75:
    print("Your grade is B")
elif 40 <= marks < 60:
    print("Your grade is C")
else:
    print("Your grade is F")
num = 2 + 3 - 5 * 7 / 11 % 13 ** 17 // 19
print("Number is ", num)
list_1 = [1, 2, 3, 4, 5, 6]
list_2 = ['a', 'e', 'i', 'o', 'u']
list_3 = ['Sithila Sihan', 'Somaratne', 13, 100000.00]
print(list_1)
print(list_2)
print(list_3)
values = [3, 16, 29, 35, 49, 57]
print(values[0])
print(values[4])
print(values[0:3])
print(values[2:5])
print(values)
values.append(66)
print(values)
values[2] = 23
print(values)
values.remove(3)
values.append(76)
print(values)
del values[6]
print(values)
List = ['ph', 'ch', 1997, 2000, 2000, 2009]
List[2] = 2001
List.remove(2000)
List.append(2015)
print(List[2:])
data = [[1, 2, 3, ], [4, 0, 6], [7, 8, 9]]
print(data[1][1])
print(data)
data[1][1] = 5
print(data)
data[1].append(0)
print(data)
data[1].remove(0)
print(data)
data[1].append(0)
print(data)
del data[1][3]
print(data)
print(len([1, 2, 3]))
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(['Hi'] * 4)
print(3 in [1, 2, 3])
print(4 in [1, 2, 3])
for x in [1, 2, 3]:
    print(x)
L = ['a', 'b', 'c']
print(L[2])
print(L[-2])
print(L[1:])
# my-solution
numList = [2, 4, 6, 8, 3, 4, 2, 1]
print(numList)
del numList[4:]
print(numList)
# excepted-solution
numList = [2, 4, 6, 8, 3, 4, 2, 1]
eventList = []
for i in numList:
    if (i % 2 == 0) and (i not in eventList):
        eventList.append(i)
print(eventList)
num = [13, 16, 55, 43, 76]
print(num[1:4])
for counter in [1, 2, 3, 4, 5]:
    print("This is a loop: counter = ", counter)
print(list(range(10)))
print(list(range(5, 10)))
print(list(range(0, 10, 3)))
print(list(range(-10, -100, -30)))
for i in range(50):
    print("Sithila is cool!")
total = 0
for counter in range(0, 101, 2):
    total = total + counter
print("total = ", total)
a = 0
for i in range(2, 4):
    a = a + i
print(a)
num = int(input("Input a number to repeat: "))
while num != 0:
    print("Hello World!")
    num = num - 1
print("End!")
for x in range(0, 5):
    for y in range(0, 10):
        print("$", end="")
    print("")
num1 = 2
while num1 > 0:
    num2 = 2
    while num2 > 0:
        print("Sri Lanka")
        num2 = num2 - 1
    num1 = num1 - 1
n = 10
for i in range(0, n):
    print(i, "Hello")
    if i == 3:
        print("Count Aborted")
        break
    print(i, "World")
print("End of program")
tot = 0
for num in range(5):
    if num == 3:
        break
    tot = tot + num
print(tot)
for i in range(-2, 3):
    if i == 0:
        continue
    print("5 divided by ", i, " is: ", (5.0 / i))
print("End")
tot = 0
for num in range(5):
    if num >= 3:
        continue
    tot = tot + num
print(tot)
fruits = ["Apple", "orange", "Grapes", "Banana"]
for fruit in fruits:
    pass
print("Done")
tot = 1
for num in range(5):
    pass
print(tot)
numbers = [3, 2, 5, 8, 2, 9]
for number in numbers:
    print("Looking at: ", number)
    if number == 5:
        print("FOUND number!")
        break
else:
    print("Number NOT FOUND")
print("End!")
for number in numbers:
    print("Looking at: ", number)
    if number == 6:
        print("FOUND number!")
        break
else:
    print("Number NOT FOUND")
print("End!")
numbers = [3, 2, 5, 7, 8]
count = 0
for number in numbers:
    count += 1
    if number == 1:
        break
else:
    count = -1
print(count)
count = 0
for number in numbers:
    count += 1
    if number == 5:
        break
else:
    count = -1
print(count)
val = int(input())
for x in range(0, val):
    for y in range(0, val):
        print('*', end='')
    print('')
i = int(input())
j = 2
if i > 1:
    while j <= (i / j):
        if not (i % j):
            print("not a prime")
            break
        j = j + 1
    if j > i / j:
        print("prime")
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep="-")
print(1, 2, 3, 4, sep="_", end="!?")
print('')
print("Sri Lanka is an island in Asia, it was an ex-colony of the British Empire until {}".format(1948))
print(
    "Here are the numbers from 0 to 9 which are ordered randomly: {4}, {1}, {0}, {3}, {2}, {8}, {9}, {7}, {6}, {5},".format(
        3, 7, 9, 2, 1, 0, 4, 6, 5, 8))


def greet(name):
    """Greet a person with name"""
    print("Hello ", name)
    return


name = input("Enter your name: ")
greet(name)


# --Exercise
def circumference(radius):
    Pi = 3.14
    return 2 * Pi * radius


def area(radius):
    Pi = 3.14
    return Pi * radius * radius


r = input("Input the radius of the circle: ")
radius = int(r)
print("Circumference of the circle is ", circumference(radius))
print("Area of the circle is ", area(radius))


def sqr(n):
    x = n ** 2
    return x


try:
    number = input("")
    n = int(n)
    print(sqr(n))
except EOFError:
    ""
num_input = input("Input a number: ")
try:
    num_value = int(num_input)
    print(num_value)
except:
    num_value = -1
    if num_value > 0:
        print("A negative number was entered")
    else:
        print("You can only enter numbers!")
fhandle1 = open("myfile.txt")
fcontents = fhandle1.read()
print(fcontents)
fhandle1.close()
fhandle2 = open("myfile.txt", "w")
mystring = "I'm learning IT with iCET, UoM, Udemy, W3School, Google Sites and YouTube."
fhandle2.write(mystring)
fhandle2.close()

