import time
from threading import Thread


def countdown(n):
    while n > 0:
        print(f'T{n}')
        n -= 1
        # time.sleep(1)


if __name__ == '__main__':
    t = Thread(target=countdown, args=(999999999, ), daemon=True)
    t.start()
    m = 999999999
    while m > 0:
        # time.sleep(3)
        if t.is_alive():
            print('still running')
        else:
            print('completed')
        print(f'L{m}')
        m -= 1
