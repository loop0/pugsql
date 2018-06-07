# pylint: disable=missing-docstring

import re
import sqlparse

name_token = re.compile(
    r'^--\s+:name\s+(?P<name>[-\w]+)\s+(?P<command>:(!|\?|<!|i!))?\s+(?P<result>:(1|\*|n))?',
    re.MULTILINE
)
params_token = re.compile(r':([*:\w]+)')


class PugSQLParser:

    def parse(self, fd):
        text = fd.read().rstrip('\n')
        statements = []
        for statement in sqlparse.split(text):
            match = name_token.search(statement)
            sql = ' '.join(sqlparse.format(statement, strip_comments=True).split())
            sql = params_token.sub(r'%(\1)s', sql)

            name = match.group('name')
            command = match.group('command')
            result = match.group('result')

            if name:
                statements.append({
                    'name': name.replace('-', '_'),
                    'command': command,
                    'result': result,
                    'sql': sql
                })

        return statements
