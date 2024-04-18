from domain.entities.alert import Alert
from application.interfaces.alert_interface import AlertInterface
from application.interfaces.api_interface import ApiInterface
from application.interfaces.user_interface import UserInterface  
from application.errors.crypto_errors import CryptoError, InvalidCryptoError, InvalidCurrencyError, DuplicateIdError, DuplicateAlertError, InvalidVariationError, InvalidModeError, NoAlertsFoundError, NoASpecificAlertCreatedError

class AlertService:
    def __init__(self, alert_interface: AlertInterface, user_interface: UserInterface, api_interface: ApiInterface):
        self.alert_interface = alert_interface
        self.user_interface = user_interface
        self.api_interface = api_interface

    def create_alert_AS(self, id, crypto, limite, variation, devise, mode): 
        if self.alert_interface.get_alert(id) is not None:
            raise DuplicateIdError(id)
        alerts = self.alert_interface.get_all_alerts()
        for alert in alerts:
            if (alert.crypto == crypto and alert.limite == limite and alert.variation == variation and
                alert.devise == devise and alert.mode == mode):  
                raise DuplicateAlertError(crypto, limite, variation, devise, mode)  
        if not self.api_interface.is_valid_crypto(crypto):
            raise InvalidCryptoError(crypto)
        if variation not in ['augmentation', 'diminution']:
            raise InvalidVariationError(variation)
        if not self.api_interface.is_valid_currency(devise):
            raise InvalidCurrencyError(devise)
        if mode not in ['valeur', 'pourcentage']:  
            raise InvalidModeError(mode) 
        current_rate = self.api_interface.get_current_value(crypto, devise)
        alert = Alert(id, crypto, limite, variation, devise, mode, current_rate) 
        self.alert_interface.save_alert(alert)    
        return f'Alerte créée avec l\'id {id}, en {crypto}, une devise {devise}, une variation {variation}, une limite de {limite} et un mode {mode}' 

    def list_alerts_AS(self):
        alerts = self.alert_interface.get_all_alerts()
        if alerts is not None and len(alerts) > 0:
            return [f'Alerte {alert.id} : {alert.crypto} limite = {alert.limite}, variation = {alert.variation}, devise = {alert.devise}, mode = {alert.mode}' for alert in alerts] 
        else:
            return ["Pas d'alerte trouvé."]
    
    def modify_alert_AS(self, id, crypto, limite, variation, devise, mode):  
        if not self.api_interface.is_valid_crypto(crypto):
            raise InvalidCryptoError(crypto)
        if not self.api_interface.is_valid_currency(devise):
            raise InvalidCurrencyError(devise)
        if mode not in ['valeur', 'pourcentage']:
            raise InvalidModeError(mode)
        if variation not in ['augmentation', 'diminution']:
            raise InvalidVariationError(variation)
        alerts = self.alert_interface.get_all_alerts()
        for alert in alerts:
            if alert.id != id and (alert.crypto == crypto and alert.limite == limite and alert.variation == variation and
                alert.devise == devise and alert.mode == mode):  
                raise DuplicateAlertError(crypto, limite, variation, devise, mode)  
        alert = self.alert_interface.get_alert(id)
        if alert is not None:
            alert.crypto = crypto
            alert.limite = limite
            alert.variation = variation
            alert.devise = devise
            alert.mode = mode  
            self.alert_interface.update_alert(id, alert)
            return f'Alerte modifiée à l\'id {id}, avec {crypto}, une devise {devise}, une variation {variation}, une limite de {limite} et un mode {mode}'  
        else:
            return f'Pas d\'alerte trouvée à l\'id {id}'

    def delete_alert_AS(self, id):
        alert = self.alert_interface.get_alert(id)
        if alert is not None:
            self.alert_interface.delete_alert(id)
            return f'Alerte à l\'id {id} a été supprimée'
        else:
            return f'Pas d\'alerte trouvée à l\'id {id}'

    def delete_all_alerts_AS(self):
        self.alert_interface.delete_all_alerts()
        return f'Toutes les alertes ont été supprimées'

    def check_alerts_AS(self, crypto, devise):
        if not self.api_interface.is_valid_crypto(crypto):
            raise InvalidCryptoError(crypto)
        if not self.api_interface.is_valid_currency(devise):
            raise InvalidCurrencyError(devise)
        alerts = self.alert_interface.get_alerts_for_crypto(crypto)
        if not alerts:
            raise NoAlertsFoundError(crypto, devise)
        if not any(alert.devise == devise for alert in alerts):
            raise NoASpecificAlertCreatedError(crypto, devise)
        alert_messages = []
        chiffre_signficatif_percentage_change=3
        percentage_change_cent_pour_cent = 100
        for alert in alerts:
            if alert.devise == devise:
                current_value = self.api_interface.get_current_value(crypto, devise)
                alert_messages.append(f"La valeur actuelle en {crypto} est {current_value} {devise}")
                if alert.mode == 'pourcentage':  
                    percentage_change = round(((current_value - alert.reference_value) / alert.reference_value) * percentage_change_cent_pour_cent, chiffre_signficatif_percentage_change)
                    alert_messages.append(f"Le pourcentage de changement est de {percentage_change}% par rapport à la limite de {alert.limite}% définie lors de la création de l'alerte")
                    if alert.variation == 'diminution' and percentage_change <= -alert.limite:
                        alert_messages.append(f'Alerte: {crypto} a diminué de {percentage_change}% par rapport à sa valeur lors de la création de l\'alerte. Le seuil défini est de {alert.limite}%')
                    elif alert.variation == 'augmentation' and percentage_change >= alert.limite:
                        alert_messages.append(f'Alerte: {crypto} a augmenté de {percentage_change}% par rapport à sa valeur lors de la création de l\'alerte. Le seuil défini est de {alert.limite}%')
                else:
                    if alert.variation == 'diminution' and current_value < alert.limite:
                        alert_messages.append(f'Alerte: {crypto} est tombé en dessous de {alert.limite} {devise}')
                    elif alert.variation == 'augmentation' and current_value > alert.limite:
                        alert_messages.append(f'Alerte: {crypto} a dépassé {alert.limite} {devise}')
            alert_messages.append("")
        return alert_messages
