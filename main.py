print("Hello World")
if 5 > 2:
    print("Five is greater than two")
# This is a comment
"""
This is a comment
written in 
more than just one line
"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Apple"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()


def myfunc():
    X = "fantastic"
    print("Python is " + X)


myfunc()

print("Python is " + x)


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)

x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)

x = "Hello World"

print(x)

print(type(x))

x = 20

print(x)

print(type(x))

x = 20.5

print(x)

print(type(x))

x = 20.50

print(x)

print(type(x))

x = 1j

print(x)

print(type(x))

x = ["apple", "banana", "cherry"]

x = ("apple", "banana", "cherry")

print(x)

print(type(x))

x = range(6)

print(x)

print(type(x))

x = {"name": "John", "age": 36}

print(x)

print(type(x))

x = {"apple", "banana", "cherry"}

print(x)

print(type(x))

x = frozenset({"apple", "banana", "cherry"})

print(x)

print(type(x))

x = True

print(x)

print(type(x))

x = b"Hello"

print(x)

print(type(x))

x = bytearray(5)

print(x)

print(type(x))

x = memoryview(bytes(5))

print(x)

print(type(x))

x = None

print(x)

print(type(x))

a = 1
b = 2.8
c = 1j

print(type(a))
print(type(b))
print(type(c))

d = 1
e = 12E4
f = -5j

print(type(d))
print(type(e))
print(type(f))

g = float(d)

# convert from float to int:
h = int(e)

# convert from int to complex:
i = complex(f)

print(g)
print(h)
print(i)

print(type(g))
print(type(h))
print(type(i))

import random

print(random.randrange(4, 11))
j = int(1)
k = float(4.2)
l = str(2)
m = "Hello"
print(m)
n = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(n)

o = "Hello, World!"
print(o[0])
print(o[2:5])

for x in "banana":
    print(x)

p = "Hello, World!"
print(len(p))

txt = "The best things in life are free!"
print("free" in txt)
if "free" in txt:
    print("Yes, 'free' is present.")
print("expensive" not in txt)
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

q = " Hello, World! "
print(q[2:5])
print(q[:5])
print(q[2:])
print(q[-5:-2])
print(q.upper())
print(q.lower())
print(q.strip())
print(q.replace("H", "J"))
print(q.split(", "))

r = "Pine"
s = "apple"
t = r + s
print(t)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantità = 3
cosa = 567
prezzo = 49.95
ordine = "I want to pay {2} dollars for {0} pieces of item {1}."
print(ordine.format(quantità, cosa, prezzo))

text = "We are the so-called \"Vikings\" from the north."
print(text)
text = "We are the so-called \'Vikings\' from the north."
print(text)
text = "We are the so-called \\Vikings\\ from the north."
print(text)
text = "We are the so-called \nVikings from the north."
print(text)
text = "We are \rthe so-called Vikings from the north."
print(text)
text = "We are \tthe so-called Vikings from the north."
print(text)
text = "We are  \bthe so-called Vikings from the north."
print(text)
text = "We are \fthe so-called Vikings from the north."
print(text)
text = "\110\145\154\154\157"
print(txt)
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

var = ("\n"
       "capitalize()	Converts the first character to upper case\n"
       "casefold()	Converts string into lower case\n"
       "center()	Returns a centered string\n"
       "count()	Returns the number of times a specified value occurs in a string\n"
       "encode()	Returns an encoded version of the string\n"
       "endswith()	Returns true if the string ends with the specified value\n"
       "expandtabs()	Sets the tab size of the string\n"
       "find()	Searches the string for a specified value and returns the position of where it was found\n"
       "format()	Formats specified values in a string\n"
       "format_map()	Formats specified values in a string\n"
       "index()	Searches the string for a specified value and returns the position of where it was found\n"
       "isalnum()	Returns True if all characters in the string are alphanumeric\n"
       "isalpha()	Returns True if all characters in the string are in the alphabet\n"
       "isdecimal()	Returns True if all characters in the string are decimals\n"
       "isdigit()	Returns True if all characters in the string are digits\n"
       "isidentifier()	Returns True if the string is an identifier\n"
       "islower()	Returns True if all characters in the string are lower case\n"
       "isnumeric()	Returns True if all characters in the string are numeric\n"
       "isprintable()	Returns True if all characters in the string are printable\n"
       "isspace()	Returns True if all characters in the string are whitespaces\n"
       "istitle()	Returns True if the string follows the rules of a title\n"
       "isupper()	Returns True if all characters in the string are upper case\n"
       "join()	Joins the elements of an iterable to the end of the string\n"
       "ljust()	Returns a left justified version of the string\n"
       "lower()	Converts a string into lower case\n"
       "lstrip()	Returns a left trim version of the string\n"
       "maketrans()	Returns a translation table to be used in translations\n"
       "partition()	Returns a tuple where the string is parted into three parts\n"
       "replace()	Returns a string where a specified value is replaced with a specified value\n"
       "rfind()	Searches the string for a specified value and returns the last position of where it was found\n"
       "rindex()	Searches the string for a specified value and returns the last position of where it was found\n"
       "rjust()	Returns a right justified version of the string\n"
       "rpartition()	Returns a tuple where the string is parted into three parts\n"
       "rsplit()	Splits the string at the specified separator, and returns a list\n"
       "rstrip()	Returns a right trim version of the string\n"
       "split()	Splits the string at the specified separator, and returns a list\n"
       "splitlines()	Splits the string at line breaks and returns a list\n"
       "startswith()	Returns true if the string starts with the specified value\n"
       "strip()	Returns a trimmed version of the string\n"
       "swapcase()	Swaps cases, lower case becomes upper case and vice versa\n"
       "title()	Converts the first character of each word to upper case\n"
       "translate()	Returns a translated string\n"
       "upper()	Converts a string into upper case\n"
       "zfill()	Fills the string with a specified number of 0 values at the beginning\n"
       "\n")
print(10 > 9)
print(10 == 9)
print(10 < 9)

number = 200
numb = 33

if number > numb:
    print("number is greater than numb")
else:
    print("numb is not greater than number")

print(bool("Hello"))
print(bool(15))

w = "Hello"
y = 15

print(bool(x))
print(bool(y))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


class myclass:
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))


def myFunction():
    return True


print(myFunction())


def miaFunzione():
    return True


if miaFunzione():
    print("YES!")
else:
    print("NO!")

x = 200.00
print(isinstance(x, int))

print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 % 5)
print(10 ** 5)
print(10 // 5)
"""
ASSIGNMENTS OPERATORS

