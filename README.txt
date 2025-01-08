install requarements.txt using python 3.7
pip install -r requirements.txt

waitress-serve --call "app:create_wsgi_app"
http://localhost:8080
