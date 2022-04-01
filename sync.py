import sqlite3


class DataBase:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        # try:
        cursor.execute(sql, parameters)
        # except Exception as e:
        #     print(e)

        if commit:
            connection.commit()

        if fetchone:
            data = cursor.fetchone()

        if fetchall:
            data = cursor.fetchall()
        connection.close()

        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users(id integer , name varchar(50))
        """
        self.execute(sql=sql, commit=True)


def logger(statement):
    print(
        f"""
    -----------------------------------------------------------
    EXECUTING:
    {statement}
    ___________________________________________________________        
            """
    )

if __name__ == '__main__':
    db = DataBase()