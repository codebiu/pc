# pc_api
from pc_util.routes import route
@route("/home")
def home(name: str):
    print(f"Hello, {name}!")
    return f"Hello, {name}!"
print('pc 配置 route')