from flask import Flask, jsonify
import mysql.connector as con
import pandas as pd
import os
import geopandas as gpd
from shapely.geometry import Point

app = Flask(__name__)

def get_db_connection():
    mydb = con.connect(
        host="localhost",
        user="root",
        password="Hyper",
        database="crime"
    )
    return mydb

@app.route('/initialize', methods=['GET'])
def initialize_db():
    mydb = get_db_connection()
    mycursor = mydb.cursor()

    # Create database and tables
    mycursor.execute("CREATE DATABASE IF NOT EXISTS crime;")
    mycursor.execute("USE crime;")
    mycursor.execute("CREATE TABLE IF NOT EXISTS crime_data (Crime_Type VARCHAR(255), Location VARCHAR(255), Latitude INT, Longitude INT);")
    mycursor.execute("CREATE TABLE IF NOT EXISTS rape (Area VARCHAR(255), Crime_Type VARCHAR(255), Cases INT);")

    # Read the CSV file into a DataFrame
    file_path = r"C:\\Users\\Acer\\Downloads\\sample_crime_data.csv"
    df = pd.read_csv(file_path)
    columns = ['Crime_Type', 'Location', 'Latitude', 'Longitude']
    filtered_df = df[columns]

    # Convert the DataFrame to a list of tuples
    data_tuples = list(filtered_df.itertuples(index=False, name=None))

    # Insert data into the table
    set6 = "INSERT INTO crime_data VALUES (%s, %s, %s, %s);"
    mycursor.executemany(set6, data_tuples)
    mydb.commit()

    return jsonify({"message": "Database initialized and data inserted successfully."})

@app.route('/data', methods=['GET'])
def get_data():
    mydb = get_db_connection()
    mycursor = mydb.cursor()

    # Fetch data from the database
    mycursor.execute("SELECT latitude, longitude, crime_type FROM crime_data;")
    data = mycursor.fetchall()
    mydb.close()
    df3 = pd.DataFrame(data, columns=['latitude', 'longitude', 'crime_type'])
if __name__== '__main__':
    app.run(debug=True)
