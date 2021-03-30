from airtest.core.android.adb import ADB
from airtest.core.api import *
from airtest.report.report import simple_report
import logging


class utils_tools(object):

    def adb_devices(self):
        """
        获取手机设备号
        :return:
        """
        adb = ADB()
        if not adb.devices():
            raise IndexError('not devices found')
        return adb.devices()

    def adb_serial(self):
        """
        筛选出手机序列号
        :return:
        """
        serial = utils_tools().adb_devices()
        list = [i[0] for i in serial]
        return list

    def adb_connect(self, serial, path):
        """
        链接手机，并设定日志地址
        :return:
        """
        devices = utils_tools().adb_serial()
        if not devices:
            raise IndexError('no devices can connect')
        auto_setup(__file__, logdir=path, devices=[f'Android://127.0.0.1:5037/{serial}'])
        return

    def adb_report(self, path):
        """
        自动生成报告
        :param path:
        :return:
        """
        simple_report(__file__, logpath=f'{path}', logfile=f'{path}/log.txt', output=f'{path}/log.html')
        return

    def adb_logger(self):
        """
        执行日志只显示错误内容
        :return:
        """
        logger = logging.getLogger('airtest')
        logger.setLevel(logging.ERROR)

    def adb_start(self):
        """
        设定启动的app
        :return:
        """
        stop_app('com.road7.phoenix')
        start_app('com.road7.phoenix')


