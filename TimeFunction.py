import time
start=time.time()
input('wait for 5 secs and press enter')
end=time.time()
print (f"u took {end-start} secs")
time.sleep(3)
print(f"time {time.ctime()}")   #for current time

text = "Typing simulation in Python..."
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.1)
