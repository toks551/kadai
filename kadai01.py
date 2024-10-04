
def fizz_buzz():
    n = int(input("最大値: "))
    for num in range(1, n + 1):
        if num % 15 == 0:
            print("Fizz Buzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizz_buzz()

