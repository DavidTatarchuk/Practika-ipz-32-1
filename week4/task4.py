import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# 1. ГЕШУВАННЯ (SHA-256)
def run_hashing(text):
    # Перетворюємо текст у байти та рахуємо геш
    hash_object = hashlib.sha256(text.encode())
    hex_dig = hash_object.hexdigest()
    print(f"[SHA-256] Вхід: '{text}' -> Геш: {hex_dig}")
    return hex_dig

# 2. СИМЕТРИЧНЕ ШИФРУВАННЯ (AES через Fernet)
def run_symmetric(text):
    # Генеруємо ключ
    key = Fernet.generate_key()
    cipher = Fernet(key)
    
    # Шифруємо
    encrypted_text = cipher.encrypt(text.encode())
    print(f"[AES] Зашифровано: {encrypted_text}")
    
    # Розшифровуємо
    decrypted_text = cipher.decrypt(encrypted_text).decode()
    print(f"[AES] Розшифровано: {decrypted_text}")

# 3. АСИМЕТРИЧНИЙ ПІДПИС (RSA)
def run_rsa_signature(text):
    # Генеруємо пару ключів (публічний та приватний)
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    # Створюємо підпис (sign)
    signature = private_key.sign(
        text.encode(),
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    print(f"[RSA] Підпис створено (розмір {len(signature)} байт)")

    # Перевіряємо підпис (verify)
    try:
        public_key.verify(
            signature,
            text.encode(),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        print("[RSA] Успіх: Підпис вірний (дані не змінено).")
    except Exception:
        print("[RSA] Помилка: Підпис невірний!")

# --- ЗАПУСК ---
message = "Secret Message"

print("--- 1. Гешування ---")
run_hashing(message)

print("\n--- 2. Симетричне шифрування (AES) ---")
run_symmetric(message)

print("\n--- 3. Цифровий підпис (RSA) ---")
run_rsa_signature(message)