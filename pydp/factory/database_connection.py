class DatabaseConnection:
    def connect(self) -> str:
        pass


# Concrete database connection classes for different databases
class MySQLConnection(DatabaseConnection):
    def connect(self) -> str:
        return 'Connected to MySQL database'


class PostgreSQLConnection(DatabaseConnection):
    def connect(self) -> str:
        return 'Connected to PostgreSQL database'


class SQLiteConnection(DatabaseConnection):
    def connect(self) -> str:
        return 'Connected to SQLite database'


# Database Factory to create specific database connections
class DatabaseFactory:
    @staticmethod
    def create_connection(db_type: str) -> DatabaseConnection:
        if db_type == 'MySQL':
            return MySQLConnection()
        elif db_type == 'PostgreSQL':
            return PostgreSQLConnection()
        elif db_type == 'SQLite':
            return SQLiteConnection()
        else:
            raise ValueError(f'Unknown database type: {db_type}')


# Usage
db_types = ['MySQL', 'PostgreSQL', 'SQLite']
for db_type in db_types:
    connection = DatabaseFactory.create_connection(db_type)
    print(connection.connect())
