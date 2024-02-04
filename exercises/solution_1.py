from sqlite3 import Connection, Cursor
#1.20
def verify_testApply10PercentDiscountToAllProductsHavingPriceLarger120(connection: Connection) -> list:
    cursor : Cursor = connection.cursor()
    cursor.execute("select Name, Price*0.9 as New_Price from Products "
                       + "where Price >= 120")
    results : list = cursor.fetchall()
    return results

#1.19 Apply a 10% discount to all products
def verify_testApply10PercentDiscountToAllProducts(connection: Connection) -> list:
    cursor : Cursor = connection.cursor()
    cursor.execute("select Name, Price*0.9 as New_Price from Products")
    results : list = cursor.fetchall()
    return results

#1.18
def verify_testUpdateNameOfProduct8(connection: Connection) -> list:
    cursor : Cursor = connection.cursor()
    cursor.execute("update products "
                   + "set name = 'Laser Printer' "
                   + "where code=8;")
    results : list = cursor.fetchall()
    return results

#1.17
def verify_testAddNewProductLoudspeakers(connection: Connection) -> list:
    cursor : Cursor = connection.cursor()
    cursor.execute("insert into Products values (11, 'Loudspeakers', 70, 2)")
    results : list = cursor.fetchall()
    return results

#1.16
def verify_testNameManufacturerAndNamePriceOfItsMostExpensiveProduct(connection: Connection) -> list:
    cursor : Cursor = connection.cursor()
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
    return results

#1.15
def verify_testNamePriceCheapestProduct(connection: Connection) -> list:
    cursor : Cursor = connection.cursor()
    cursor.execute("select name, price from Products where price = (select min(price) from products)")
    results : list = cursor.fetchall()
    return results

#1.14
def verify_testManufacturerNameWhoseProductsHavingAveragePriceLarger150(connection: Connection) -> list:
    cursor : Cursor = connection.cursor()
    cursor.execute("select b.name,avg(a.price) "
                   + "from Manufacturers b join Products a "
                   + "on b.code = a.Manufacturer "
                   + "group by b.name "
                   + "having avg(a.price)>=150")
    results : list = cursor.fetchall()
    return results

#1.13
def verify_testNamePriceManufacturer (connection: Connection) -> list:
    cursor : Cursor = connection.cursor()
    cursor.execute("select avg(a.price), b.name from Products a join Manufacturers b "
                   + "on a.manufacturer = b.code group by b.name")
    results : list = cursor.fetchall()
    return results

#1.12
def verify_testAveragePriceOfEachManufacturerProducts(connection: Connection) -> list:
    cursor : Cursor = connection.cursor()
    cursor.execute("SELECT AVG(Price), Manufacturer FROM Products GROUP BY Manufacturer")
    results : list = cursor.fetchall()
    return results

#1.11
def verify_testNamePriceManufacturerOfAllProducts(connection: Connection) -> list:
    cursor : Cursor = connection.cursor()
    cursor.execute("select a.name, a.price, b.name from products a join Manufacturers b on(a.manufacturer = b.code)")
    results : list = cursor.fetchall()
    return results

#1.10
def verify_testAllDataFromProductsAndManufacturer(connection: Connection) -> list:
    cursor : Cursor = connection.cursor()
    cursor.execute("select a.*, b.name from products a join Manufacturers b on(a.manufacturer = b.code)")
    results : list = cursor.fetchall()
    return results

#1.9
def verify_testNumberOfProductsWithPriceLarger180SortedByPrice(connection: Connection) -> list:
    cursor : Cursor = connection.cursor()
    cursor.execute("select name, price from products where price>=180 order by price desc, name asc")
    results : list = cursor.fetchall()
    return results

#1.8
def verify_testNumberOfProductsWithPriceLarger180(connection: Connection) -> list:
    cursor : Cursor = connection.cursor()
    cursor.execute("select count(*) from products where price>=180")
    results : list = cursor.fetchall()
    return results

#1.7
def verify_testAVGPriceProductsCode2(connection: Connection) -> list:
    cursor : Cursor = connection.cursor()
    cursor.execute("select avg(price) from products where  Manufacturer = 2")
    results : list = cursor.fetchall()
    return results

#1.6
def verify_testAVGPriceAllProducts(connection: Connection) -> list:
    cursor : Cursor = connection.cursor()
    cursor.execute("select avg(price) from products")
    results : list = cursor.fetchall()
    return results

#1.5
def verify_testNamePriceInCents(connection: Connection) -> list:
    cursor : Cursor = connection.cursor()
    cursor.execute("select name, price*100 from products")
    results : list = cursor.fetchall()
    return results

#1.4
def verify_testProductsWithPricebetween60And120(connection: Connection) -> list:
    cursor : Cursor = connection.cursor()
    cursor.execute("select * from products where price between 60 and 120")
    results : list = cursor.fetchall()
    return results

#1.3
def verify_testSelectProductsLess200(connection: Connection) -> list:
    cursor : Cursor = connection.cursor()
    cursor.execute("select name from products where price <= 200")
    results : list = cursor.fetchall()
    return results

#1.2
def verify_testSelectNamesAndPrices(connection: Connection) -> list:
    cursor : Cursor = connection.cursor()
    cursor.execute("select name, price from products")
    results : list = cursor.fetchall()
    return results

#1.1
def verify_testSelectProductNames(connection: Connection) -> list:
    cursor : Cursor = connection.cursor()
    cursor.execute('SELECT Name FROM Products')
    results : list = cursor.fetchall()
    return results