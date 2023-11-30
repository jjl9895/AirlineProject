from flask import Flask, render_template, request, redirect, url_for
import mysql.connector


app = Flask(__name__)

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
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if check_customer_credentials(email, password):
            return redirect(url_for('customerhome'))  # Redirect to customer home page
        elif check_airlineStaff_credentials(email, password):
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
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        return True
    return False


@app.route('/customerregistration', methods=['GET', 'POST'])
def register():
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
        
        if register_customer(email, first_name, last_name, password, pass_num, pass_exp, pass_country, dob, building_num, street, apt_num, city, state, zipcode):
            return redirect(url_for('login'))  # Redirect to customer home page
        else:    
            error = 'Invalid Entries, Please Fill Out All Fields'
        
    return render_template('customerregistration.html')


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
