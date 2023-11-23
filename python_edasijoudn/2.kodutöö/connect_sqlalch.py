from sqlalchemy import create_engine
from sqlalchemy import *
from datetime import time

engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

provider = Table(
   'provider', meta, 
   Column('id', Integer, primary_key=True), 
   Column('name', String), 
)

canteen = Table(
   'canteen', meta, 
   Column('id', Integer, primary_key=True), 
   Column('provider_id', Integer, ForeignKey('provider.id'), nullable=False),
   Column('name', String), 
   Column('location', String), 
   Column('day', String), 
   Column('open', Time), 
   Column('close', Time), 
)

meta.create_all(engine)

conn = engine.connect()

conn.execute(provider.insert(), [
   {'name' : "Rahva Toit"},
   {'name' : "Baltic Restaurants Estonia AS"},
   {'name' : "TTÜ Sport"},
   {'name' : "Kohvik"},
])

conn.execute(canteen.insert(), [
   {'provider_id' : 1, 'name': "Economics Canteen", 'location': "Akadeemia tee 3", "day": "Mon-Fri", "open": time.fromisoformat("08:30:00"), "close": time.fromisoformat("18:30:00") },
   {'provider_id' : 1, 'name': "Library Canteen", 'location': "Ehitajate tee 1", "day": "Mon-Fri", "open": time.fromisoformat("08:30:00"), "close": time.fromisoformat("19:00:00") },
   {'provider_id' : 2, 'name': "Deli Cafe", 'location': "Ehitajate tee 5", "day": "Mon-Fri", "open": time.fromisoformat("09:00:00"), "close": time.fromisoformat("16:00:00") },
   {'provider_id' : 2, 'name': "Daily", 'location': "Ehitajate tee 5", "day": "Mon-Fri", "open": time.fromisoformat("09:00:00"), "close": time.fromisoformat("16:00:00") },
   {'provider_id' : 1, 'name': "U06 Canteen", 'location': "U06", "day": "Mon-Fri", "open": time.fromisoformat("09:00:00"), "close": time.fromisoformat("16:00:00") },
   {'provider_id' : 2, 'name': "Natural Science Building canteen", 'location': "Akadeemia tee 15", "day": "Mon-Fri", "open": time.fromisoformat("09:00:00"), "close": time.fromisoformat("16:00:00") },

   {'provider_id' : 2, 'name': "ICT canteen", 'location': "Raja 15", "day": "Mon-Fri", "open": time.fromisoformat("09:00:00"), "close": time.fromisoformat("16:00:00") },
   {'provider_id' : 3, 'name': "Sports building canteen", 'location': "Männiliiva 7", "day": "Mon-Fri", "open": time.fromisoformat("11:00:00"), "close": time.fromisoformat("20:00:00") },
])


conn.commit()

### Selecting ### 
select1 = canteen.select().where(canteen.c.open<= time.fromisoformat("16:15:00"), canteen.c.close >= time.fromisoformat("18:00:00"))

select2 = select1.join(provider, canteen.c.provider_id == provider.c.id).where(provider.c.name == 'Rahva Toit')

conn = engine.connect()
result1 = conn.execute(select1)
result2 = conn.execute(select2)

#Printing out result of select1
for row in result1:
   print (row[2])

#Printing out result of select2
for row in result2:
   print(row[2])
        

conn.close()
