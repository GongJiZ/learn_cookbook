from threading import Thread, Event
import time


def count_down(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print(f'T{n}')
        n -= 1
        time.sleep(3)


if __name__ == '__main__':
    started_event = Event()

    print('launching countdown')
    t = Thread(target=count_down, args=(10, started_event))
    t.start()

    started_event.wait()
    print('countdown running')
