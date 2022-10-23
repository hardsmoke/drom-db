import sqlite3
import pandas as pd

con = sqlite3.connect("drom.sqlite")

cursor = con.cursor()

# Добавить владельца
addOwnerQuery = '''
INSERT INTO owner(phoneNumberOwner, nameOwner, surnameOwner, patronymicOwner) VALUES
(:pNumber, :name, :surname, :patronymic);
'''
cursor.execute(addOwnerQuery, {'pNumber': '89520817412', 'name': 'Сергей', 'surname': 'Ломака', 'patronymic':''})

# Добавить автомобиль владельца
addCarQuery = '''
INSERT INTO car(
owner_idOwner, mileageCar, releaseYearCar,
colorCar, carPrice, photoCar, description,
horsePowers, modelCar_idmodelCar, bodyTypeCar_idBodyTypeCar,
city_idCity, drivetrain_idDrivetrain, transmission_idTransmission) VALUES
(:ownerId, :mileage, :releaseYear, :color, :price, :photo, :description, :horsePowers, :modelId, :bodyTypeId, :cityId, :drivetrainId, :transmissionId)'''

cursor.execute(addCarQuery, 
{'ownerId': 12, 'mileage': 235, 'releaseYear': 2009,
'color': '', 'price': 250000, 'photo': '', 'description': '',
'horsePowers': 115, 'modelId': 21, 'bodyTypeId': 2,
'cityId': 10, 'drivetrainId': 1, 'transmissionId': 1})

# Добавить объявление
addAdQuery = '''
INSERT INTO advertisment(owner_idOwner, car_idCar, applicationDate) VALUES
(:ownerId, :carId, (SELECT DATE()))'''

cursor.execute(addAdQuery, {'ownerId': 12, 'carId': 27})

selectAllAds = '''SELECT * FROM advertisment'''
selectAllOwners = '''SELECT * FROM owner'''
selectAllCars = '''SELECT * FROM car'''


df = pd.read_sql(selectAllCars, con)

print(df)

con.commit()
con.close()
