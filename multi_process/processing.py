from multiprocessing import Pool
from utils.common_utils import utils_tools
from script.yinhun_1 import scripe_yinhun_1
from airtest.core.api import *
import os
import time


class yinhun_multi():

    def program(self, serial):
        path = f'D://log/log{int(time.time())}'
        try:
            # utils_tools().adb_logger()
            utils_tools().adb_connect(serial, path)
            utils_tools().adb_start()
            sleep(10)
            scripe_yinhun_1()
        finally:
            utils_tools().adb_report(path)

    def run(self):
        po = Pool(3)
        list = utils_tools().adb_serial()
        for serial in list:
            po.apply_async(self.program, (serial,))
            sleep(2)
        po.close()
        po.join()


if __name__ == '__main__':

    yindun_multi().run()






