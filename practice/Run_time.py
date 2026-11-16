# Run time calculation of a python program.
import time as t

begin = (t.time())

count = 0
for i in range(1000):
    for j in range(10):
        count += 1
end = (t.time())
run_time = round((end - begin),10)

print("Run Time of the program:",run_time)