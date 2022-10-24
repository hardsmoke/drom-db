import sqlite3
import pandas as pd

con = sqlite3.connect("drom.sqlite")

cursor = con.cursor()

# по ID автомобиля вывести название компании и модель
query = '''
SELECT company.nameCompany, modelcar.nameModelCar
FROM company, (modelcar JOIN car ON car.modelcar_idModelCar == modelcar.idModelCar) as CarInfo
WHERE CarInfo.idCar == :carId AND modelcar.company_idCompany == company.idCompany
'''
cursor.execute(query, {'carId': 14})

# вывести все автомобили с указанной трансмиссией
query = '''
SELECT idCar
FROM car JOIN drivetrain ON car.drivetrain_idDrivetrain == drivetrain.idDrivetrain
WHERE :drivetrain == car.drivetrain_idDrivetrain
'''
cursor.execute(query, {'drivetrain': 3})

# df = pd.read_sql(query, con)
print(cursor.fetchall())

con.close()
