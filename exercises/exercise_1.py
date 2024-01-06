import unittest
from sqlite3 import Cursor

from SqlTestCase import SqlTestCase
import solution_1 as solution

class TestInMemorySqlQuery(SqlTestCase):
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
    
    def getSolution(self):
        return solution

    def getSqlImportFile(self) -> str:
        return "problems/01/1_build_schema.sql"

    # 1.2 Select the names and the prices of all the products in the store.
    
    
    # 1.1 Select the names of all the products in the store.
    def testSelectProductNames(self):
        # Create a cursor
        cursor : Cursor = self.conn.cursor()
        # Execute the query
        cursor.execute('SELECT Name FROM Products')
        # Fetch all of the results
        results : list = cursor.fetchall()
        # submit result
        self.fetchAllResult = results
        
if __name__ == "__main__":
    unittest.main()
