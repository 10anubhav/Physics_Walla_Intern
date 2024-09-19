# Image-To-Text Convertor

### Overview
The "Image-to-Text Converter" is a web application that allows users to upload images and convert the text within those images into editable text. The application also includes additional features like converting JPG to Word, PDF to Word, and JPG to PDF, all integrated into a user-friendly interface with a navigation bar.

### Project Structure

```
Project/
├── db.sqlite3               # SQLite database file
├── intern/                  # Core app logic
│   ├── admin.py             # Admin panel configuration
│   ├── apps.py              # Application configuration
│   ├── migrations/          # Database migration files
│   ├── models.py            # Models that define the data structure
│   ├── templates/           # HTML templates for rendering the frontend
│   ├── tests.py             # Unit tests for the application
│   ├── urls.py              # URL routing for the application
│   ├── views.py             # Views that handle request and response logic
│   └── __init__.py          # App initialization file
├── manage.py                # Django management script
├── media/                   # Directory for user-uploaded media
└── Project/                 # Configuration for the Django project
```

### Features
- **Image to Text Conversion**: Upload an image and extract the text within it.
- **JPG to Word**: Convert JPG images to Word documents.
- **PDF to Word**: Convert PDF files to Word documents.
- **JPG to PDF**: Convert JPG images to PDF files.
- **Download Files**: Easily download files in any formats.
- **Django Framework**: The app is built using the Django web framework, leveraging its models, views, and template system.
- **SQLite Database**: The project uses an SQLite database (`db.sqlite3`) for data persistence.
- **User and Media Management**: Handles internal user operations and media uploads.

### Prerequisites
- Python 3.x
- Django
- Bootstrap (included via CDN)
- Tesseract-OCR (for text extraction)

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/10anubhav/Physics_Walla_Intern.git
   cd Project
   ```

2. **Install Dependencies**
   Ensure you have Python and `pip` installed, then install the required dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Tesseract-OCR**
   - Download and install Tesseract-OCR from [here]( https://github.com/tesseract-ocr/tesseract).
   - Make sure to add Tesseract to your system's PATH.

5. **Run Database Migrations**
   Before running the app, apply migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser (Optional)**
   If you want access to the Django admin panel, create a superuser account:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**
   Start the local Django development server:
   ```bash
   python manage.py runserver
   ```

   The app will be available at `http://127.0.0.1:8000/`.

### Testing
To run the tests:
```bash
python manage.py test
```

### Project Dependencies
Ensure to list the project's dependencies in a `requirements.txt` file. You can generate this using:
```bash
pip freeze > requirements.txt
```

### Contributing
- Fork the repository.
- Create a new branch (`git checkout -b feature-branch`).
- Commit your changes (`git commit -m 'Add some feature'`).
- Push to the branch (`git push origin feature-branch`).
- Open a pull request.
