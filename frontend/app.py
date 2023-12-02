from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta #pip install python-dateutil


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


def register_customer(email, first_name, last_name, password, pass_num, pass_exp, pass_country, dob, building_num, street, apt_num, city, state, zipcode, phone):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO `customer` (`email`, `first_name`, `last_name`, `password`, `passport_num`, `passport_expiration`, `passport_country`, `date_of_birth`, `building_num`, `street`, `apt_num`, `city`, `state`, `zip`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(query, (email, first_name, last_name, password, pass_num, pass_exp, pass_country, dob, building_num, street, apt_num, city, state, zipcode))
    query = "INSERT INTO `customerphonenumbers` (`customer_email`, `phone_number`) VALUES (%s, %s);"
    cursor.execute(query, (email, phone))
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
    show_login_popup = False
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
        phone = request.form['phone']
        
        if check_customer_credentials(email, password)[0]:
            show_login_popup = True
        elif register_customer(email, first_name, last_name, password, pass_num, pass_exp, pass_country, dob, building_num, street, apt_num, city, state, zipcode, phone):
            return redirect(url_for('customerlogin')) 
        
    return render_template('customerregistration.html', show_login_popup = show_login_popup)


@app.route('/staffregistration', methods=['GET', 'POST'])
def staffregister():
    message = None
    show_login_popup = False
    if request.method == 'POST':
        username = request.form['username']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        airline = request.form['airline']
        dob = request.form['dob']
        email = request.form['email']
        phone = request.form['phone']

        if check_airlineStaff_credentials(username, password)[0]:
            show_login_popup = True
        elif register_staff(username, first_name, last_name, password, dob, airline, email, phone):
            return redirect(url_for('stafflogin')) 
        else:    
            message = "This airline is invalid. Please check airline name."
        
    return render_template('staffregistration.html', message = message, show_login_popup = show_login_popup)
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('/'))

def last_year_total():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT FORMAT(SUM(price), 2) AS total FROM ticket JOIN purchasehistory ON purchasehistory.ticket_id = ticket.id WHERE purchasehistory.customer_email = %s AND purchase_date BETWEEN %s AND %s;"
    one_year_ago = datetime.now()- timedelta(days=365)
    cursor.execute(query, (session['email'], one_year_ago.date(), datetime.now().date()))
    total = cursor.fetchone()
    cursor.close()
    conn.close()
    return total[0]

# Customer Home Page
@app.route('/customerhome')
def customerhome():
    year_spending = last_year_total()
    return render_template('customerhome.html', year_spending=year_spending)

# Airline Staff Home Page
@app.route('/airlineStaffhome', methods=['GET', 'POST'])
def airlineStaffhome():
    flights = None
    start_date = datetime.now().date()
    end_date = start_date + relativedelta(days=30)
    if request.method == 'POST':
        if 'start_date' in request.form and 'end_date' in request.form:
            start_date = request.form.get('start_date')
            end_date = request.form.get('end_date')
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            SELECT * FROM Flight
            WHERE dep_date BETWEEN %s AND %s
        """
        cursor.execute(query, (start_date, end_date))
        flights = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        # Handle exception or invalid input
        print(f"An error occurred: {e}")

    return render_template('airlinestaffhome.html', flights=flights)

# Customer My Flights Page
@app.route('/customerflights')
def customerflights():
    return render_template('customerflights.html')

# Customer Flight Search Page
@app.route('/customersearch')
def customersearch():
    return render_template('customersearch.html')

@app.route('/create', methods=['GET','POST'])
def create():
    create_type = "flight"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute ("SELECT id FROM airplane")
    airplane_ids = cursor.fetchall()
    cursor.execute ("SELECT code FROM airport")
    airports = cursor.fetchall()
    cursor.close()
    conn.close()
    if request.method == 'POST':
        create_type = request.form.get('create_type')
    return render_template('create.html', create_type=create_type, airplane_ids=airplane_ids, airports=airports)

@app.route('/create_flight', methods=['POST'])
def create_flight():
    if request.method == 'POST':
        # Extract flight details from the form
        flight_num = request.form.get('flight_num')
        dep_date = request.form.get('dep_date')
        dep_time = request.form.get('dep_time')
        arr_time = request.form.get('arr_time')
        arr_date = request.form.get('arr_date')
        base_price = request.form.get('base_price')
        airplane_id = request.form.get('airplane_id')
        dep_airport = request.form.get('dep_airport')
        arr_airport = request.form.get('arr_airport')
        status = request.form.get('status')

        # Inserting data into the database
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "SELECT airline_name FROM airlinestaff WHERE username = %s"
            cursor.execute(query, (session["email"], ))
            airline_name = cursor.fetchone()[0]

            insert_query = """
                INSERT INTO Flight (num, dep_date, dep_time, arr_time, arr_date, base_price, airplane_id, airline_name, dep_airport, arr_airport, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (flight_num, dep_date, dep_time, arr_time, arr_date, base_price, airplane_id, airline_name, dep_airport, arr_airport, status))
            conn.commit()
        except Exception as e:
            conn.rollback()
            cursor.close()
            conn.close()
            return f"An error occurred: {e}", 500
        finally:
            cursor.close()
            conn.close()

    # If the method is not POST, redirect to the airline staff home page
    return redirect(url_for('airlineStaffhome'))

