import time
def deco(func):
    def wrapper():
        startTime = time.time()
        func()
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
    return wrapper
@deco
def func():
    print("hello")
    time.sleep(1)
    print("world")
if __name__ == '__main__':
    f = func
    f()