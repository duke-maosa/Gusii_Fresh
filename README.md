# Gusii Fresh

Gusii Fresh is an e-commerce platform dedicated to providing the freshest produce from Kisii, Kenya, directly to your doorstep. This README file will guide you through the setup, installation, and running of the project.

![Gusii Fresh](path/to/your/image.jpeg/png)

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

Gusii Fresh is an online marketplace aimed at connecting local farmers with customers seeking fresh produce. The platform offers a range of products, easy navigation, secure payment options, and a seamless shopping experience.

## Features

- User authentication and profile management
- Product listing and categorization
- Shopping cart and order processing
- Search functionality
- Review and rating system
- Notifications and alerts
- Secure payments integration

## Screenshots

### Home Page
![Home Page](media/GHF%20page/homepage.png)

### Product Page
![Product Page](media/GHF%20page/product-list.png)

### Cart Page
![Cart Page](media/GHF%20page/check-out.png)

### Login Page
![Log In](media/GHF%20page/login.png)

### Edit Profile
![Edit Profile](media/GHF%20page/change-password.png)



## Technologies Used

- Django 5.0.6
- HTML, CSS, JavaScript
- Bootstrap 4
- SQLite (default database)
- Crispy Forms
- Allauth for authentication

## Prerequisites

Ensure you have the following installed on your local development environment:

- Python 3.8+
- Django 5.0.6
- pip (Python package installer)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/duke-maosa/Gusii_Fresh.git
    cd Gusii_Fresh
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Collect static files:

    ```bash
    python manage.py collectstatic
    ```

## Running the Application

1. Start the development server:

    ```bash
    python manage.py runserver
    ```

2. Open your web browser and navigate to `http://127.0.0.1:8000`.

## Project Structure

```plaintext
Gusii_Fresh/
├── account/
├── analytics/
├── cart/
├── home/
├── marketing/
├── notifications/
├── orders/
├── payments/
├── products/
├── reviews/
├── search/
├── security/
├── static/
├── support/
├── templates/
├── manage.py
└── requirements.txt



Open your browser and navigate to http://127.0.0.1:8000 to view the application.

Configuration
settings.py
Ensure your settings.py is properly configured with the following settings:
SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

LOGIN_REDIRECT_URL = '/account/profile/'
LOGOUT_REDIRECT_URL = '/home/'
AUTH_USER_MODEL = 'account.CustomUser'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SITE_ID = 1
Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a Pull Request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Thank you for using Gusii Fresh! If you have any questions, feel free to contact us at dukemaosa75@gmail.com.

