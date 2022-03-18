from database import DataBase
import asyncio
if __name__ == "__main__":
    async def test():
        db = DataBase()
        # await db.create_table()
        # await db.create_table_users()
        # await db.add_user_to_table(user_id=1, name="Name")
        print("user qoshildi")
        data = await db.get_all_users()
        print(data)
asyncio.run(test())