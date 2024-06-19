import os

# 导入所需包
from flask_cors import CORS

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    @staticmethod  # 此注释可表明使用类名可以直接调用该方法
    def init_app(app):
        # 执行当前需要的环境的初始化
        CORS(app)


class DevelopmentConfig(Config):
    # 开发环境
    DEBUG = True


class TestingConfig(Config):
    # 测试环境
    # TESTING = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    #                           'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    pass


class ProductionConfig(Config):
    # 生产环境
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #                           'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    pass


config = {'development': DevelopmentConfig, 'testing': TestingConfig, 'production': ProductionConfig,
          'default': DevelopmentConfig}
