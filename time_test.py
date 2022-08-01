from tracemalloc import start
import OOP_Solution
import Functional_Solution
import time

def time_it(functions):
    function_times = ["OOP", "Functional"]
    for function in functions:
        times = []
        for x in range(100):
            start_time = time.time_ns()
            function()
            end_time = time.time_ns()
            total = end_time - start_time
            times.append(total/1000000000)
        function_times.append(times)
    index = 0
    for entry in function_times[2:]:
        print(f'Function: {function_times[index]} Min: {min(entry)}, Max: {max(entry)}, Average: {sum(entry)/len(entry):.2f},'\
            f' Total: {sum(entry)}')
        index += 1

if __name__ == '__main__':

    time_it([OOP_Solution.main, Functional_Solution.main])