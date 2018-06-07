import pytest

from pugsql import def_db_fns


@pytest.fixture
def mocked_db(mocker):
    db = mocker.Mock()
    db.cursor().rowcount = 1
    return db


@pytest.mark.parametrize('function_name, function_args, execute_args, result_function', (
        (
            'all_characters',
            [],
            ['select * from characters order by id;'],
            'fetchall'
        ),
        (
            'character_by_id',
            [{'id': 1}],
            ['select * from characters where id = %(id)s;', {'id': 1}],
            'fetchone'
        ),
        (
            'character_by_name',
            [{'name': 'Oompa Loompa'}],
            ['select * from characters where upper(name) = upper(%(name)s);', {'name': 'Oompa Loompa'}],
            'fetchone'
        ),

    )
)
def test_def_db_fns(mocked_db, function_name, function_args, execute_args, result_function):
    def_db_fns('characters.sql')
    from pugsql import characters

    assert hasattr(characters, function_name)

    getattr(characters, function_name)(mocked_db, *function_args)
    cursor = mocked_db.cursor
    cursor.assert_called()
    cursor().execute.assert_called_once_with(*execute_args)
    getattr(cursor(), result_function).assert_called()


def test_insert_character(mocked_db):
    def_db_fns('characters.sql')
    from pugsql import characters

    result = characters.insert_character(mocked_db,
                                         {'name': 'Oompa Loompa', 'specialty': 'Chocolatier'})
    assert result == 1

    cursor = mocked_db.cursor
    cursor.assert_called()
    cursor().execute.assert_called_once_with(
        "insert into characters (name, specialty) values (%(name)s, %(specialty)s);",
        {'name': 'Oompa Loompa', 'specialty': 'Chocolatier'}
    )
