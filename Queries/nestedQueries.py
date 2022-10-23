import sqlite3
import pandas as pd

con = sqlite3.connect("drom.sqlite")

cursor = con.cursor()

# найти все автомобили указанной компании и отсортироваться по возрастанию цены
query = '''
SELECT idCar, owner_idOwner, carPrice, nameModelCar
FROM (car JOIN modelcar ON car.modelcar_idModelCar == modelcar.idModelCar) as carInfo
WHERE 
    carInfo.company_idCompany == (SELECT idCompany FROM company WHERE nameCompany == :company)
GROUP BY car.carPrice
'''
cursor.execute(query, {'company': 'BMW'})

print(cursor.fetchall())

con.close()