
block_cipher = None


a = Analysis(['BufferCalculator.py'],
             pathex=['C:\\Users\\cmedders\\buffcalc\\'],
             binaries=[],
             datas=[("Buffers.db", ".")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='BufferCalculator',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True, icon="iso255.ico" )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='BufferCalculator')