def calc_age(date_str):
    date= datetime.strptime(date_str, '%Y-%m-%d')
    age = datetime.now() - date
    years = (age.days)/365
    return years

@app.route('/create_airplane', methods=['POST'])
def create_airplane():
    if request.method == 'POST':
        # Extract flight details from the form
        airplane_id = request.form.get('airplane_id')
        num_of_seats = request.form.get('num_of_seats')
        manufacturer = request.form.get('manufacturer')
        model_num = request.form.get('model_num')
        manufacture_date = request.form.get('manufacture_date')

        age = calc_age(manufacture_date)
        # Inserting data into the database
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "SELECT airline_name FROM airlinestaff WHERE username = %s"
            cursor.execute(query, (session["email"], ))
            airline_name = cursor.fetchone()[0]

            
            insert_query = """
                INSERT INTO Airplane (id, num_of_seats, manufacturer, model_num, manufacture_date, age, airline_name)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(insert_query, (airplane_id, num_of_seats, manufacturer, model_num, manufacture_date, age, airline_name))
            conn.commit()
        except Exception as e:
            conn.rollback()
            cursor.close()
            conn.close()
            return f"An error occurred: {e}", 500
        finally:
            cursor.close()
            conn.close()

    # If the method is not POST, redirect to the airline staff home page
    return redirect(url_for('create'))

@app.route('/create_airport', methods=['POST'])
def create_airport():
    if request.method == 'POST':
        # Extract flight details from the form
        code = request.form.get('code')
        name = request.form.get('name')
        city = request.form.get('city')
        country = request.form.get('country')
        num_of_term = request.form.get('num_of_term')
        airport_type = request.form.get('type')

        # Inserting data into the database
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
        
            insert_query = """
                INSERT INTO Airport (code, name, city, country, num_of_terminals, type)
                VALUES (%s, %s, %s, %s, %s, %s);
            """
            cursor.execute(insert_query, (code, name, city, country, num_of_term, airport_type))
            conn.commit()
        except Exception as e:
            conn.rollback()
            cursor.close()
            conn.close()
            return f"An error occurred: {e}", 500
        finally:
            cursor.close()
            conn.close()

    # If the method is not POST, redirect to the airline staff home page
    return redirect(url_for('create'))

@app.route('/schedule_maintenance', methods=['POST'])
def schedule_maintenance():
    if request.method == 'POST':
        # Extract flight details from the form
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')
        airplane_id = request.form.get('airplane_id')

        # Inserting data into the database
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            insert_query = """
                INSERT INTO Maintenance (start_date, start_time, end_date, end_time, airplane_id)
                VALUES (%s, %s, %s, %s, %s);
            """
            cursor.execute(insert_query, (start_date, start_time, end_date, end_time, airplane_id))
            conn.commit()
        except Exception as e:
            conn.rollback()
            cursor.close()
            conn.close()
            return f"An error occurred: {e}", 500
        finally:
            cursor.close()
            conn.close()

    # If the method is not POST, redirect to the airline staff home page
    return redirect(url_for('create'))

if __name__ == '__main__':
    app.run(debug=True)