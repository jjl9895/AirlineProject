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
db_config = graceconfig

# Establishing a database connection
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

# Login page
@app.route('/')
def home():
    return render_template('home.html')


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

def register_customer(email, first_name, last_name, password, pass_num, pass_exp, pass_country, dob, building_num, street, apt_num, city, state, zipcode):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO `customer` (`email`, `first_name`, `last_name`, `password`, `passport_num`, `passport_expiration`, `passport_country`, `date_of_birth`, `building_num`, `street`, `apt_num`, `city`, `state`, `zip`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(query, (email, first_name, last_name, password, pass_num, pass_exp, pass_country, dob, building_num, street, apt_num, city, state, zipcode))
    conn.commit()
    cursor.close()
    conn.close()

    return True

def register_staff(username, first_name, last_name, password, dob, airline, email, phone):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Airline WHERE name = %s", (airline,))
    user = cursor.fetchone()
    if user:
        query = "INSERT INTO `airlinestaff` (`username`, `password`, `first_name`, `last_name`, `date_of_birth`, `airline_name`) VALUES (%s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (username, first_name, last_name, password, dob, airline))
        query = "INSERT INTO `airlinestaffemails` (`staff_username`, `email`) VALUES (%s, %s);"
        cursor.execute(query, (username, email))
        query = "INSERT INTO `airlinestaffphonenumbers` (`staff_username`, `phone_number`) VALUES (%s, %s);"
        cursor.execute(query, (username, phone))
        conn.commit()
        cursor.close()
        conn.close()
    else:
        cursor.close()
        conn.close()
        return False
    return True


@app.route('/customerregistration', methods=['GET', 'POST'])
def customerregister():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        pass_num = request.form['pass_num']
        pass_exp = request.form['pass_exp']
        pass_country = request.form['pass_country']
        dob = request.form['dob']
        building_num = request.form['building_num']
        street = request.form['street']
        apt_num = request.form['apt_num']
        city = request.form['city']
        state = request.form['state']
        zipcode = request.form['zipcode']
        
        if check_customer_credentials(email, password):
            error = 'This email is already in use'
        elif register_customer(email, first_name, last_name, password, pass_num, pass_exp, pass_country, dob, building_num, street, apt_num, city, state, zipcode):
            return redirect(url_for('login')) 
        
    return render_template('customerregistration.html')


@app.route('/staffregistration', methods=['GET', 'POST'])
def staffregister():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        airline = request.form['airline']
        dob = request.form['dob']
        email = request.form['email']
        phone = request.form['phone']

        if check_airlineStaff_credentials(username, password):
            error = 'This username is already in use'
        elif register_staff(username, first_name, last_name, password, dob, airline, email, phone):
            return redirect(url_for('login')) 
        else:    
            error = 'Invalid Airline'
        
    return render_template('staffregistration.html')

# Customer Home Page
@app.route('/customerhome')
def customerhome():
    return render_template('customerhome.html')

# Airline Staff Home Page
@app.route('/airlineStaffhome')
def airlineStaffhome():
    return render_template('airlinestaffhome.html')

# Customer My Flights Page
@app.route('/customerflights')
def customerflights():
    return render_template('customerflights.html')

# Customer Flight Search Page
@app.route('/customersearch')
def customersearch():
    return render_template('customersearch.html')

if __name__ == '__main__':
    app.run(debug=True)
