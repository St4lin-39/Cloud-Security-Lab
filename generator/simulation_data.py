import random 
BRUTE_FORCE_PASSWORDS = [
    "123456",
    "password",
    "admin",
    "welcome",
    "qwerty",
    "Spring2025!",
    "Summer2025!",
    "Password123"
]


LEAKED_CREDENTIALS = {
    "Luis": "Luis123",
    "Carlos": "Carlos2024",
    "Ana": "AnaPassword",
    "Pedro": "Pedro321",
    "Maria": "Maria2025"
}


PASSWORD_SPRAYING_PASSWORD = "Spring2025!"

def get_random_brute_force_password():
    return random.choice(BRUTE_FORCE_PASSWORDS)

def get_leaked_password(username: str):
    return LEAKED_CREDENTIALS.get(username)

def get_password_spraying_password():
    return PASSWORD_SPRAYING_PASSWORD