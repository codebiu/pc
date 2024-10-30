# 全局路由 map
routes = {}

# 路由装饰器
def route(path: str):
    def decorator(func):
        routes[path] = func
        return func
    return decorator

class Api:
    # 模拟请求处理
    def handle_request(self,params, **kwargs):
        path = params['path']
        data = params['data']
        if path in routes:
            return routes[path](data)
        else:
            return "404 Not Found"