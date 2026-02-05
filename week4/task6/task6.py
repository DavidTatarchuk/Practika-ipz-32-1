import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        # "db" — це назва сервісу з docker-compose (вона працює як хост)
        conn = psycopg2.connect(
            host="db",
            database="mydb",
            user="user",
            password="password"
        )
        return "Успіх! Підключення до PostgreSQL працює!"
    except Exception as e:
        return f"Помилка: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)