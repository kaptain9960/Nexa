# Nexa Fashion House

Nexa Fashion House is a modern web-based fashion platform built with **Django**. It showcases stylish collections, manages products, and allows customers to explore the brand online. The system features an admin dashboard for managing content, ensuring smooth operations and an elegant user experience.

---

## Table of Contents

- [About the Project](#about-the-project)  
- [Features](#features)  
- [Technologies Used](#technologies-used)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [License](#license)

---

## About the Project

Nexa Fashion House is designed to help fashion businesses present their products elegantly and manage them efficiently. It allows admins to upload collections, manage portfolios, and maintain an interactive website for customers.  

Key highlights:  

- Modern, responsive web interface  
- Admin dashboard for product and portfolio management  
- Portfolio and service detail pages  
- Resume download functionality for professional profiles  
- Static assets handling (CSS, JS, images)  
- Built with Django and SQLite for simplicity and scalability

---

## Features

- **User Interface**: Clean and responsive UI for seamless browsing.  
- **Portfolio Management**: Showcase fashion collections with detail pages.  
- **Services Management**: Present available fashion services.  
- **Resume Download**: Download profile/resume directly from the site.  
- **Admin Dashboard**: Add, update, and delete products, portfolios, and services.  
- **Static Files Handling**: Images, CSS, and JS included for full styling.

---

## Technologies Used

- **Backend**: Python 3.12, Django 4.x  
- **Database**: SQLite  
- **Frontend**: HTML, CSS, JavaScript, Bootstrap (or your CSS framework)  
- **Version Control**: Git, GitHub  
- **Virtual Environment**: venv  

---

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:

```bash
git clone https://github.com/kaptain9960/Nexa.git
cd Nexa

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate    # Windows

Install dependencies:

pip install -r requirements.txt

Apply migrations:

python manage.py makemigrations
python manage.py migrate

Create a superuser:

python manage.py createsuperuser

Run the development server:

python manage.py runserver

Open your browser and go to:

http://127.0.0.1:8000/
Usage

Navigate the homepage to see featured portfolios and services.

Click on portfolio or service details to view more information.

Admin users can log in at /admin/ to manage content.

Project Structure
Nexa/
│
├── Nexa/                  # Django project folder
│   ├── settings.py        # Project settings
│   ├── urls.py            # URL configuration
│   ├── wsgi.py
│   └── asgi.py
│
├── core/                  # Main app folder
│   ├── views.py           # View functions
│   ├── urls.py            # App URLs
│   ├── models.py          # Database models
│   ├── templates/         # HTML templates
│   └── static/            # CSS, JS, images
│
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── README.md
Contributing

Contributions are welcome! Please follow these steps:

Fork the repository.

Create a new branch: git checkout -b feature/YourFeature.

Commit your changes: git commit -m "Add feature".

Push to the branch: git push origin feature/YourFeature.

Create a Pull Request.

License

This project is open-source and available under the MIT License.