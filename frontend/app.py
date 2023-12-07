from flask import Flask, render_template, request, redirect, url_for, session, flash, get_flashed_messages
import mysql.connector
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import hashlib
import sys

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
    'user': 'graceableidnger',         
    'password': '12345',    
    'database': 'projectairport'
}  

nikhilconfig = { 
    'host': 'localhost', 
    'user': 'nikhilreddy',         
    'password': '123456',    
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
    session.clear()
    return render_template('home.html')

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
                if 'next' in session:
                    return redirect(session['next']) # Redirect to the page the user was trying to access
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
                conn = get_db_connection()
                cursor = conn.cursor()
                session['username'] = username
                query = "SELECT airline_name FROM airlinestaff WHERE username = %s"
                cursor.execute(query, (session['username'], ))
                session['airline'] = cursor.fetchone()[0]
                cursor.close()
                conn.close()
                return redirect(url_for('staffhome'))  # Redirect to staff home page
            else:
                message = 'Wrong password. Try again.'
        else:
            show_register_popup = True  # User does not exist, offer registration

    return render_template('stafflogin.html', message=message, show_register_popup=show_register_popup)


def check_customer_credentials(email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT password FROM Customer WHERE email = %s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    password = hashlib.md5(password.encode()).hexdigest()

    if user:
        password_correct = user[0] == password
        return True, password_correct
    return False, False

def check_airlineStaff_credentials(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    password = hashlib.md5(password.encode()).hexdigest()
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
    query = "INSERT INTO `customer` (`email`, `first_name`, `last_name`, `password`, `passport_num`, `passport_expiration`, `passport_country`, `date_of_birth`, `building_num`, `street`, `apt_num`, `city`, `state`, `zip`) VALUES (%s, %s, %s, MD5(%s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
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
    query = "SELECT * FROM Airline WHERE name = %s"
    cursor.execute(query, (airline,))
    user = cursor.fetchone()
    if user:
        query = "INSERT INTO `airlinestaff` (`username`, `password`, `first_name`, `last_name`, `date_of_birth`, `airline_name`) VALUES (%s, MD5(%s), %s, %s, %s, %s);"
        cursor.execute(query, (username, password, first_name, last_name, dob, airline))
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
            if 'next' in session:
                return redirect(session['next'])
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
    return redirect(url_for('home'))

def last_year_total(start_date, end_date):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT FORMAT(SUM(price), 2) AS total FROM ticket JOIN purchasehistory ON purchasehistory.ticket_id = ticket.id WHERE purchasehistory.customer_email = %s AND purchase_date BETWEEN %s AND %s;"
    cursor.execute(query, (session['email'], start_date, end_date))
    total = cursor.fetchone()
    cursor.close()
    conn.close()
    return total[0]


def last_6m_total():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT FORMAT(SUM(price), 2) AS total FROM ticket JOIN purchasehistory ON purchasehistory.ticket_id = ticket.id WHERE purchasehistory.customer_email = %s AND purchase_date BETWEEN %s AND %s;"
    one_year_ago = datetime.now()- timedelta(days=183)
    cursor.execute(query, (session['email'], one_year_ago.date(), datetime.now().date()))
    total = cursor.fetchone()
    cursor.close()
    conn.close()
    return total[0]

# Customer Home Page
@app.route('/customerhome', methods=['GET', 'POST'])
def customerhome():
    end_date_tot = datetime.now().date()
    start_date_tot = end_date_tot - relativedelta(years=1)
    
    end_date_6m = datetime.now().date()
    start_date_6m = end_date_6m - relativedelta(months=6)
    if request.method == "POST":
        if 'start_date_tot' in request.form and 'end_date_tot' in request.form:
            start_date_tot = request.form.get('start_date_tot')
            end_date_tot = request.form.get('end_date_tot')

        if 'start_date_6m' in request.form and 'end_date_6m' in request.form:
            start_date_6m = request.form.get('start_date_6m')
            end_date_6m = request.form.get('end_date_6m')

    year_spending = last_year_total(start_date_tot, end_date_tot)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """SELECT
        DATE_FORMAT(purchasehistory.purchase_date, '%Y-%m') AS month,
        SUM(ticket.price) AS total_spending
        FROM
            ticket JOIN purchasehistory ON purchasehistory.ticket_id = ticket.id
        WHERE
            purchasehistory.customer_email = %s AND purchase_date BETWEEN %s AND %s
        GROUP BY
            month
        ORDER BY
            month;"""
        cursor.execute(query, (session['email'], start_date_6m, end_date_6m))
        spending_6m = cursor.fetchall()
    except Exception as e:
        # Handle exception or invalid input
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

    return render_template('customerhome.html', year_spending=year_spending, spending_6m=spending_6m)

# Airline Staff Home Page
@app.route('/staffhome', methods=['GET', 'POST'])
def staffhome():
    result = "NULL"
    if(get_flashed_messages()):
        result = get_flashed_messages()[0]
        get_flashed_messages().clear()
    flights = None
    start_date = datetime.now().date()
    end_date = start_date + relativedelta(days=30)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute ("SELECT num FROM flight")
    flight_nums = cursor.fetchall()

    if request.method == 'POST':
        if 'start_date' in request.form and 'end_date' in request.form:
            start_date = request.form.get('start_date')
            end_date = request.form.get('end_date')
    try:
        query = """
            SELECT * FROM Flight
            WHERE dep_date BETWEEN %s AND %s AND airline_name = %s
        """
        cursor.execute(query, (start_date, end_date, session['airline']))
        flights = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        # Handle exception or invalid input
        print(f"An error occurred: {e}")

    return render_template('staffhome.html', flights=flights, flight_nums=flight_nums, result=result)

@app.route('/change_status', methods=['POST'])
def changestatus():
    if request.method == 'POST':
        try:
            status = request.form.get('status')
            flight_num = request.form.get('flight_num')

            conn = get_db_connection()
            cursor = conn.cursor()
            query = "UPDATE `flight` SET `status` = %s WHERE `num` = %s"
            cursor.execute(query, (status, flight_num))
            conn.commit()
        except Exception as e:
            conn.rollback()
            cursor.close()
            conn.close()
            return f"An error occurred: {e}", 500
        finally:
            cursor.close()
            conn.close()
    return redirect(url_for('staffhome'))

# Customer My Flights Page
@app.route('/customerflights')
def customerflights():
    customer = session['email']
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT f.num, f.dep_airport, f.arr_airport, f.dep_date, f.dep_time, f.arr_date, f.arr_time, f.status, t.airline_name \
            FROM PurchaseHistory as ph \
            JOIN Ticket as t on t.id = ph.ticket_id \
            JOIN Flight as f on f.num = t.flight_num \
            WHERE ph.customer_email = %s AND f.dep_date >= CURDATE()" 
    
    cursor.execute(query, (customer,))
    future_flights = cursor.fetchall()
    query = "SELECT f.num, f.dep_airport, f.arr_airport, f.dep_date, f.dep_time, f.arr_date, f.arr_time, f.status, t.airline_name \
            FROM PurchaseHistory as ph \
            JOIN Ticket as t on t.id = ph.ticket_id \
            JOIN Flight as f on f.num = t.flight_num \
            WHERE ph.customer_email = %s AND f.dep_date < CURDATE()"
    cursor.execute(query, (customer,))
    past_flights = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('customerflights.html', past_flights=past_flights, future_flights=future_flights)

@app.route('/viewcustomers/<int:flight_num>/<dep_date>/<dep_time>', methods=['GET', 'POST'])
def viewcustomers(flight_num, dep_date, dep_time):
    if 'username' not in session:
        return redirect(url_for('stafflogin'))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT c.email, first_name, last_name, passport_num, passport_expiration, passport_country, date_of_birth, building_num, street, apt_num, city, state, zip FROM Customer as c JOIN Ticket as t on c.email=t.customer_email WHERE airline_name = %s AND flight_num = %s AND flight_dep_date = %s AND flight_dep_time=%s"
    cursor.execute(query, (session['airline'],flight_num, dep_date, dep_time))
    customers = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('viewcustomers.html', flight_num=flight_num, dep_date=dep_date, dep_time=dep_time, customers=customers)


@app.route('/purchasetickets/<int:flight_id>', methods=['GET', 'POST'])
def purchasetickets(flight_id):
    if 'email' not in session:
        session['next'] = url_for('purchasetickets', flight_id=flight_id)
        return redirect(url_for('customerlogin'))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Flight WHERE num = %s"
    cursor.execute(query, (flight_id,))
    flight = cursor.fetchone()

    airplane_id = flight[6]
    query = "SELECT * FROM Airplane WHERE id = %s"
    cursor.execute(query, (airplane_id,))
    airplane = cursor.fetchone()
    num_seats = airplane[1]

    query = "SELECT COUNT(*) FROM PurchaseHistory as ph JOIN Ticket as t on t.id = ph.ticket_id WHERE t.flight_num = %s"
    cursor.execute(query, (flight_id,))
    num_tickets_sold = cursor.fetchone()[0]

    percentage_full = num_tickets_sold / num_seats * 100
    if percentage_full >= 100:
        return "This flight is full. Please select another flight."
    additional_cost = 0
    if percentage_full >= 80: 
        additional_cost = 0.25
    
    query = "SELECT id, price, flight_num, flight_dep_date, flight_dep_time, airline_name FROM Ticket WHERE flight_num = %s AND customer_email IS NULL"
    cursor.execute(query, (flight_id,))
    tickets = cursor.fetchall()

    modified_tickets = []
    for ticket in tickets:
        ticket_list = [ticket[0], ticket[1] + ticket[1] * additional_cost, ticket[2], ticket[3], ticket[4], ticket[5]]
        modified_tickets.append(ticket_list)

    return render_template('purchasetickets.html', flight_id=flight_id, tickets=modified_tickets)

@app.route('/buyticket/<int:ticket_id>', methods=['GET', 'POST'])
def buyticket(ticket_id):
    email = session['email']
    time = datetime.now().time()
    purchase_date = datetime.now().date()
    if request.method == 'POST': 

        card_type = request.form.get('card_type')
        card_number = request.form.get('card_number')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        expiration_date = request.form.get('expiration_date')
        full_name = first_name + " " + last_name

        conn = get_db_connection()
        cursor = conn.cursor()
        query = "UPDATE Ticket SET customer_email = %s WHERE id = %s"
        cursor.execute(query, (email, ticket_id))

        query = "SELECT date_of_birth FROM Customer WHERE email = %s"
        cursor.execute(query, (email,))
        dob = cursor.fetchone()[0]

        query = """INSERT INTO PurchaseHistory (customer_email, purchase_time, card_num, exp_date, purchase_date, first_name, last_name, 
            name_on_card, date_of_birth, card_type, ticket_id) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"""
        cursor.execute(query, (email, time, card_number, expiration_date, purchase_date, first_name, last_name, full_name, dob, card_type, ticket_id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('customerflights'))


    return render_template('buyticket.html', ticket_id=ticket_id)

@app.route('/reviewflight/<int:flight_num>/<dep_date>/<dep_time>/<airline_name>', methods=['GET', 'POST'])
def reviewflight(flight_num, dep_date, dep_time, airline_name):
    email = session['email']
    if request.method == 'POST': 
        rating = request.form.get('rating')
        comments = request.form.get('comments')

        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO reviews (customer_email, flight_num, rating, comment, dep_date, dep_time, airline_name) \
            VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (email, flight_num, rating, comments, dep_date, dep_time, airline_name))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('customerflights'))


    return render_template('reviewflight.html', flight_num=flight_num, dep_date=dep_date, dep_time=dep_time, airline_name=airline_name)

# Flight Search Page
@app.route('/searchflights', methods=['GET', 'POST'])
def searchflights():
    flights = None  # Default to no flights

    if request.method == 'POST':
        departure_airport = request.form['departure_airport']
        arrival_airport = request.form['arrival_airport']
        departure_date = request.form['departure_date']

        # Query the database for flights
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT num, dep_airport, arr_airport, dep_date, dep_time, arr_date, arr_time, status \
              FROM Flight WHERE dep_airport = %s AND arr_airport = %s AND dep_date = %s AND dep_date >= CURDATE()"
        cursor.execute(query, (departure_airport, arrival_airport, departure_date))
        flights = cursor.fetchall()
        cursor.close()
        conn.close()

    return render_template('searchflights.html', flights=flights)
@app.route('/create', methods=['GET','POST'])
def create():
    result = "NULL"
    if(get_flashed_messages()):
        result = get_flashed_messages()[0]
        get_flashed_messages().clear()
    create_type = "flight"
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT id FROM airplane WHERE airline_name = %s"
    cursor.execute (query, (session['airline'], ))
    airplane_ids = cursor.fetchall()
    cursor.execute ("SELECT code FROM airport")
    airports = cursor.fetchall()
    cursor.close()
    conn.close()
    if request.method == 'POST':
        create_type = request.form.get('create_type')
    return render_template('create.html', create_type=create_type, airplane_ids=airplane_ids, airports=airports, result=result)

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
        cursor.execute("SELECT EXISTS(SELECT 1 FROM maintenance WHERE CURDATE() BETWEEN start_date AND end_date AND airplane_id = %s)", (airplane_id,))
        exists = cursor.fetchall()
        if exists == 1:
            raise Exception("Plane under maintenace")

        dep_airport = request.form.get('dep_airport')
        arr_airport = request.form.get('arr_airport')
        status = request.form.get('status')
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT num, dep_date, dep_time FROM Flight WHERE num = %s AND dep_date = %s AND dep_time = %s", (flight_num, datetime.strptime(dep_date,'%Y-%m-%d'), dep_time ))
        check = cursor.fetchall()
        print(check, file = sys.stderr)
        
        # Inserting data into the database
        try:
            if (len(check) == 0 ):
                if(dep_date<arr_date or (dep_date==arr_date and dep_time<arr_time)):
                    if(dep_airport != arr_airport):
                        insert_query = """
                            INSERT INTO Flight (num, dep_date, dep_time, arr_time, arr_date, base_price, airplane_id, airline_name, dep_airport, arr_airport, status)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """
                        cursor.execute(insert_query, (flight_num, dep_date, dep_time, arr_time, arr_date, base_price, airplane_id, session["airline"], dep_airport, arr_airport, status))
                        conn.commit()

                        max_id_query =  """
                                        SELECT MAX(id) FROM Ticket
                                        """
                        cursor.execute(max_id_query)
                        max_id = cursor.fetchall()[0][0]
                        print(max_id, file=sys.stderr)
                        num_seats_query =   """
                                            SELECT num_of_seats FROM Airplane WHERE id = %s
                                            """
                        cursor.execute(num_seats_query, (airplane_id, ))
                        num_seats = cursor.fetchall()[0][0]
                        # ticket creation
                        query = """
                                INSERT INTO Ticket (id, price, flight_num, flight_dep_date, flight_dep_time, airline_name)
                                VALUES(%s, %s, %s, %s, %s, %s)
                                """
                        print(num_seats, file=sys.stderr)
                        if(max_id == None):
                            max_id = 0
                        for i in range(max_id+1, max_id+1+num_seats): 
                            cursor.execute(query, (i, base_price, flight_num, dep_date, dep_time, session["airline"]))
                            conn.commit()

                    else:
                        raise Exception("Arrival and departure airports must be different.")
                else:
                    raise Exception("Departure must be before arrival.")
            else: 
                raise Exception("Flight Already in Flights")
        except Exception as e:
            conn.rollback()
            cursor.close()
            conn.close()
            flash("Invalid data, flight not added. "+str(e))
            return redirect(url_for('create'))
        else:
            flash("Flight successfully added.")
        finally:
            cursor.close()
            conn.close()

    # If the method is not POST, redirect to the airline staff home page
    return redirect(url_for('staffhome'))

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

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM Airplane;")
        ids = cursor.fetchall()
        # Inserting data into the database
        try:
            if((int(airplane_id),) not in ids):
                if(datetime.strptime(manufacture_date, '%Y-%m-%d')<datetime.now()):
                    insert_query = """
                        INSERT INTO Airplane (id, num_of_seats, manufacturer, model_num, manufacture_date, age, airline_name)
                        VALUES (%s, %s, %s, %s, %s, %s, %s);
                    """
                    cursor.execute(insert_query, (airplane_id, num_of_seats, manufacturer, model_num, manufacture_date, age, session['airline']))
                    conn.commit()
                else:
                    raise Exception("Invalid manufacture date.")
            else:
                raise Exception("Airplane ID must be unique.")
        except Exception as e:
            conn.rollback()
            cursor.close()
            conn.close()
            flash("Invalid data, airplane not registered. "+str(e))
        else:
            flash("Airplane successfully registered.")
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

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT code FROM Airport;")
        codes = cursor.fetchall()
        # Inserting data into the database
        try:
            if((code,) not in codes):
                if(len(code) == 3 and code.isalpha()):
                    insert_query = """
                        INSERT INTO Airport (code, name, city, country, num_of_terminals, type)
                        VALUES (%s, %s, %s, %s, %s, %s);
                    """
                    cursor.execute(insert_query, (code, name, city, country, num_of_term, airport_type))
                    conn.commit()
                else:
                    raise Exception("Invalid airport code.")
            else:
                raise Exception("Code must be unique.")
        except Exception as e:
            conn.rollback()
            cursor.close()
            conn.close()
            flash("Invalid data, airport not registered. "+str(e))
        else:
            flash("Airport successfully registered.")
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
            if(datetime.strptime(start_date, "%Y-%m-%d")>datetime.now() and (datetime.strptime(start_date, "%Y-%m-%d")<datetime.strptime(end_date, "%Y-%m-%d") or (datetime.strptime(start_date, "%Y-%m-%d")==datetime.strptime(end_date, "%Y-%m-%d") and datetime.strptime(start_time, "%H:%M")<datetime.strptime(end_time, "%H:%M")))):
                insert_query = """
                    INSERT INTO Maintenance (start_date, start_time, end_date, end_time, airplane_id)
                    VALUES (%s, %s, %s, %s, %s);
                """
                cursor.execute(insert_query, (start_date, start_time, end_date, end_time, airplane_id))
                conn.commit()
            else:
                raise Exception("Please enter valid dates.")
        except Exception as e:
            conn.rollback()
            cursor.close()
            conn.close()
            flash("Invalid data, maintenance not scheduled. "+str(e))
        else:
            flash("Maintenance successfully scheduled.")
        finally:
            cursor.close()
            conn.close()

    # If the method is not POST, redirect to the airline staff home page
    return redirect(url_for('create'))

def get_total_revenue():
    conn = get_db_connection()
    cursor = conn.cursor()

    last_month_revenue = 0
    last_year_revenue = 0

    try:
        # Query for last month's revenue
        query = "SELECT SUM(Ticket.price) FROM PurchaseHistory JOIN Ticket ON PurchaseHistory.ticket_id = Ticket.id WHERE PurchaseHistory.purchase_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH) AND Ticket.airline_name = %s"
        cursor.execute(query, (session['airline'],))
        result = cursor.fetchone()
        last_month_revenue = result[0] if result else 0

        # Clearing the result of the first query
        cursor.fetchall()

        # Query for last year's revenue
        cursor.execute("SELECT SUM(Ticket.price) FROM PurchaseHistory JOIN Ticket ON PurchaseHistory.ticket_id = Ticket.id WHERE PurchaseHistory.purchase_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR) AND Ticket.airline_name = %s", (session['airline'],))
        result = cursor.fetchone()
        last_year_revenue = result[0] if result else 0

    except mysql.connector.Error as err:
        print("Error occurred: {}".format(err))
    finally:
        cursor.close()
        conn.close()

    return last_month_revenue, last_year_revenue

def get_frequent_customer():
    conn = get_db_connection()
    cursor = conn.cursor()


    # Adjust this query to find the most frequent flying customer
    cursor.execute("SELECT Customer.first_name, Customer.last_name, COUNT(*) FROM purchasehistory JOIN Customer JOIN Ticket ON PurchaseHistory.customer_email = Customer.email AND Ticket.customer_email = purchasehistory.customer_email WHERE airline_name = %s AND purchase_date >= CURDATE() - INTERVAL 1 YEAR GROUP BY purchasehistory.customer_email ORDER BY COUNT(*) DESC LIMIT 1", (session['airline'],))
    frequent_customer = cursor.fetchone()

    cursor.close()
    conn.close()
    return frequent_customer

@app.route('/search_customer_flights', methods=['POST'])
def search_customer_flights():
    customer_email = request.form.get('customer_email')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT airline_name FROM airlinestaff WHERE username = %s"
    cursor.execute(query, (session['username'], ))
    airline_name = cursor.fetchone()[0]


    # Now, get the flights for the customer on the same airline
    cursor.execute("""
        SELECT * FROM Flight
        JOIN Ticket ON Flight.num = Ticket.flight_num
        WHERE Ticket.customer_email = %s AND Flight.airline_name = %s )
    """, (customer_email, session['airline']))
    flights = cursor.fetchall()

    cursor.close()
    conn.close()

    print(session['airline'])
    print(customer_email)

    return render_template('customer_flights_result.html', flights=flights, airline_name = session['airline'], customer_email=customer_email)

@app.route('/staffstats')
def staff_stats():
    last_month_revenue, last_year_revenue = get_total_revenue()
    frequent_customer = get_frequent_customer()


    conn = get_db_connection()
    cursor = conn.cursor()


    # Adjusted query to fetch flights with ratings and comments
    cursor.execute("""
        SELECT 
            Flight.num AS FlightNumber,
            AVG(Reviews.rating) OVER (PARTITION BY Flight.num) AS AverageRating,
            Reviews.customer_email,
            Reviews.flight_num,
            Reviews.rating AS IndividualRating,
            Reviews.comment AS ReviewComment,
            Reviews.dep_date,
            Reviews.dep_time,
            Reviews.airline_name
        FROM 
            Flight
        JOIN 
            Reviews ON Flight.num = Reviews.flight_num
        WHERE
            Flight.airline_name = %s
        ORDER BY 
            Flight.num, Reviews.dep_date, Reviews.dep_time
    """, (session['airline'],))
    flights_with_ratings = cursor.fetchall()

    cursor.close()
    conn.close()

    # Render the staffstats.html template with the gathered data
    return render_template('staffstats.html', 
                           last_month_revenue=last_month_revenue, 
                           last_year_revenue=last_year_revenue, 
                           frequent_customer=frequent_customer, 
                           flights_with_ratings=flights_with_ratings)

if __name__ == '__main__':
    app.run(debug=True)
