# pylint: disable=missing-docstring

from importlib.abc import MetaPathFinder, Loader
from importlib.machinery import ModuleSpec


class PugSQLModuleFinder(MetaPathFinder):

    def __init__(self, modules):
        self._modules = modules

    def find_spec(self, fullname, path, target=None):
        if not fullname.startswith('pugsql'):
            return None

        module_name = fullname[7:]
        if module_name not in self._modules.keys():
            from pugsql import def_db_fns
            def_db_fns('{}.sql'.format(module_name))

        return ModuleSpec(module_name, PugSQLModuleLoader(self._modules))


class PugSQLModuleLoader(Loader):

    def __init__(self, modules):
        self._modules = modules

    def exec_module(self, module):
        module_code = self._modules[module.__name__]
        module_globals = module.__dict__
        exec(module_code, module_globals)
