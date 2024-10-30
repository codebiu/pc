# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src\\pc_main.py','../server_py/src/server_main.py'],
    pathex=[],
    binaries=[],
    datas=[('../server_py/source', 'source'),('pc_source','pc_source')],
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
    name='code_tm_pc_py',
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
    icon=['pc_source\\img\\ion\\pc_favicon64.ico'],
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
