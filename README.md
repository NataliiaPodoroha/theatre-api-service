# Theatre Service API Service

The Theater API Service is a Django-based RESTful API for managing plays, performances, actors, and more in the theater service. It offers endpoints for creation, updating and retrieval of theater-related data, as well as user registration and order management.

### Features:

* Creating plays with genres and actors
* Ability to add an image to plays
* Creating theatre halls
* Creating performances with show time, play and theatre hall
* Filtering plays and performances
* Managing reservations and tickets
* Ticket validation based on cargo and seat availability.
* JWT authentication for users.
* Documentation is located at: </api/doc/swagger/>, </api/doc/redoc/>


## Installation

1. Clone the repository:

   ```
   git clone https://github.com/PodorogaNatalia/theatre-api-service
   ```
2. Create .env file and define environmental variables following .env.sample

3. Install Docker on your machine.
   
4. Run command:
   ```
   docker-compose up --build
   ```
5. You should use such localhost for you app: ```127.0.0.1:8000```


## Service has next endpoints:
   ```
   "theatre" : 
                "http://127.0.0.1:8000/api/theatre/genres/"
                "http://127.0.0.1:8000/api/theatre/actors/"
                "http://127.0.0.1:8000/api/theatre/plays/"
                "http://127.0.0.1:8000/api/theatre/theatre_halls/"
                "http://127.0.0.1:8000/api/theatre/performances/"
                "http://127.0.0.1:8000/api/theatre/reservations/"
   "user" : 
                   "http://127.0.0.1:8000/api/user/register/"
                   "http://127.0.0.1:8000/api/user/me/"
                   "http://127.0.0.1:8000/api/user/token/"
                   "http://127.0.0.1:8000/api/user/token/refresh/"
   "documentation": 
                   "http://127.0.0.1:8000/api/doc/"
                   "http://127.0.0.1:8000/api/swagger/"
                   "http://127.0.0.1:8000/api/redoc/"
   ```

## Schema
![db.png](db.png)


## Screenshots of the project
![endpoints.png](endpoints.png)

![swagger1.png](swagger1.png)

![swagger2.png](swagger2.png)