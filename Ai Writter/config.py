##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
