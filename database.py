import aiosqlite
import asyncio


class DataBase:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    async def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        async with aiosqlite.connect(self.path_to_db) as db:
            if not parameters:
                parameters = ()
            data = None
            cursor = await db.cursor()
            await cursor.execute(sql, parameters)

            if commit:
                await db.commit()

            if fetchone:
                data = await cursor.fetchone()
            if fetchall:
                data = await cursor.fetchall()
            # await cursor.close()
            # await db.close()
            return data

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Userform(
        id integer primary key,
        name text
        )
        """
        await self.execute(sql=sql, commit=True)

    async def add_user_to_table(self, user_id: int, name: str):
        sql = """
        INSERT INTO Userform(id, name) VALUES (?,?)
        """

        await self.execute(
            sql=sql,
            parameters=(user_id, name),
            commit=True
        )

    async def get_all_users(self):
        sql = """
        SELECT * FROM Userform
        """
        return await self.execute(sql=sql, fetchall=True)



