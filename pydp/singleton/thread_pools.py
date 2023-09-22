import threading
import time


class ThreadPool:
    _instance = None

    def __new__(cls, max_threads=5):
        if not cls._instance:
            cls._instance = super(ThreadPool, cls).__new__(cls)
            cls._instance._semaphore = threading.Semaphore(max_threads)
            cls._instance._max_threads = max_threads
        return cls._instance

    def execute(self, func, *args):
        self._semaphore.acquire()
        t = threading.Thread(target=self._thread_func, args=(func, args))
        t.start()

    def _thread_func(self, func, args):
        func(*args)
        self._semaphore.release()


def sample_task(name):
    print(f'Task {name} started')
    time.sleep(2)
    print(f'Task {name} completed')


# Usage
pool1 = ThreadPool(2)
pool1.execute(sample_task, 'A')
pool1.execute(sample_task, 'B')

pool2 = ThreadPool(2)
pool2.execute(sample_task, 'C')

# Both pool1 and pool2 refer to the same instance, so they share the same thread limit.
