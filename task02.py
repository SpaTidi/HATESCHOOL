"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence

def check_fibonacci(data: Sequence[int]) -> bool:
        if len(data) == 1:
                return data[0] == 0 
    
        if len(data) == 2:
                return data[0] == 0 and data[1] == 1
        
        if data[0] != 0 or data[1] != 1:
                return False
    
        for i in range(2, len(data)):
            if data[i] != data[i - 1] + data[i - 2]:
                    return False
    
        return True

if __name__ == '__main__':
        print(check_fibonacci([0, 1, 1]))
        print(check_fibonacci([1, 1, 2]))
        print(check_fibonacci([0]))
        print(check_fibonacci([0, 1]))