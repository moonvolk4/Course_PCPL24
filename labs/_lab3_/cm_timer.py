from time import time, sleep
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.start_time = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'time: {time() - self.start_time}')


@contextmanager
def cm_timer_2():
    start_time = time()
    yield
    print(f'time: {time() - start_time}')


if __name__ == '__main__':
    with cm_timer_1():
        sleep(5.5)

    print('*' * 40)

    with cm_timer_2():
        sleep(5.5)
