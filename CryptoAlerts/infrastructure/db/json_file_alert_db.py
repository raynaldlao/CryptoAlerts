import json
import os
from application.interfaces.alert_interface import AlertInterface
from domain.entities.alert import Alert

class JsonFileAlertDb(AlertInterface):
    def __init__(self, alerts_file='data/alerts.json'):
        self.alerts_file = alerts_file 
        file_size_octet_db_alert_json = 0
        if os.path.exists(alerts_file) and os.path.getsize(alerts_file) > file_size_octet_db_alert_json:
            with open(alerts_file, 'r') as f:
                self.alerts = json.load(f)
        else:
            self.alerts = []

    def save_alert(self, alert):
        self.alerts.append(alert.__dict__)
        self._save_alerts()

    def get_alert(self, id):
        for alert in self.alerts:
            if alert['id'] == id:
                return Alert(**alert)
        return None

    def delete_alert(self, id):
        self.alerts = [alert for alert in self.alerts if alert['id'] != id]
        self._save_alerts()

    def delete_all_alerts(self):
        self.alerts = []
        self._save_alerts()

    def get_all_alerts(self):
        return [Alert(**alert) for alert in self.alerts]

    def get_alerts_for_crypto(self, crypto):
        return [Alert(**alert) for alert in self.alerts if alert['crypto'] == crypto]

    def _save_alerts(self):
        with open(self.alerts_file, 'w') as f:
            json.dump(self.alerts, f)

    def update_alert(self, id, alert):
        for i, existing_alert in enumerate(self.alerts):
            if existing_alert['id'] == id:
                self.alerts[i] = alert.__dict__
                self._save_alerts()
                return
        print(f'Pas d\'alerte trouvée à l\'id {id}')
