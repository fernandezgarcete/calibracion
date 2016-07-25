__author__ = 'Juanjo'

from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options={"py2exe": {"bundle_files": 1, 'compressed': True, 'includes': ['sip']}},
    windows=[{'script': 'calibrar.py', 'icon_resources': [(1, 'c:/Users/Juanjo/Pictures/CONAE_chico_transp.ico')]}],
    zipfile=None,
    data_files=[('imageformats', ['C:/Python34/Lib/site-packages/PyQt4/plugins/imageformats/qico4.dll'])]
)
