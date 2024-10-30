from pc_config.pyvebview_config import window

# 窗口事件
def on_closed():
    print('pywebview window is closed')

window.events.closed += on_closed