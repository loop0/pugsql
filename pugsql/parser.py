# pylint: disable=missing-docstring

import re
import sqlparse

name_token = re.compile(
    r'^--\s+:name\s+(?P<name>[-\w]+)\s+(?P<command>:(!|\?|<!|i!))?\s+(?P<result>:(1|\*|n))?',
    re.MULTILINE
)


class PugSQLParser:

    def parse(self, fd):
        text = fd.read()
        statements = []
        for statement in sqlparse.split(text):
            match = name_token.search(statement)
            sql = ' '.join(sqlparse.format(statement, strip_comments=True).split())

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
