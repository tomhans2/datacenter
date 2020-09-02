"""
创建线程工作池
    1. 创建队列，存储任务
    2. 生成线程守护
    3. 每个线程循环阻塞，并处理队列任务
    4. 任务完成后更新队列
    5. 主线程阻塞，直到任务队列完成
"""

import threading
from time import sleep, ctime
from queue import Queue
import os


class ThreadManager(threading.Thread):

    def __init__(self, master_queue, function='default_error', args=''):
        threading.Thread.__init__(self)
        self.master_queue = master_queue
        self.args = args
        self.function = function

    def run(self):
        while True:
            self.function, self.args = self.master_queue.get()
            self.function(*self.args)
            self.master_queue.task_done()

    def default_error(self, *args):
        raise NotImplementedError('Default error, call back function is not implemented, args = %', ''.format(*args))


class ThreadPoolManager(object):
    """
    线程池管理，这个线程池将管理ThreadManager，并调度工作
    """

    def __init__(self, thread_num):
        self.master_queue = Queue()
        self.thread_num = thread_num
        self.init(self.thread_num)

    def init(self, thread_num):
        for i in range(thread_num):
            thread = ThreadManager(self.master_queue)
            thread.start()

    def add_job(self, function='default_error', *args):
        self.master_queue.put((function, *args))


lock = threading.Lock()


# 测试
def loop(nloop, nsec):
    # lock.acquire()
    print('当前线程名称：%s' % threading.current_thread().name)
    print('开始任务：(%s,%s) at %s' % (nloop, nsec, ctime()))
    sleep(nsec)
    print('任务：%s，完成 at %s' % (loop, ctime()))
    # lock.release()


all_functions_TupleParam = [(loop, (1, 4)), (loop, (2, 10)), (loop, (3, 5)), (loop, (4, 4)), (loop, (5, 10)),
                            (loop, (6, 7)), (loop, (7, 6))]


def main():
    print('starting at: %s', ctime())
    thread_pool = ThreadPoolManager(4)
    for each in all_functions_TupleParam:
        func, args = each
        thread_pool.add_job(func, args)
    thread_pool.master_queue.join()
    print('all done at: %s', ctime())
    os._exit(0)


if __name__ == '__main__':
    main()
