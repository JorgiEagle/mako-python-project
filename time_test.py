from tracemalloc import start
import Skeleton
import main
import time

def time_it(function):
    times = []
    for x in range(100):
        start_time = time.time_ns()
        function()
        end_time = time.time_ns()
        total = end_time - start_time
        times.append(total/1000000000)

    print(f"Function: {str(function)} Min: {min(times)}, Max: {max(times)}, Average: {sum(times)/len(times):.2f},'\
        ' Total: {sum(times)}")

if __name__ == '__main__':
    time_it(Skeleton.main)
    time_it(main.main)