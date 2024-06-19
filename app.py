import os

from flask import Flask

from blueprints.api import api_bp
from config import config

config_name = os.getenv('FLASK_CONFIG') or 'default'
app = Flask(__name__)
app.register_blueprint(api_bp)

app.config.from_object(config[config_name])  # 可以直接把对象里面的配置数据转换到app.config里面
config[config_name].init_app(app)

# 路由和其他处理程序定义
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # app.run(debug=True)
