from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# Налаштування
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Ключ для підпису токенів
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

# Тимчасова база даних (словник)
users_db = {} 

# 1. Реєстрація (Зберігаємо геш пароля)
@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    # Створюємо геш пароля
    pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    
    users_db[username] = pw_hash
    return jsonify({"message": "Користувача створено успішно"}), 201

# 2. Вхід (Перевіряємо геш -> Видаємо токен)
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    stored_hash = users_db.get(username)

    # Перевірка: чи існує юзер і чи співпадає пароль з гешем
    if stored_hash and bcrypt.check_password_hash(stored_hash, password):
        token = create_access_token(identity=username)
        return jsonify({"access_token": token})
    
    return jsonify({"message": "Невірний логін або пароль"}), 401

# 3. Захищений маршрут (Вимагає токен)
@app.route('/profile', methods=['GET'])
@jwt_required()  # <-- Цей декоратор захищає вхід
def profile():
    current_user = get_jwt_identity()
    return jsonify({"message": f"Ласкаво просимо, {current_user}! Це секретні дані."})

if __name__ == '__main__':
    app.run(debug=True)