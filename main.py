from mysql.connector import Error
from greetings import Greetings
import mysql.connector
import pandas as pd
import os
import warnings

#FOR FINAL USE ONLY, IMPORTANT CODE WARNINGS MAY BE IGNORED WHILE DEBUGGING!
warnings.filterwarnings("ignore")

brand_list = []
brand_characteristics = []
characteristics_map = {}
d_desc_map = {}
bestsell_map = {}

#creates connection to MySQL local DB
def create_server_connection(host_name, user_name, user_password, database):
    connection = None
    try:
        connection = mysql.connector.connect(
        host = host_name,
        user = user_name,
        passwd = user_password,
        database = database,
        buffered = True
        )
        #print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

connection = create_server_connection("localhost", "root", "Sacomode", "carchooser")

#gets a car_brand list from DB 
def get_DB_Brands(cursor):
    cursor.execute("SELECT brand FROM carchooser.brands")
    Brands = []
    for row in cursor:
        for field in row:
            Brands.append(field)
    return Brands



#loads the knowledge from MySQL DB into variables
def preprocess():
    cursor = connection.cursor()
    brand_list = get_DB_Brands(cursor)

    for car_brand in brand_list:

        cursor.execute(f"SELECT {car_brand} FROM carchooser.characteristics")
        Characteristics = []
        for row in cursor:
            for field in row:
                Characteristics.append(field)
        brand_characteristics.append(Characteristics)
        characteristics_map[str(Characteristics)] = car_brand

        cursor.execute(f"SELECT description FROM carchooser.brands WHERE brand = '{car_brand}'")
        description =  pd.read_sql(f"SELECT description FROM carchooser.brands WHERE brand = '{car_brand}'", connection)
        d_desc_map[car_brand] = description.iloc[0,0]

        cursor.execute(f"SELECT bestsell FROM carchooser.brands WHERE brand = '{car_brand}'")
        treatment =  pd.read_sql(f"SELECT bestsell FROM carchooser.brands WHERE brand = '{car_brand}'", connection)
        bestsell_map[car_brand] = treatment.iloc[0,0]


def get_details(car_brand): return d_desc_map[car_brand]

def get_characteristics(car_brand): return bestsell_map[car_brand]

def if_not_matched(car_brand):
    print("")
    id_car_brand = car_brand
    car_brand_details = get_details(id_car_brand)
    characteristics = get_characteristics(id_car_brand)
    os.system('cls')
    print(f"According to your necessities you are looking for a: {id_car_brand}\n")
    print(f"Description: \n{car_brand_details}\n")
    print(f"Brand Best Seller: {characteristics}\n")

#program entry point
if __name__ == "__main__":
    preprocess()

    #creating class object
    engine = Greetings(characteristics_map, if_not_matched, get_characteristics, get_details)

    #loop to keep running the code until user says no when asked for another diagnosis
    while 1:
        engine.reset()
        engine.run()
        print("\nWould you like to repeat this cuestionary? (Reply yes or no)")
        if input() == "no":
            exit()
