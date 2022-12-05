import time

for i in range(1, 51):
    print("[" + i * "#" + "]" + str(i * 2) + "%", end="\r")
    time.sleep(0.05)