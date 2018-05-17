from pugsql.parser import PugSQLParser


class TestParser:

    def test_parse(self):
        parser = PugSQLParser()
        with open('characters.sql', 'r') as fd:
            parsed_file = parser.parse(fd)

        assert len(parsed_file) == 5
