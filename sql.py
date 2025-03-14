import sqlite3
from collections.abc import Collection, Iterator


class TableData(Collection):
        def __init__(self, database_name: str, table_name: str):
                self.database_name = database_name
                self.table_name = table_name

        def _execute_query(self, query: str, params: dict = None):
                with sqlite3.connect(self.database_name) as conn:
                        cursor = conn.cursor()
                        cursor.execute(query, params or {})
                        return cursor.fetchall()

        def __len__(self):
                query = f"SELECT COUNT(*) FROM {self.table_name}"
                return self._execute_query(query)[0][0]

        def __getitem__(self, name: str):
                query = f"SELECT * FROM {self.table_name} WHERE name = :name"
                result = self._execute_query(query, {"name": name})
                if not result:
                        raise KeyError(f"Не найдено: {name}")
                return result[0]

        def __contains__(self, name: str):
                query = f"SELECT 1 FROM {self.table_name} WHERE name = :name LIMIT 1"
                return bool(self._execute_query(query, {"name": name}))

        def __iter__(self):
                return TableIterator(self.database_name, self.table_name)
        
        def show_tables(self):
                query = "SELECT name FROM sqlite_master WHERE type='table';"
                tables = self._execute_query(query)
                return [table[0] for table in tables]

class TableIterator(Iterator):
        def __init__(self, database_name: str, table_name: str):
                self.conn = sqlite3.connect(database_name)
                self.cursor = self.conn.cursor()
                self.table_name = table_name
                self.cursor.execute(f"SELECT * FROM {table_name}")

        def __iter__(self):
                return self

        def __next__(self):
                row = self.cursor.fetchone()
                if row is None:
                        self.conn.close()
                        raise StopIteration
                return row

if __name__ == "__main__":
        db_name = "example.sqlite"
        table_name = "presidents"
        presidents = TableData(db_name, table_name)

        print("Таблицы в базе данных:")
        tables = presidents.show_tables()
        for table in tables:
                print(f"Таблица: '{table}'")
        
        print(f"Все значения: {len(presidents)}")
    
        test_name = "Yeltsin"
        print(f"{test_name} существует: {test_name in presidents}")
    
        if test_name in presidents:
                print(f"Строка с {test_name}: {presidents[test_name]}")
    
        print("Все президенты:")
        for president in presidents:
                print(president)