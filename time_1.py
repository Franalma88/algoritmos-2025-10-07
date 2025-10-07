import time
n = float(input("Introduce el número de segundos entre cada cuenta: "))

time_begin=time.time()
for i in range(1, 11):
    print(i)
    time.sleep(n)
end_time=time.time()
print(f"¡Tarda {end_time-time_begin} segundos")
