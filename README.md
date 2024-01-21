# RatioAPI - Kubernetes Deployment
 
This project includes a Flask and a Swagger UI-based API based on SQLAlchemy that are used to view and add user data. It includes the ability to write CSV files to the database created with SQLite and read this data.
 
## PURPOSE OF THE PROJECT
The project is a backend project written in Flask. There is a database that has already been created in SQLite and there are name and email columns in it, the user can perform GET and POST operations in the Swagger UI interface, which he accesses via the http://20.81.21.248:5000/ URL. With the GET operation, the user can view the records in the database, add the cvs extension files on the user's computer with POST, and if the column names of the csv file he added are name and email, he automatically adds the records in this csv file to the database, if the column names do not match, the error message is displayed on the screen.
 
### Transactions
 
1. With Flask, the necessary codes in the backend were written in the database.py file and connected to the database.
 
 2.The Docker container has been created and the necessary libraries have been added in the requriments.txt file.
 
3. The created container was dumped into the docker hub environment.
 
4. Install az cli to deploy in Microsoft Azure
 
5. A resource group named ratio-api_rg was created in Azure and a Kubernetes Service named ratio-api-aks was created.
 
6. Necessary adjustments have been made to the YAML file named deployement.yaml.
 
 7.Deployement has been implemented into Kubernetes.
 
8.For the test of the application, the pods name was looked at and the loadbalancer IP was found and it started broadcasting to the outside world from port 5000.
 
9. Also, you can take a look at http://20.81.21.248:5000/ to start using the API.
 
## Project Information: 
 
Libraries Used: Flask>=2.1.1,Werkzeug>=2.0.1,Flask-RESTx>=0.1.1,Flask-SQLAlchemy>=3.0.2
 
Language Used: Python(Flask)
 
