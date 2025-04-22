RTC Tracker Project
Overview
The RTC Tracker Project is designed to manage and track RTC (Record of Rights, Tenancy, and Crops) records for various districts, taluks, hoblis, and villages. The backend of the project exposes an API for retrieving and managing RTC records, while a frontend can be developed to provide a user interface for interacting with this data.

This repository contains the backend code implemented with Django and Django REST Framework, which provides RESTful API endpoints for managing RTC records.

Features
API endpoints to create, read, update, and delete RTC records.

Integration with a database (SQLite) to store and manage RTC records.

A scraper that fetches RTC data for specific years and stores it in the database.

User authentication (if implemented).

Table of Contents
Technologies Used

Project Setup

Installation

Usage

API Endpoints

Troubleshooting

Contributing

License

Technologies Used
Backend: Django, Django REST Framework

Database: SQLite (can be switched to other databases)

Python Version: 3.8+ (Recommended)

Libraries/Packages:

Django

Django REST Framework

SQLite

Project Setup
1. Clone the Repository
To get started with the project, first, clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/rtc-tracker.git
cd rtc-tracker
2. Set Up the Virtual Environment
It is recommended to create a virtual environment to manage project dependencies.

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install Required Dependencies
Once the virtual environment is activated, install the necessary dependencies from requirements.txt:

bash
Copy
Edit
pip install -r requirements.txt
Installation
1. Database Setup
Once the dependencies are installed, you need to set up the database by applying migrations. This will create the required database tables, including the RTC records table.

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
2. Create Superuser (Optional)
If you'd like to access the Django admin panel, you can create a superuser:

bash
Copy
Edit
python manage.py createsuperuser
Follow the prompts to set up your superuser account.

Usage
To start the development server and test the API, run the following command:

bash
Copy
Edit
python manage.py runserver
This will start the server at http://127.0.0.1:8000/.

You can now access the API endpoints and the admin panel (if you created a superuser) at the following URLs:

Admin Panel: http://127.0.0.1:8000/admin/

API: http://127.0.0.1:8000/api/

API Endpoints
Here are the available API endpoints for the RTC Tracker:

1. /api/rtc-records/ (GET, POST)
GET: Retrieve a list of all RTC records.

POST: Create a new RTC record.

Request Example (POST):

json
Copy
Edit
{
  "district": "District Name",
  "taluk": "Taluk Name",
  "hobli": "Hobli Name",
  "village": "Village Name",
  "survey_no": "1234",
  "hissa_no": "5678",
  "year": "2025"
}
2. /api/rtc-records/{id}/ (GET, PUT, DELETE)
GET: Retrieve details of a specific RTC record by ID.

PUT: Update an existing RTC record by ID.

DELETE: Delete a specific RTC record by ID.

3. /api/scrape/{year}/ (GET)
GET: Fetch RTC data for a specific year.

Troubleshooting
Common Issues
1. Database Table Missing:
If you encounter an error stating that a database table is missing (e.g., no such table: rtc_app_rtcrecord), it typically means that the migrations haven’t been applied successfully.

Solution:

Run python manage.py makemigrations followed by python manage.py migrate to apply all the necessary migrations.

2. Invalid Query Parameter:
If you get errors when querying the API, ensure that the URL parameters are correctly formatted. For example, when scraping data for a year, use the correct format:

swift
Copy
Edit
GET /api/scrape/2025/
Contributing
If you'd like to contribute to this project, please follow these steps:

Fork the repository.

Create a new branch for your changes (git checkout -b feature-branch).

Make your changes and commit them (git commit -am 'Add feature').

Push your branch (git push origin feature-branch).

Submit a pull request.

Please ensure that any contributions adhere to the coding standards of the project.

License
This project is licensed under the MIT License – see the LICENSE file for details.

Feel free to modify and expand the content as required! This README should help others to understand the project setup, usage, and contribute efficiently.
