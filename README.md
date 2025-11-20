Community Ready Project (SQLite)

This ZIP is a ready-to-run Django project (uses SQLite by default so no DB install required).

Steps to run (Windows PowerShell):
1. Extract the ZIP and open PowerShell inside the project folder.
2. Create and activate venv:
   python -m venv venv
   .\venv\Scripts\Activate.ps1
3. Install requirements:
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
4. Make migrations and migrate:
   python manage.py makemigrations
   python manage.py migrate
5. Create superuser:
   python manage.py createsuperuser
6. Run server:
   python manage.py runserver
7. Open http://127.0.0.1:8000/ and /admin/

Notes:
- Uploads go to the media/ folder.
- 'My Portfolio' page shows only your artworks (/artworks/my/).
