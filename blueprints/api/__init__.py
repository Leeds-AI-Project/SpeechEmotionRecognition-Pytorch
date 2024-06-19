# @FileName: __init__.py

from flask import Blueprint

# 从Flask导入Blueprint类，实例化这个类就获得了我们的蓝本对象。
api_bp = Blueprint("api", __name__, url_prefix="/api/")

# 构造方法中的第一个参数是蓝本的名称；第二个参数是包或模块的名称，我们可以使用__name__变量


# 导入需要使用蓝图的视图文件，在下面导入解决循环导入报错
from ..api import data
