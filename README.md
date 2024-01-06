# Soccer Bets Project
The "Soccer Bets Project" is a web app developed with
Django, Celery, Celery Beat, Redis, and PostgreSQL. It
provides soccer enthusiasts with betting tips for
upcoming matches. Using Celery and Redis, it
delivers real-time updates and employs scheduled
tasks through Celery Beat. PostgreSQL stores user
data and historical tips. Admins can update tips via
the admin dashboard.

To run the Soccer Bets Project on your local environment, follow these steps:

1. Clone the repository to your local machine:

    ```
   git clone https://github.com/ntungufhadzeni/soccer_bets.git
   ```
2. Navigate to the project directory:
   ```
   cd soccer_bets
   ```
3. Create rapidapi.com account and subscribe subscription to the Football Prediction API to get API key.
4. Create .env.dev file and paste this:

   ```
   # .env.dev
   SECRET_KEY=django-insecure-q#(2#8744e7j0o44%f9c)p&qf)640)g6&i+z&1d=at7a!8&a6!#w
   DEBUG=1
   REDIS_URL=redis://redis:6379/0
   SQL_ENGINE=django.db.backends.postgresql
   SQL_DATABASE=postgres
   SQL_USER=postgres
   SQL_PASSWORD=postgres
   SQL_HOST=db
   SQL_PORT=5432
   DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
   X_RAPIDAPI_KEY=<your football prediction api key here>
   X_RAPIDAPI_HOST=football-prediction-api.p.rapidapi.com
   API_URL=https://football-prediction-api.p.rapidapi.com/api/v2/predictions
   ```
5. Build and start docker containers:
   ```
   docker-compose -f docker-compose.dev.yml up --build
    ```
6. Access the project in your web browser at `http://127.0.0.1/`.
7. Create superuser account:
   ```
   docker exec -it web bash
    ```
   ```
   python manage.py createsuperuser
    ```
8. Log in to the admin panel and schedule cronjobs to retrieve data from the API: `http://127.0.0.1/admin`.