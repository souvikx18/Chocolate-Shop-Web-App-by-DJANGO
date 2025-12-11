# 🍫 Chocolate-Shop-Web-App-by-DJANGO

A fully functional Chocolate Shop Web Application built using Django, featuring product listings, shopping cart components, order UI, and clean templates.
This project is ideal for learning Django's MVC (MVT) architecture while building a real-world web application.


🚀 Features-----
🛍️ Display chocolates and product categories
📄 Dynamic pages rendered with Django Templates
🎨 Static files integrated (CSS, images, JS)
🗂️ Database-backed product entries (SQLite)
🧱 Django project structured into reusable apps (Home, Hello)
⚙️ Easy to set up and run locally


🛠️ Tech Stack--
-----------------------------------------
| Component | Technology                |
| --------- | ------------------------- |
| Backend   | Django (Python)           |
| Frontend  | HTML, CSS                 |
| Database  | SQLite                    |
| Server    | Django Development Server |
-----------------------------------------


📁 Project Structure--
Chocolate-Shop-Web-App-by-DJANGO/
│
├── Hello/                         # Main Django project folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                # Global Django settings
│   ├── urls.py                    # Root URL configuration
│   └── wsgi.py
│
├── home/                          # Django App (Handles pages/views)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py                  # Database models
│   ├── tests.py
│   ├── urls.py                    # App-level URL routes
│   └── views.py                   # All view functions
│
├── static/                        # Static assets (images, CSS, JS)
│   └── img/
│       ├── chocolate_img.jpeg
│       ├── chocolate_tray_img.jpeg
│       ├── chocolate1.avif
│       ├── chocolate2.avif
│       ├── chocolate3.avif
│       ├── chocolate4.avif
│       ├── chocolate5.avif
│       ├── chocolate6.avif
│       ├── chocolate7.avif
│       ├── chocolate8.avif
│       ├── chocolate9.avif
│       ├── contact.avif.jpg
│       └── shop_img.jpeg
│
├── templates/                     # HTML templates for frontend
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── services.html
│   └── contact.html
│
├── db.sqlite3                     # Main database file
├── db.sqlite3.backup              # Backup database
├── manage.py                      # Django command-line utility
└── README.md

⚙️ Installation & Setup--
1️⃣ Clone the repository-
git clone https://github.com/souvikx18/Chocolate-Shop-Web-App-by-DJANGO.git
cd Chocolate-Shop-Web-App-by-DJANGO

2️⃣ Create & activate a virtual environment-
python -m venv venv
venv\Scripts\activate    # Windows
# or
source venv/bin/activate # Mac / Linux

3️⃣ Install dependencies-
pip install django

4️⃣ Run migrations (if needed)-
python manage.py migrate

5️⃣ Start the development server-
python manage.py runserver

6️⃣ Open in browser-
http://127.0.0.1:8000/


🧠 How It Works----
Django routes URLs → views (views.py)
Views fetch data → pass to templates
Templates render dynamic pages
SQLite stores product information
Static files provide UI styling


📌 Future Enhancements---
🛒 Shopping cart with sessions
🔐 Login & Register system
💰 Online payment integration
⭐ Product ratings & reviews
📦 Admin dashboard for inventory


🤝 Contributing--
Pull requests are welcome!
For major changes, please open an issue first.
