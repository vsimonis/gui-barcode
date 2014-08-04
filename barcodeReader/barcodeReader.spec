# -*- mode: python -*-
a = Analysis(['barcodeReader.py'],
             pathex=['C:\\Users\\Valerie\\Source\\Repos\\gui-barcode\\barcodeReader\\barcodeReader'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          Tree('data',prefix='data'),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='barcodeReader.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
