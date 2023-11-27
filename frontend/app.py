from flask import Flask
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',             # or your database host
    'user': 'Jeff',         # your database username
    'password': '[_ODOim51K7VM9fi',     # your database password
    'database': 'AirportProject' # your database name
}

# Establishing a database connection
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Example query - modify according to your database structure
    cursor.execute('SELECT * FROM Airline')
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    # You can format the data as you prefer to send it to your frontend
    return str(data)  # For now, just returning raw data

if __name__ == '__main__':
    app.run(debug=True)
