from pythonforandroid.recipe import CythonRecipe
import os


class groestlcoin_hashRecipe(CythonRecipe):
    version = '1.0.1'
    url = 'https://pypi.python.org/packages/source/g/groestlcoin_hash/groestlcoin_hash-{version}.tar.gz'  # noqa
    depends = ['python3crystax']
    call_hostpython_via_targetpython = True
    cythonize = False


recipe = groestlcoin_hashRecipe()
