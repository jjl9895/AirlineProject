from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector


app = Flask(__name__)
app.secret_key = '184nHU'

jeffconfig = {
    'host': 'localhost',            
    'user': 'Jeff',         
    'password': '[_ODOim51K7VM9fi',    
    'database': 'AirportProject'
}

graceconfig = { 
    'host': 'localhost', 
    'user': 'graceableidinger',         
    'password': '12345',    
    'database': 'projectairport'
}  
# Database configuration
db_config = jeffconfig

# Establishing a database connection
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

# Login page
@app.route('/')
def home():
    flights = display_flights()
    return render_template('home.html', flights=flights)

def display_flights():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Flight")
    flights = cursor.fetchall()
    cursor.close()
    conn.close()
    return flights


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if check_customer_credentials(session.get('email'), session.get('password')):
        return redirect(url_for('customerhome'))
    elif check_airlineStaff_credentials(session.get('email'), session.get('password')):
        return redirect(url_for('airlineStaffhome'))
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if check_customer_credentials(email, password):
            session['email'] = email
            session['password'] = password
            return redirect(url_for('customerhome'))  # Redirect to customer home page
            
        elif check_airlineStaff_credentials(email, password):
            session['email'] = email
            session['password'] = password
            return redirect(url_for('airlineStaffhome')) # Redirect to airline staff home page 
        else:    
            error = 'Invalid credentials'

    return render_template('login.html', error=error)


def check_customer_credentials(email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Customer WHERE email = %s AND password = %s", (email, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        return True
    return False

def check_airlineStaff_credentials(email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "   SELECT * FROM AirlineStaffEmails as asemail Join AirlineStaff as astaff \
                WHERE \
                asemail.staff_username = astaff.username \
                AND asemail.email = %s \
                AND astaff.password = %s "

    cursor.execute(query, (email, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        return True
    return False


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('/'))


@app.route('/registration', methods=['GET', 'POST'])
def register():
    return render_template('registration.html')


# Customer Home Page
@app.route('/customerhome')
def customerhome():
    return render_template('customerhome.html')

# Airline Staff Home Page
@app.route('/airlineStaffhome')
def airlineStaffhome():
    return render_template('airlinestaffhome.html')

if __name__ == '__main__':
    app.run(debug=True)
