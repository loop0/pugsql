# pugsql
PugSQL is HugSQL for Python (but not yet)

[![Build Status](https://travis-ci.org/loop0/pugsql.svg?branch=master)](https://travis-ci.org/loop0/pugsql) [![Coverage Status](https://coveralls.io/repos/github/loop0/pugsql/badge.svg?branch=master)](https://coveralls.io/github/loop0/pugsql?branch=master)

## Usage

`characters.sql`
```sql
-- :name character-by-id :? :1
select * from characters
where id = :id;
```

`example.py`
```python
import psycopg2
from psycopg2.extras import RealDictCursor
from pugsql import characters

conn = psycopg2.connect('postgres://postgres@localhost:5432/db', cursor_factory=RealDictCursor)
characters.character_by_id(conn, {'id': 1})
# {'id': 1, 'name': 'Bruno Ribeiro', 'specialty': 'Backend Developer', 'created_at': datetime.datetime(2018, 6, 7, 2, 8, 5, 449020)}
```

## TODO
- [ ] Everything :)
