import multiprocessing
from multiprocessing import Pool, Process
import os, time, sys
import psutil

"""

"""
import multiprocessing
from multiprocessing import Pool, Process
import os, time, sys
import psutil


class ProcessPoolManager(object):

    def __init__(self, cpus=None):
        self.pool = Pool(processes=cpus)
        self.task = {}
        self.cmds = []
        self.process_info = []

    def __len__(self):
        return len(self.task)

    def callback(self,text):
        print('函数执行完毕：%',text)

    def init_process_pool(self):
        pass

    @property
    def process(self):
        pass

    def assign(self):
        pass

    def apply_async(self):
        pass

    def join(self):
        pass


def main():
    pass


if __name__ == '__main__':
    main()
