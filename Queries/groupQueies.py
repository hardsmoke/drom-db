import sqlite3
import pandas as pd

con = sqlite3.connect("drom.sqlite")

cursor = con.cursor()

# Посчитать сумму цен всех автомобилей, находящихся на продаже определенного человека
query = '''
SELECT SUM(sellingCars.carPrice)
FROM (advertisment JOIN car ON advertisment.car_idCar == car.idCar) as sellingCars
WHERE advertisment.owner_idOwner == :ownerId'''

cursor.execute(query, {'ownerId': 1})

# Вывести количество автомобилей, находящихся в объявлениях с ценой, выше указанной
query = '''
SELECT COUNT(sellingCars.idCar)
FROM (advertisment JOIN car ON advertisment.car_idCar == car.idCar) as sellingCars
WHERE sellingCars.carPrice > :price
'''

cursor.execute(query, {'price': 4500000})

print(cursor.fetchall())

con.commit()
con.close()