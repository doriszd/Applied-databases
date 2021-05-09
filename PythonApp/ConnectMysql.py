# importing pymysql
import pymysql

conn = None   
# connecting to "world" database
def connect():   
    global conn   
    
    # entering my own credentials
    conn = pymysql.connect(host="localhost", user="root", password="321bobi321", db="world", cursorclass=pymysql.cursors.DictCursor)

# function to define first choice in the menu - View people
def view_people():

# if there is no connection, connect
    if (not conn):
        print("No connection")
        connect()
        
# sql query - selecting everything from person table in world database       
    sql = "SELECT * from person" 
    
# activating and executing sql command   
    with conn: 
        cursor = conn.cursor() 
        cursor.execute(sql)  
        
# while loop: getting the results in size of 2        
    while True:
        person = cursor.fetchmany(2)
        # if there are no more rows to show print ("There are no more people to show.")
        if not person:
            print("There are no more people to show.")
            # break the loop
            break
        # for each row (data) in person table  print personId, personname, age
        for x in person:
            print(x["personID"], "|", x["personname"], "|", x["age"])
        # user will be asked to press any key on the board
        q = input("-- Quit == <q>") 
        # if the user input is q print below message and break out of loop
        if q == "q": 
            print("Return to main menu")
            break 
                

# function to define second choice in the menu - Independence year
def independence_year(year):

# if there is no connection, connect
    if (not conn):
        connect()
        
# sql query - selecting data from country table      
    sql = """
        select Name, IndepYear, Continent, Population
        from country
        where IndepYear = %s
        """
    
# activating and executing sql command   
    with conn: 
        try:
        
            cursor = conn.cursor() 
            cursor.execute(sql, year)  
            return cursor.fetchall() 
         # error exception - Integrity error
        except pymysql.IntegrityError as e:
            print(e)
        # error exception - Internal error
        except pymysql.InternalError as e:
            print(e)      
        # other exceptions
        except Exception as e:
            print("Error - please try again.", e)

# function to define third choice in the menu - adding name and age
def add_your_name(name,age):

# if there is no connection, connect
    if (not conn):
        connect()
        
# sql query - selecting data from country table      
    sql = """
        INSERT INTO person
        (personname, age) 
        VALUES (%s, %s)
        """
    
# activating and executing sql command   
    with conn: 
        try:
        
            cursor = conn.cursor() 
            cursor.execute(sql, (name,age))  
            return cursor.fetchall() 
         # error exception - Integrity error
        except pymysql.IntegrityError as e:
            print("***Error***:" ,name, "already exists")
        # error exception - Internal error
        except pymysql.InternalError as e:
            print(e)      
       
# function to define fourth choice in the menu - country by name   
def country_by_name(country):     

# if there is no connection, connect
    if (not conn):
        connect()
        
# sql query - selecting data from country table      
    sql = """
            SELECT Name, Continent, Population, HeadOfState from country
            where Name like %s       
            """              
    
# activating and executing sql command   
    with conn: 
        try:
        
            cursor = conn.cursor() 
            cursor.execute(sql, ("%"+country+"%")) 
            return cursor.fetchall() 
         # error exception - Integrity error
        except pymysql.IntegrityError as e:
            print(e)
        # error exception - Internal error
        except pymysql.InternalError as e:
            print(e)        
            
            
# function to define fifth choice in the menu - Icountries by population         
def countries_by_pop(symbol, population):     

# if there is no connection, connect
    if (not conn):
        connect()
        
# sql query - selecting data from country table      
    sql = "SELECT * from country"                 
    
# activating and executing sql command   
    with conn: 
        try:
        
            cursor = conn.cursor() 
            cursor.execute(sql)
            return cursor.fetchall() 
         # error exception - Integrity error
        except pymysql.IntegrityError as e:
            print(e)
        # error exception - Internal error
        except pymysql.InternalError as e:
            print(e)     
        except Exception as e:
            print("other error", e)
            