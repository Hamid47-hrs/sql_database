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

    def add_items(self, items: tuple):
        for item_value in items:
            sql_script = f"INSERT INTO {self.table_name}(name, age, gender, is_married) VALUES(?, ?, ?, ?)"
            self.connection.execute(sql_script, item_value)
            self.connection.commit()

    def read_item(self, column_name: str):
        """Returns the SQL cursor. You have to loop through it with the "for" method."""

        sql_script = f" SELECT ({column_name}) FROM {self.table_name}"
        data = self.connection.execute(sql_script)

        return data

    def read_all_items(self):
        """Returns the SQL cursor. You have to loop through it with the "for" method."""

        sql_script = f" SELECT * FROM {self.table_name}"
        data = self.connection.execute(sql_script)

        return data

    def update_items(self, new_data: dict, condition: dict):
        new_data_list = [(key, value) for key, value in new_data.items()]
        condition_key = [key for key in condition.keys()][0]
        condition_value = [value for value in condition.values()][0]

        if type(condition_value) == str:
            for item in new_data_list:
                if type(item[1]) == str:
                    data_script = f""" UPDATE {self.table_name}
                                        SET {item[0]} = '{item[1]}'
                                        WHERE {condition_key} = '{condition_value}'"""
                    self.connection.execute(data_script)
                    self.connection.commit()
                else:
                    data_script = f""" UPDATE {self.table_name}
                                        SET {item[0]} = {item[1]}
                                        WHERE {condition_key} = '{condition_value}'"""
                    self.connection.execute(data_script)
                    self.connection.commit()
        else:
            for item in new_data_list:
                if type(item[1]) == str:
                    data_script = f""" UPDATE {self.table_name}
                                        SET {item[0]} = '{item[1]}'
                                        WHERE {condition_key} = {condition_value}"""
                    self.connection.execute(data_script)
                    self.connection.commit()
                else:
                    data_script = f""" UPDATE {self.table_name}
                                        SET {item[0]} = {item[1]}
                                        WHERE {condition_key} = {condition_value}"""
                    self.connection.execute(data_script)
                    self.connection.commit()

    def delete_items(self, condition):
        condition_key = [key for key in condition.keys()][0]
        condition_value = [value for value in condition.values()][0]
        data_script = """"""

        if type(condition_value) == str:
            data_script = f""" DELETE FROM {self.table_name} WHERE {condition_key} = '{condition_value}'"""
        else:
            data_script = f""" DELETE FROM {self.table_name} WHERE {condition_key} = {condition_value}"""

        self.connection.execute(data_script)
        self.connection.commit()

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

my_database.add_items(
    items=[
        ("Hamid", 29, "male", False),
        ("Ali", 13, "male", False),
        ("Sara", 31, "female", True),
        ("Mamad", 50, "male", True),
    ]
)

my_database.read_all_items()

new_data = {"name": "Hamid Reza", "age": 30, "is_married": True}

condition = {"age": 50}

my_database.update_items(new_data, condition)

# my_database.delete_items(condition)
my_database.close_database()
