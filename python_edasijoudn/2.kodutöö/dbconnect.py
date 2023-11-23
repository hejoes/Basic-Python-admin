import sqlite3

def opendb():
    global conn
    conn = sqlite3.connect('diners.db')
    print ("Opened database successfully")

def create_tables():
    #create a table in the previously created database
    conn.execute('''CREATE TABLE canteen (
                id INTEGER PRIMARY KEY NOT NULL,
                provider_id INTEGER NOT NULL,
                name VARCHAR(40) NOT NULL,
                location VARCHAR(50) NOT NULL,
                day VARCHAR(30),
                open TIME,
                close TIME,
                FOREIGN KEY(provider_id) REFERENCES provider(id)
                )''')

    conn.execute('''CREATE TABLE provider (
                id INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL
                )''')
                         
    
def createRecords():
    """
    create some records in the provider table
    """
    conn.execute("INSERT INTO provider (id, name) \
                 VALUES (1, 'Rahva Toit')");
    conn.execute("INSERT INTO provider (id, name) \
                 VALUES (2, 'Baltic Restaurants Estonia AS')");
    conn.execute("INSERT INTO provider (id, name) \
                 VALUES (3, 'TTÜ Sport')");
    conn.execute("INSERT INTO provider (id, name) \
                 VALUES (4, 'Kohvik')");
   
   
    
    conn.execute("INSERT INTO canteen (id, provider_id, name, location, day, open, close) \
                 VALUES (1, 1, 'Economics canteen', 'Akadeemia tee 3', 'Mon-Fri', '08:30:00', '18:30:00')");
    
    conn.execute("INSERT INTO canteen (id, provider_id, name, location, day, open, close) \
                 VALUES (2, 1, 'Library canteen', 'Ehitajate tee 1', 'Mon-Fri', '08:30:00', '19:00:00')")

    conn.execute("INSERT INTO canteen (id, provider_id, name, location, day, open, close) \
                 VALUES (3, 2, 'Deli Cafe', 'Ehitajate tee 5', 'Mon-Fri', '09:00:00', '16:00:00')")

    conn.execute("INSERT INTO canteen (id, provider_id, name, location, day, open, close) \
                 VALUES (4, 2, 'Daily', 'Ehitajate tee 5', 'Mon-Fri', '09:00:00', '16:00:00')")

    conn.execute("INSERT INTO canteen (id, provider_id, name, location, day, open, close) \
                 VALUES (5, 1, 'U06 canteen', 'U06', 'Mon-Fri', '09:00:00', '16:00:00')")
    
    conn.execute("INSERT INTO canteen (id, provider_id, name, location, day, open, close) \
                 VALUES (6, 2, 'Natural Science building canteen', 'Akadeemia tee 15', 'Mon-Fri', '09:00:00', '16:00:00')")

    conn.execute("INSERT INTO canteen (id, provider_id, name, location, day, open, close) \
                 VALUES (7, 2, 'ICT canteen', 'Raja 15', 'Mon-Fri', '09:00:00', '16:00:00')")

    conn.execute("INSERT INTO canteen (id, provider_id, name, location, day, open, close) \
                 VALUES (8, 3, 'Sports building canteen', 'Männiliiva 7', 'Mon-Fri', '11:00:00', '20:00:00')")

    conn.commit()


def selectRecords():

    stm1 = conn.execute("SELECT name FROM canteen WHERE open <= '18:00:00' AND close >= '16:15:00'")
    for name in stm1:
       print(name)
       
    stm2 = conn.execute("SELECT canteen.name FROM canteen JOIN provider ON canteen.provider_id = provider.id WHERE provider.name = 'Rahva Toit'")
    for provider in stm2:
        print(provider)

def closeconn():
    """
    close connection
    """
    conn.close()
    print ("Connection closed")
    

if __name__ == "__main__":
    opendb()
    create_tables()
    createRecords()
    selectRecords()
    # delRecords()
    #closeconn()