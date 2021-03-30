from multi_process.processing import yinhun_multi


def run():
    try:
        yinhun_multi().run()
    except:
        raise IndexError('运行错误')


if __name__ == '__main__':
    run()