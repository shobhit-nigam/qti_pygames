import time
listx = [11, 22, 33, 44]

obji = iter(listx)

while True:
    try:
        varx = next(obji)
        print(varx)
        time.sleep(1)
        # do something with varx
    except StopIteration:
        # if StopIteration is raised, it means that
        # iterator is exhausted
        print("will exit now")
        time.sleep(1)
        break
