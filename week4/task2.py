from flask import Flask, jsonify, request

app = Flask(__name__)

# "База даних" у пам'яті (список)
users = [
    {"id": 1, "name": "Ivan", "role": "admin"},
    {"id": 2, "name": "Maria", "role": "user"}
]

# Функція для стандартизації відповіді
def api_response(status, data=None, message=""):
    return jsonify({"status": status, "data": data, "message": message})

# 1. Отримати всіх (GET)
@app.route('/users', methods=['GET'])
def get_users():
    return api_response("success", users, "Список користувачів")

# 2. Створити нового (POST)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = {
        "id": users[-1]["id"] + 1 if users else 1,
        "name": data.get("name"),
        "role": data.get("role")
    }
    users.append(new_user)
    return api_response("success", new_user, "Користувача створено"), 201

# 3. Отримати одного (GET)
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return api_response("success", user, "Користувача знайдено")
    return api_response("error", message="Користувача не знайдено"), 404

# 4. Оновити (PUT)
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return api_response("error", message="Користувача не знайдено"), 404
    
    data = request.json
    user.update(data) # Оновлюємо поля
    return api_response("success", user, "Дані оновлено")

# 5. Видалити (DELETE)
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return api_response("success", message="Користувача видалено")

if __name__ == '__main__':
    app.run(debug=True)