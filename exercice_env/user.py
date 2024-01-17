"""Module pour générer des utilisateurs aléatoirement"""
import faker
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(filename=BASE_DIR / "user.log", level=logging.INFO)
fake = faker.Faker()

#Génére un utilisateur
def get_user():
    """Génère un utilisateur

    Returns:
        str: user
    """
    logging.info("Generating user")
    return f"{fake.first_name()}, {fake.last_name()}"

#Génére plusieurs utilisateurs    
def get_users(n):
    """Génère une liste de plusieurs utilisateurs

    Args:
        n (int): nombre d'utilisateurs à générer

    Returns:
        liste[str]: utilisateurs
    """
    logging.info(f"Generatin a liste of {n} users")
#Option 1
    users = []
    for i in range(n):
        users.append(get_user())
    return users

#Option 2 compréension de liste sur une ligne
    #return [get_users() for _ in range(n)]

if __name__ == "__main__":
    user = get_users(n=5)
    print(user)
