"""webview初始化"""

# self
from pc_util.port_ex import port_no_used

# pc_api
from pc_util.routes import Api

# lib
import webview

#  pc路由
api = Api()
window = webview.create_window(
    "pc",
    f"http://localhost:{port_no_used}",
    js_api=api,
    # 无框
    # frameless=True,
    # 创建透明窗口。在 Windows 上不受支持。
    # transparent=True,
)

print("...pc服务配置完成")
