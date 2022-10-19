import time
class Sample():
    def __init__(self):
        print("init method")

    def __enter__(self):
        print("enter method")
        return ""

    def __exit__(self, x, y, z):
        print("exit method")


with Sample() as obja:
    print("within the 'with' block")
    time.sleep(5)

print("outside the with block")
