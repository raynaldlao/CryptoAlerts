from typing import Optional

class UserInterface:
    def save_user(self, username: str, password: str):
        """Enregistre un nouvel utilisateur"""
        raise NotImplementedError

    def get_user(self, username: str) -> Optional[str]:
        """Récupère le mot de passe d'un utilisateur"""
        raise NotImplementedError
    
