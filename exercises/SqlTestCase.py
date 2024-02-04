import os
from sqlite3 import Connection
import sqlite3
import unittest

class SqlTestCase(unittest.TestCase):
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.fetchAllResult = []
        self.conn: Connection
    
    def setUp(self):
        # Create an in-memory database
        # self.conn : Connection = sqlite3.connect(':memory:')
        os.remove('test.db')
        self.conn : Connection = sqlite3.connect('test.db')
        # Import data to run the test by execute the SQL file
        with open(self.getSqlImportFile(), 'r') as f:
            script = f.read()
            self.conn.executescript(script)
        # Commit the changes
        self.conn.commit()
    
    def tearDown(self):
        verifyMethod = f"verify_{self._testMethodName}"
        verifyResult = getattr(self.getSolution(), verifyMethod)(self.conn)
        self.assertEqual(len(self.fetchAllResult), len(verifyResult), f"expected: {verifyResult}\n giving: {self.fetchAllResult}")
        self.assertEqual(self.fetchAllResult, verifyResult, f"expected: {verifyResult}\n giving: {self.fetchAllResult}")
        # Close the database connection
        self.conn.close()
    
    def getSqlImportFile(self) -> str:
        return ""
        
    def getSolution(self):
        return None