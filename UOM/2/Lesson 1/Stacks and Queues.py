#This is UOM Python 2 
#Lesson 1.1: Stacks and Queues

############# Stacks #############

def push(stack, value):
    stack.append(value)

def pop(stack):
    stack.pop()

central_powers_WW1 = []
push(central_powers_WW1, "2nd Reich (Germany)")
push(central_powers_WW1, "Austria-Hungary")
push(central_powers_WW1, "Ottoman Empire")
push(central_powers_WW1, "Bulgaria")
push(central_powers_WW1, "Italy")

print(central_powers_WW1)

pop(central_powers_WW1)

print(central_powers_WW1)

############# Queues #############

def enqueue(queue, value):
    queue.append(value)

def dequeue(queue):
    queue.pop(0)
    
numbers = []
enqueue(numbers, 0)
enqueue(numbers, 1)
enqueue(numbers, 2)
enqueue(numbers, 3)
enqueue(numbers, 4)
enqueue(numbers, 5)
enqueue(numbers, 6)
enqueue(numbers, 7)
enqueue(numbers, 8)
enqueue(numbers, 9)

print(numbers)

dequeue(numbers)

print(numbers)







