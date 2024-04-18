from typing import Dict

class ApiInterface:
    def get_current_value(self, crypto: str, devise: str) -> float:
        """Récupère la valeur actuelle pour une crypto-monnaie spécifique"""
        raise NotImplementedError

    def is_valid_crypto(self, crypto: str) -> bool:
        """Vérifie si une crypto-monnaie est valide"""
        raise NotImplementedError

    def is_valid_currency(self, devise: str) -> bool:
        """Vérifie si une devise est valide"""
        raise NotImplementedError
