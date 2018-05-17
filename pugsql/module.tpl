{% for statement in statements %}
def {{ statement.name }}(db, param_data=None, options=None, command_options=None):
    cursor = db.cursor()
    cursor.execute("{{ statement.sql }}")
    return cursor.fetchall()
{% endfor %}
