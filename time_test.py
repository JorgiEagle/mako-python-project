from tracemalloc import start
import OOP_Solution
import Functional_Solution
import time

def time_it(functions):
    times = []
    for x in range(100):
        start_time = time.time_ns()
        function()
        end_time = time.time_ns()
        total = end_time - start_time
        times.append(total/1000000000)

    print(f'Function: {function.__name__} Min: {min(times)}, Max: {max(times)}, Average: {sum(times)/len(times):.2f},'\
        f' Total: {sum(times)}')

if __name__ == '__main__':
    time_it([OOP_Solution.main, Functional_Solution.main])