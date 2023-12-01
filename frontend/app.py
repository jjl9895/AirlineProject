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


@app.route('/customerlogin', methods=['GET', 'POST'])
def customerlogin():
    message = None
    show_register_popup = False

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user_exists, password_correct = check_customer_credentials(email, password)
        if user_exists:
            if password_correct:
                session['email'] = email
                return redirect(url_for('customerhome'))  # Redirect to customer home page
            else:
                message = 'Wrong password. Try again.'
        else:
            show_register_popup = True  # User does not exist, offer registration

    return render_template('customerlogin.html', message=message, show_register_popup=show_register_popup)


@app.route('/stafflogin', methods=['GET', 'POST'])
def stafflogin():
    message = None
    show_register_popup = False

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user_exists, password_correct = check_airlineStaff_credentials(username, password)
        if user_exists:
            if password_correct:
                session['email'] = username
                return redirect(url_for('airlineStaffhome'))  # Redirect to customer home page
            else:
                message = 'Wrong password. Try again.'
        else:
            show_register_popup = True  # User does not exist, offer registration

    return render_template('stafflogin.html', message=message, show_register_popup=show_register_popup)


def check_customer_credentials(email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM Customer WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        password_correct = user[0] == password
        return True, password_correct
    return False, False

def check_airlineStaff_credentials(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "SELECT password FROM AirlineStaff WHERE username = %s"
    
    cursor.execute(query, (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        password_correct = user[0] == password
        return True, password_correct
    return False, False


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


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('/'))


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
