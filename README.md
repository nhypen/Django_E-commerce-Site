# Django E-commerce Site

## Description

Django E-commerce Site is a simple online store built with Python and Django. The application allows users to browse products, view product details, add products to a shopping cart, and place orders. Products and orders are stored in a SQLite database and managed through Django's built-in administration panel.

This project was created as a portfolio project to practice Django fundamentals such as models, views, templates, forms, URL routing, and database operations.

---

## Features

* Product catalog
* Product detail pages
* Shopping cart
* Order creation
* SQLite database
* Django Admin Panel
* Product management
* Order management
* Responsive and simple user interface

---

## Technologies Used

* Python 3
* Django 4.2
* SQLite3
* HTML5
* CSS3

---

## Project Structure

```text
django_ecommerce/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
│
├── ecommerce/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── shop/
    ├── admin.py
    ├── apps.py
    ├── cart.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    │
    └── templates/
        └── shop/
            ├── base.html
            ├── product_list.html
            ├── product_detail.html
            ├── cart.html
            ├── checkout.html
            └── order_success.html
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/django-ecommerce-site.git
cd django-ecommerce-site
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Create administrator account:

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

Open in browser:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

---

## Learning Objectives

This project demonstrates:

* Django Models
* Django Views
* Django Templates
* URL Routing
* Form Handling
* Session-Based Cart
* Database Relationships
* Django Administration Panel
* CRUD Operations

---

## Author
nhypen

Portfolio project created for learning Django and backend web development.
