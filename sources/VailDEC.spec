# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['VailDEC.py'],
             pathex=['C:\\Users\\t_koga\\Desktop\\VailDEC3-sources\\sources'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          Tree('resources',prefix='resources'), #<-
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='VailDEC',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='IMG_8776.ICO')
