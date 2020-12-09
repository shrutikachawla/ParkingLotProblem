## ParkingLotProblem

#### Shrutika Chawla 
##### shrutikachawla.96@gmail.com


### Class Diagrams:

***************************
         CAR             
   regno : String (PK)      
   color : String        
   status : String       
   slot : Integer        
   level : Integer       
   createdAt : DateTime  
***************************

***************************
         TICKET          
   carID : String (FK)    
   slotAllotted: String  
   ticketNo : String (PK)     
***************************

***************************
         DEVICE          
   id : String (PK)    
   name: String (Unique)  
   password : String     
***************************

### Tests:

#### Parking:
* If an unauthorized user is trying to park the car, error is thrown.
* If registration no. of car received is not present in db, error is thrown.
* If registration no. of car exists, and slot no. has an entry other than 100, car is already parked and error should be thrown
* If registration no. of car exists, and slot and level fields have value 100, create an entry in Ticket table with min possible slot, and update slot and level values for the given regn. no.

#### Leaving:
* If an unauthorized user is trying to park the car, error is thrown.
* If ticket no. of car received is not present in db, error is thrown.
* If ticket no. of car exists, and slotAllotted has an entry 00, car has already been taken away and error should be thrown.
* If ticket no. of car exists, and slotAllotted has a valid value, update Ticket and Car table for suitable fields


### API Documentation
* host_name/api/signup/ : accepts a JSON object (username & password) to register a device in the system
* host_name/api/login/ : accepts a JSON object (username & password) to sign in a device into the system for authorized parking
* host_name/api/home/ : lists all the cars present in db
* host_name/api/ticket : lists all the tickets issued from the system
* host_name/api/detail/?regno=123 : lists the car with the mentioned registration no.
* host_name/api/park/?regno=123 : parks the car and issues a ticket with a slot
* host_name/api/leave/?ticketNo=123 : makes the slot available mentioned in given ticket no. and updates Car table
* host_name/api/regNoByColor/?color=anycolor : fetches the registration no. of cars in mentioned color
* host_name/api/slotByReg/?regno=XXXXXX : fetches the slot no. of a car with mentioned registration no.
* host_name/api/slotByColor/?color=anycolor : fetches the slot numbers of all colors in mentioned color

### Problems faced
* Was unfamiliar with Django. Setting up the environment took quite a lot of time
* Took some time to understand the basic functioning in Django. Used my spring-boot knowledge to develop the APIs


### To run project 
-> git clone https://github.com/shrutikachawla/ParkingLotProblem.git
-> cd parkingLot
-> pip install -r requirements.txt
-> python manage.py migrate
-> python manage.py runserver
