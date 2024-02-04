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
    # 1.20 Apply a 10% discount to all products with a price larger than or equal to $120
    def testApply10PercentDiscountToAllProductsHavingPriceLarger120(self):
        # Create a cursor
        cursor : Cursor = self.conn.cursor()
        cursor.execute("select Name, Price*0.9 as New_Price from Products "
                       + "where Price >= 120")
        results : list = cursor.fetchall()
        self.fetchAllResult = results
    # 1.19 Apply a 10% discount to all products
    def testApply10PercentDiscountToAllProducts(self):
        # Create a cursor
        cursor : Cursor = self.conn.cursor()
        cursor.execute("select Name, Price*0.9 as New_Price from Products")
        results : list = cursor.fetchall()
        self.fetchAllResult = results
    # 1.18 Update the name of product 8 to "Laser Printer"
    def testUpdateNameOfProduct8(self):
        # Create a cursor
        cursor : Cursor = self.conn.cursor()
        cursor.execute("update Products set name = 'Laser Printer' where code = 8")
        results : list = cursor.fetchall()
        self.fetchAllResult = results
    # 1.17 Add a new product: Loudspeakers, $70, manufacturer 2
    def testAddNewProductLoudspeakers(self):
        # Create a cursor
        cursor : Cursor = self.conn.cursor()
        cursor.execute("insert into Products values (100,'Loudspeakers',70,2)")
        results : list = cursor.fetchall()
        self.fetchAllResult = results
    # 1.16 Select the name of each manufacturer along with the name and price of its most expensive product
    def testNameManufacturerAndNamePriceOfItsMostExpensiveProduct(self):
        # Create a cursor
        cursor : Cursor = self.conn.cursor()
        cursor.execute("select max_price_mapping.name as manu_name, max_price_mapping.price, products_with_manu_name.name as product_name "
                   + "from " 
                   + "(SELECT Manufacturers.Name, MAX(Price) price "
                   + "FROM Products, Manufacturers "
                   + "WHERE Manufacturer = Manufacturers.Code GROUP BY Manufacturers.Name) as max_price_mapping "
                   + "left join "
                   + "(select products.*, manufacturers.name manu_name "
                   + "from products join manufacturers "
                   + "on (products.manufacturer = manufacturers.code)) "
                   + "as products_with_manu_name "
                   + "on "
                   + "(max_price_mapping.name = products_with_manu_name.manu_name "
                   + "and "
                   + "max_price_mapping.price = products_with_manu_name.price)")
        results : list = cursor.fetchall()
        self.fetchAllResult = results
        
    # 1.15 Select the name and price of the cheapest product
    def testNamePriceCheapestProduct(self):
        # Create a cursor
        cursor : Cursor = self.conn.cursor()
        cursor.execute("select Name, Price from Products where Price = (select min(Price) from Products)")
        results : list = cursor.fetchall()
        self.fetchAllResult = results
    # 1.14 Select the names of manufacturer whose products have an average price larger than or equal to $150
    def testManufacturerNameWhoseProductsHavingAveragePriceLarger150(self):
        # Create a cursor
        cursor : Cursor = self.conn.cursor()
        cursor.execute("select m.Name, AVG(Price) from Products p left join Manufacturers m on p.Manufacturer = m.Code "
                       + "group by m.Name having AVG(Price) >= 150")
        results : list = cursor.fetchall()
        self.fetchAllResult = results
    # 1.13 Select the average price of each manufacturer's products, showing the manufacturer's name.
    def testNamePriceManufacturer(self):
        # Create a cursor
        cursor : Cursor = self.conn.cursor()
        cursor.execute("select AVG(Price), m.Name from Products p left join Manufacturers m on p.Manufacturer = m.Code "
                       + "group by m.Name")
        results : list = cursor.fetchall()
        self.fetchAllResult = results
    # 1.12 Select the average price of each manufacturer's products, showing only the manufacturer's code
    def testAveragePriceOfEachManufacturerProducts(self):
        # Create a cursor
        cursor : Cursor = self.conn.cursor()
        cursor.execute("select AVG(Price), p.Manufacturer from Products p left join Manufacturers m on p.Manufacturer = m.Code "
                       + "group by p.Manufacturer")
        results : list = cursor.fetchall()
        self.fetchAllResult = results
    # 1.11 Select the product name, price, and manufacturer name of all the products
    def testNamePriceManufacturerOfAllProducts(self):
        # Create a cursor
        cursor : Cursor = self.conn.cursor()
        cursor.execute("select p.Name, p.Price, m.Name from Products p left join Manufacturers m on p.Manufacturer = m.Code")
        results : list = cursor.fetchall()
        self.fetchAllResult = results
    # 1.10 Select all the data from the products, including all the data for each product's manufacturer
    def testAllDataFromProductsAndManufacturer(self):
        # Create a cursor
        cursor : Cursor = self.conn.cursor()
        cursor.execute("select p.*, m.Name from Products p left join Manufacturers m on p.Manufacturer = m.Code")
        results : list = cursor.fetchall()
        self.fetchAllResult = results
    # 1.9 Select the name and price of all products with a price larger than or equal to $180, and sort first by price (in descending order), and then by name (in ascending order).
    def verify_testNumberOfProductsWithPriceLarger180SortedByPrice(self):
        # Create a cursor
        cursor : Cursor = self.conn.cursor()
        cursor.execute("select Name, Price from Products where Price >= 180 order by Price DESC, Name ASC")
        results : list = cursor.fetchall()
        self.fetchAllResult = results
    # 1.8 Compute the number of products with a price larger than or equal to $180
    def testNumberOfProductsWithPriceLarger180(self):
        # Create a cursor
        cursor : Cursor = self.conn.cursor()
        cursor.execute("select count(Code) from Products where Price >= 180")
        results : list = cursor.fetchall()
        self.fetchAllResult = results
    # 1.7 Compute the average price of all products with manufacturer code equal to 2.
    def testAVGPriceProductsCode2(self):
        # Create a cursor
        cursor : Cursor = self.conn.cursor()
        cursor.execute("select AVG(Price) from Products where Manufacturer = 2")
        results : list = cursor.fetchall()
        self.fetchAllResult = results
        
    # 1.6 Compute the average price of all the products.
    def testAVGPriceAllProducts(self):
        # Create a cursor
        cursor : Cursor = self.conn.cursor()
        cursor.execute("select AVG(Price) from Products")
        results : list = cursor.fetchall()
        self.fetchAllResult = results
        
    # 1.5 Select the name and price in cents (i.e., the price must be multiplied by 100).
    def testNamePriceInCents(self):
        # Create a cursor
        cursor : Cursor = self.conn.cursor()
        cursor.execute("select Name, Price*100 from Products")
        results : list = cursor.fetchall()
        self.fetchAllResult = results
        
    # 1.4 Select all the products with a price between $60 and $120.
    def testProductsWithPricebetween60And120(self):
        # Create a cursor
        cursor : Cursor = self.conn.cursor()
        cursor.execute("select * from Products where Price between 60 and 120")
        results : list = cursor.fetchall()
        self.fetchAllResult = results
        
    # 1.3 Select the name of the products with a price less than or equal to $200.
    def testSelectProductsLess200(self):
        # Create a cursor
        cursor : Cursor = self.conn.cursor()
        cursor.execute("select Name from Products where Price <= 200")
        results : list = cursor.fetchall()
        self.fetchAllResult = results
        
    # 1.2 Select the names and the prices of all the products in the store.
    def testSelectNamesAndPrices(self):
        # Create a cursor
        cursor : Cursor = self.conn.cursor()
        cursor.execute("select Name, Price from Products")
        results : list = cursor.fetchall()
        self.fetchAllResult = results
    
    
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