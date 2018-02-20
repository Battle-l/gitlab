# -*- mode: python -*-

block_cipher = None


a = Analysis(['0005.py'],
             pathex=['D:\\PyCharm\\gitlab\\practice\\0005'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='0005',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
