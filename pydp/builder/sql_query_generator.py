class SQLQuery:
    def __init__(self, table):
        self._table = table
        self._fields = ['*']
        self._conditions = []

    def __str__(self):
        query = f'SELECT {", ".join(self._fields)} FROM {self._table}'
        if self._conditions:
            query += ' WHERE ' + ' AND '.join(self._conditions)
        return query


class SQLQueryBuilder:
    def __init__(self, table):
        self.query = SQLQuery(table)

    def select_fields(self, *fields):
        self.query._fields = fields
        return self

    def where(self, condition):
        self.query._conditions.append(condition)
        return self

    def build(self):
        return self.query


# Usage
builder = SQLQueryBuilder('users')
custom_query = (builder.select_fields('id', 'name', 'email')
                .where('age > 21')
                .where('status = "active"')
                .build())
print(custom_query)  # Outputs: SELECT id, name, email FROM users WHERE age > 21 AND status = "active"
