from domain.entities.alert import Alert
from typing import List

class AlertInterface:
    def save_alert(self, alert: Alert):
        """Enregistre une alerte dans la base de données"""
        raise NotImplementedError

    def get_alert(self, id: int) -> Alert:
        """Récupère une alerte spécifique de la base de données"""
        raise NotImplementedError

    def delete_alert(self, id: int):
        """Supprime une alerte spécifique de la base de données"""
        raise NotImplementedError

    def delete_all_alerts(self):
        """Supprime toutes les alertes de la base de données"""
        raise NotImplementedError

    def get_all_alerts(self) -> List[Alert]:
        """Récupère toutes les alertes de la base de données"""
        raise NotImplementedError

    def get_alerts_for_crypto(self, crypto: str) -> List[Alert]:
        """Récupère toutes les alertes pour une crypto-monnaie spécifique de la base de données"""
        raise NotImplementedError

    def update_alert(self, id, alert):
        """Mettre à jour une alerte existante"""
        raise NotImplementedError
