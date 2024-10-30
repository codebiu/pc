import webview
from Routes import route,Api
@route("/home")
def home(name: str):
    return f"Hello, {name}!"

if __name__ == '__main__':
    api = Api()
    # Create a resizable webview window with minimum size constraints
    window = webview.create_window('pywebview中html和python交互的例子', 'index.html', js_api=api)
    webview.start()
    # ssl=True