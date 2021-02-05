import timeit
from functools import lru_cache

class CustomException(Exception):
    def __init__(self,a=""):
        message = a
        super().__init__(message)

@lru_cache()
def fib_rec(n: int) -> int:
    """Fibonacci - Recursive."""
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)
@lru_cache()
def fib_iter(n: int) -> int:
    """Fibonacci - Iterative."""
    first_number, second_number = 0, 1
    for i in range(0, n):
        first_number, second_number = second_number, first_number + second_number

    return first_number

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #n=int(input("Zadej n pro výpočet Fibonacciho: "))
    for n in range (0,50):
        if n<0:
            raise CustomException("N musí být >=0!")
        else:
            start_time = timeit.timeit()
            fibo_n=[]
            for my_counter in range(n+1):
                if my_counter<2:
                    fibo_n.append(my_counter)
                else:
                    temp=fibo_n[my_counter-1]+fibo_n[my_counter-2]
                    fibo_n.append(temp)

            end_time = timeit.timeit()

            fibo_n1=fib_iter(n)
            print(39*"-")
            print(n)
            print("Fibonacci iterací: ",fibo_n1)

            fibo_n2=fib_rec(n)
            end_time = timeit.timeit()
            print("Fibonacci rekurzí: ",fibo_n2)