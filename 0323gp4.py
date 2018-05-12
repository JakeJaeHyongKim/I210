def fibonacci(num):
    for i in range(num):
        if num is (0,1):
            return 1
        else:
            return fibonacci(num-1)+fibonacci(num-2)
print(fibonacci(5))
