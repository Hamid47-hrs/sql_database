import sqlite3 as sql


class PythonSqliteDataBase(object):
    def __init__(
        self,
        database_name: str = "SQLite_DataBase",
        table_name: str = "SQLite_table",
        columns: list = [],
    ):
        self.database_name = database_name
        self.table_name = table_name
        self.columns = columns
        self.connection = sql.connect(self.database_name + ".db")

        def create_table(self):
            table = f""" CREATE TABLE IF NOT EXISTS {self.table_name} (
                                id INTEGER PRIMARY KEY
                                )"""

            self.connection.execute(table)

            for item, type in self.columns:
                table = f""" ALTER TABLE {self.table_name} ADD {item} {type}"""

                self.connection.execute(table)

        create_table(self)

    def add_items_to_table(self, items: tuple):
        for item_value in items:
            data_script = f"INSERT INTO {self.table_name}(name, age, gender, is_married) VALUES(?, ?, ?, ?)"
            self.connection.execute(data_script, item_value)
            self.connection.commit()

    def read_item_from_table(self):
        data_script = f" SELECT * FROM {self.table_name}"
        data = self.connection.execute(data_script)

        for item in data:
            print(item)

    def close_database(self):
        self.connection.close()


my_database = PythonSqliteDataBase(
    database_name="A_database",
    table_name="costomers",
    columns=[
        ("name", "text"),
        ("age", "integer"),
        ("gender", "text"),
        ("is_married", "boolean"),
    ],
)

my_database.add_items_to_table(
    items=[
        ("Hamid", 29, "male", False),
        ("Ali", 13, "male", False),
        ("Sara", 31, "female", True),
        ("Mamad", 50, "male", True),
    ]
)
my_database.read_item_from_table()
my_database.close_database()
