import configparser

config=configparser.RawConfigParser()

config.read("E:\\hybrid framework project\\configurations\\config.ini") # read config.ini file

class ReadConfig:
    @staticmethod       # can be access this method directly by class name
    def getApplicationURL():
        url=config.get('common info','baseurl')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password
