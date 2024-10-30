# 把当前文件所在文件夹的父文件夹路径下main所在src加入到PYTHONPATH
import sys
import os
# 配置路径
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..",".."))
sys.path.append(os.path.join(parent_path,'server_py','src'))
from pc_util.port_ex import port_no_used
from server_main import *
from server_main import app,console,path # 导入
from pc_config.pyvebview_config import window # 窗口
from pc_controller import index,window_index
import uvicorn,threading
print(parent_path)

'''server'''
# 启动FastAPI服务 daemon守护线程,整个python程序退出时自动卸载
threading.Thread(target=uvicorn.run, args=(app,), 
                 kwargs={"host":"localhost","port": port_no_used},daemon=True).start()

'''pc'''
import webview
webview.start(
    # 指定edgechromium 或 chrome
    # gui='edgechromium'
    )

# 启动
if __name__ == "__main__":
    # 验证引入成功 关闭执行
    print('pc_py get server_py',path.path_html,__name__)
 


