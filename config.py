from distutils.debug import DEBUG

class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'jerimy'
    MYSQL_PASSWORD = '12345'
    MYSQL_DB = 'UtecBet'


config = {
    'development': DevelopmentConfig
}