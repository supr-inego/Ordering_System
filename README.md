# Ordering System (Django REST Framework)

This project is a simple **Ordering System** made using **Django** and **Django REST Framework (DRF)**.
It follows our ERD that we created.

The system allows managing:

* Customers
* Products
* Orders
* Order Items

---

## Features

* Create customers and products
* Create orders with order items
* View lists of customers, products, and orders
* Delete orders
* Update orders (bonus)

---

## Technologies Used

* Python
* Django
* Django REST Framework
* SQLite

---

## Project Structure

```
ordering_system/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── orders/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views_api.py
│   └── urls_api.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── venv/
```

---

## Models Used

* **Customer** – name, email
* **Product** – name, current_price
* **Order** – customer, created_at
* **OrderItem** – order, product, quantity, unit_price

---

## API Endpoints

* `/api/customers/`
* `/api/products/`
* `/api/orders/`
* `/api/orders/<id>/`

Allowed methods:

* GET
* POST
* PUT (bonus)
* DELETE

---

## How to Run the Project

1. Activate virtual environment:

```bash
venv\Scripts\activate
```

2. Install requirements:

```bash
pip install -r requirements.txt
```

3. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Run server:

```bash
python manage.py runserver
```

5. Open browser:

```
http://127.0.0.1:8000/api/
```

---

## Notes

* Orders support multiple items using JSON input
* Django REST Framework browsable API is used for testing

---

## Author

Cyril Iñego Dayak
Poging 3rd-Year IT Student