=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3

"""
x = 50
y = 60
bool = x == y
print(bool)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

lista = ["abc", 34, True, 40, "male"]

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

questaLista = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(questaLista)

print(thislist[1])

print(thislist[-1])

frutta = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(frutta[2:5])
print(frutta[:4])
print(frutta[2:])
print(frutta[-4:-1])

if "apple" in frutta:
    print("Yes, 'apple' is in the fruits list")

thislist[1] = "blackcurrant"
print(thislist)

frutta[1:3] = ["blackcurrant", "watermelon"]
print(frutta)

thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist[1:3] = ["watermelon"]
print(thislist)

thislist.insert(1, "banana")
print(thislist)

thislist.append("grapes")
print(thislist)

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thislist.remove("banana")
print(thislist)

thislist.insert(1, "banana")

thislist.pop(1)
print(thislist)

thislist.pop()
print(thislist)

del thislist[0]
print(thislist)

thislist.clear()
print(thislist)

thisList = ("apple", "banana", "cherry", "watermelon", "blackcurrant", "mango", "pineapple", "papaya", "kiwi", "orange")
for x in thisList:
    print(x)

for i in range(len(thisList)):
    print(thisList[i])

i = 0
while i < len(thisList):
    print(thisList[i])
    i = i + 1

[print(x) for x in thisList]
