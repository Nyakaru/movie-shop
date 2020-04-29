Movie Shop - Simple shop api with CRUD operations
=======

## How to setup and test the application
1. Install pip first using this command 

    `sudo apt-get install python3-pip`

1. Install virtualenv using pip3 `sudo pip3 install virtualenv `

1. Create a virtual environment `virtualenv venv `

1. Activate your virtual environment: `source venv/bin/activate`

1. Clone this repo with the following command:

    `git clone https://github.com/Nyakaru/movie-shop.git`

1. Cd into the movieshop directory:
    `cd movieshop`

1. Install the requirements by running the command:

      `pip install`

1. Create a database:
  In the terminal run the following after installing postgres and setting up:  
  
    `psql`
  `create DATABASE <name_of_your_database>`
1. Create a .env file in the project folder and and the following exports:  
   
   `export DATABASE="<name of your database>"`  
   
   `export USER="<your postgres username>"`  
   
   `export HOST="<localhost>"`
   
   `export PASSWORD="<your postgres password>"`
   
1. Export the settings by running the command: `source .env`

1. Migrate the database:
    
    `python manage.py makemigrations`
    
    `python manage.py migrate`
1. Run the server:
    
    `python manage.py runserver`
1. Access the endpoints via:
    1. Web browser(Swagger) - http://127.0.0.1:8000/docs/
    2. Postman - http://127.0.0.1:8000/api
