## server

## 开发备注

### conda 环境

```sh
conda env list
# 添加源
conda config --append channels conda-forge

# 初始环境
conda create -n pc_py python=3.10 

# 进入环境
conda activate pc_py
```

### lib

```sh
# pc框架
conda install pywebview
# 数据库对象和程序对象序列化反序列化关联    SQLModel 基于 Pydantic(自动安装) 和 SQLAlchemy(自动安装)
conda install sqlmodel
# 异步sqlite aiofiles
conda install aiosqlite aiofiles
# full server
conda install  sqlmodel aiosqlite aiofiles

pip install pywebview
# 导出
conda env export > environment.yaml
```

### 设置 launch.json debug

```sh
# 进入环境
conda activate pc_py
# 查看python 路径 
which python # linux
where.exe python # windows
```
路径放在.vscode/launch.json下python

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: FastAPI",
            "type": "python",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "src.main:app", "--reload","--port", "1667"
            ],
            "python":"/opt/conda/envs/pc_py/bin/python",
            "jinja": true,
            "justMyCode": true,
            "env": {"PYTHONPATH": "${workspaceRoot}/src"}
        }
    ]
}
```

### 调试

vscode debug
或
npm activate_env


## 打包配置

```sh
pyinstaller options src/pc_main.py
```

pc_main.spec
```js
# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src\\pc_main.py','../server_py/src/server_main.py'],
    pathex=[],
    binaries=[],
    datas=[('source', 'source')],
    hiddenimports=['aiosqlite'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='pc_main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['source\\img\\ion\\favicon.ico'],
    contents_directory='.',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='code_tm_pc_py',
)

```
主要路径:  ,'../server_py/src/server_main.py'


## 参考
<!-- https://blog.csdn.net/weixin_43958375/article/details/130026226 -->