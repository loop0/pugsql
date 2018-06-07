{% for statement in statements %}
def {{ statement.name }}(db, param_data=None, options=None, command_options=None):
    cursor = db.cursor()
    statement = "{{ statement.sql }}"
    qargs = [statement]
    if param_data:
        qargs.append(param_data)
    cursor.execute(*qargs)
    {% if statement.result == ":1" %}
    return cursor.fetchone()
    {% elif statement.result in (":*", ":raw") or statement.command == ":<!" %}
    return cursor.fetchall()
    {% elif statement.result == ":n" %}
    return cursor.rowcount
    {% else %}
    return
    {% endif %}
{% endfor %}
