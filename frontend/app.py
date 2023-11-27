from flask import Flask, render_template, request, redirect, url_for
import mysql.connector


app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',            
    'user': 'Jeff',         
    'password': '[_ODOim51K7VM9fi',    
    'database': 'AirportProject'
}

# Establishing a database connection
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

# Login page
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if check_credentials(email, password):
            return redirect(url_for('home'))  # Redirect to home page if login is successful
        else:
            error = 'Invalid credentials'

    return render_template('login.html', error=error)

def check_credentials(email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user and password:
        return True
    return False

@app.route('/home')
def home():
    return "Welcome to the home page"


@app.route('/index')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Airline')
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
