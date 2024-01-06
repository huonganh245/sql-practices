import unittest
import psycopg2


class TestSqlQuery(unittest.TestCase):

    def setUp(self):
        self.connection = psycopg2.connect(dbname="testdb", user="postgres", password="password")
        self.cursor = self.connection.cursor()

    def tearDown(self):
        self.cursor.close()
        self.connection.close()

    def test_select_all_customers(self):
        """
        Test the query that retrieves all customers from the database.
        """
        self.cursor.execute("SELECT * FROM customers")
        customers = self.cursor.fetchall()

        self.assertEqual(len(customers), 5)
        self.assertEqual(customers[0][0], 1)
        self.assertEqual(customers[0][1], "John Doe")
        self.assertEqual(customers[0][2], "johndoe@example.com")

    def test_select_customer_by_id(self):
        """
        Test the query that retrieves a customer by ID.
        """
        self.cursor.execute("SELECT * FROM customers WHERE id = 2")
        customer = self.cursor.fetchone()

        self.assertEqual(customer[0], 2)
        self.assertEqual(customer[1], "Jane Doe")
        self.assertEqual(customer[2], "janedoe@example.com")


if __name__ == "__main__":
    unittest.main()
