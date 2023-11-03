import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger('demologger')
        logger.setLevel(logging.INFO)
        filehandler=logging.FileHandler(filename="E:\\hybrid framework project\\logs\\automate.log",mode='a')
        formatter=logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s',
                            datefmt='%d/%m/%Y %I:%M:%S %p')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        print()

        return logger

