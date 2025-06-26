# ShopNow

ShopNow is a Django-based e-commerce project designed to provide a streamlined shopping experience. It features user authentication, customizable user accounts, and a modern, responsive frontend for product display and interaction.

## Features

- **User Authentication:** Custom user model with registration, email verification, login, and password reset functionality.
- **Responsive UI:** Modern home page and product sections, built with Django templates and static files.
- **Admin Interface:** Utilizes Django’s built-in admin for managing users and products, enhanced with additional JavaScript and CSS for better usability.
- **Static & Media Files Management:** Configured to serve static assets and user-uploaded media using Django and WhiteNoise.
- **Extensible Structure:** Designed for easy addition of new apps/modules.

## Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript (with Django templating)
- **Database:** SQLite (default, can be configured)
- **Other:** WhiteNoise for static files, Font Awesome for icons

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package installer)
- Virtualenv (recommended)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/pradeepxvi/shopnow.git
    cd shopnow
    ```

2. **Set up a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the app:**
    Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Project Structure

```
shopnow/
├── accounts/              # Custom user app (models, views, urls)
├── GreatKart/             # Django project settings and URLs
├── staticfiles/           # Static assets (admin CSS, JS, icons, etc.)
├── templates/             # HTML templates (home, registration, etc.)
├── manage.py              # Django entry point
└── requirements.txt       # Python dependencies
```

## Configuration

- **Static Files:** Served via WhiteNoise in production.
- **Media Files:** Uploaded content stored in `/media/`.
- **Email:** SMTP settings are present in `GreatKart/settings.py` for sending verification and reset emails.

## License

Some static files (icons, etc.) are licensed under MIT and SIL OFL. See `staticfiles/admin/img/README.txt` and `staticfiles/admin/img/LICENSE` for details.

## Contributing

Feel free to open issues or submit pull requests to improve this project.

## Contact

For questions or support, please contact the repository owner via [GitHub](https://github.com/pradeepxvi).
