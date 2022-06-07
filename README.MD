# Instagram Clone
### ROSELINE AKINYI

## Table of Content
+ [Description](#description)
+ [Installation Requirement]( Requisites)
+ [Technology Used](technology-used)
+ [Live links](#Live links)
+ [Reference](#reference)
+ [Licence](#licence)
+ [Authors Info](#aut)

## Description
A social media app that allows users to create account, upload photos, update their profile, like and comment on posts
## Technology Used
* [Python3.6](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)
## Requirements
* A stable internet connection
## User Story
* View different photos that interest them
* Click a single image to expand it and view the details of that photo
* Copy a link to the photo to share with my friends.
* Search for different categories
* View photos based on the location they were taken.
## set up instruction and installation
To get to this project
 1. clone this repository to a folder https://github.com/rossyvee/portfolio-website
 2. Extract the cloned file and install requirements
* cd the folder then open the portfolio-website
* pip install -r requirements.txt
  3. Export configurations
  4. python3 -m venv virtual --without-pip
  5. Activate the virtual environment source virtual/bin/activate
# Running the application locally

source virtual/bin/activate

pip install -r requirements.txt

Set Up your database User,Password, Host then make migrate

# Make migrations
python manage.py makemigrations photogallery
python manage.py migrate 

# Run the application
python manage.py runserver
Open the application on your browser 127.0.0.1:8000

## Bugs
The uploading images is not showing the images properly
  ## Licence
MIT License
Copyright (c) [2022] [Roseline Akinyi] 
Permission is  granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE
## Authors Info
Slack Profile - Rose Akinyi.

LinkedIn - (Roseline Akinyi: https://www.linkedin.com/in/roseline-akinyi-065875895/)

Email - roseakinyi001@gmail.com


`