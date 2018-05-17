# pylint: disable=missing-docstring

import os
import sys
import jinja2

from pugsql.engine import PugSQLModuleFinder
from pugsql.parser import PugSQLParser

modules = {}
sys.meta_path.append(PugSQLModuleFinder(modules))
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(os.path.abspath(__file__)))
)
module_template = jinja_env.get_template('module.tpl')


def def_db_fns(file_path):
    if not os.path.isfile(file_path):
        return

    file_name, extension = os.path.splitext(os.path.basename(file_path))
    with open(file_path, 'r') as fd:
        parser = PugSQLParser()
        statements = parser.parse(fd)
        modules[file_name] = module_template.render({'statements': statements})
