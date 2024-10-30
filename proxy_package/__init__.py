# 运行时路径。并非__init__.py的路径
import os
import sys
print("路径组:",sys.path)

BASE_DIR = "..\\server-py"
if os.path.exists(BASE_DIR):
    sys.path.append(BASE_DIR)
    print("成功添加路径:", BASE_DIR)
BASE_DIR = "..\\server-py\\src"
if os.path.exists(BASE_DIR):
    sys.path.append(BASE_DIR)
    print("成功添加路径:", BASE_DIR)
    
print("路径:",os.getcwd())
print("路径组:",sys.path)
    
from server_py.src.config.log import console


console.log("...依赖引入完成")