num = input("Input a number : ")
number = int(num)
odd_or_even = number % 2
if odd_or_even == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

