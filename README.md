# Udacity Fullstack Nanodegree Project 5 - Item Catalog

The purpose of this project was to create a python web application which displays items 

This application demonstrates the following tools/technologies:

  1. python
  2. sqlalchemy
  3. flask web framework
  5. qauth2.0
  6. jinja2 templating
  
 
This project was done as part of the Udacity Fullstack Nanodegree program

###Required Libraries and Dependencies
1. vagrant
2. python
3. Google OAuth2 Web Application API Credentials and corresponding client_secrets.json file<br>
    Please see : https://developers.google.com/identity/protocols/OAuth2
4. Google account

###How to Run Project

1. Retrieve workspace: <br> ``` git clone https://github.com/kevinhutton/Udacity-Fullstack-Nanodegree-Project5.git ```
2. Navigate to "vagrant" folder: <br> ``` cd Udacity-Fullstack-Nanodegree-Project4/vagrant ```
3. Copy your client_secret.json file to within this folder (E.g. the vagrant folder)
4. Start vagrant VM: <br> ``` vagrant up ```
5. Log onto VM: <br> ``` vagrant ssh ```
6. Navigate to "catalog" folder: <br> ``` vagrant@vagrant-ubuntu-trusty-32:~$ cd /vagrant/catalog/ ```
7. Create database and tables: <br> ``` vagrant@vagrant-ubuntu-trusty-32:/vagrant/catalog$ python database_setup.py ```
8. Populate database with mock categories: <br> ``` vagrant@vagrant-ubuntu-trusty-32:/vagrant/catalog$ python database_generate_mock_data.py ```
9. Run application: <br> ``` vagrant@vagrant-ubuntu-trusty-32:/vagrant/catalog$ python project.py ```<br>
   This will launch the application on http://localhost:5000
