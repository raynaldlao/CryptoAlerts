import argparse
import time
from domain.use_cases.alert_service import AlertService
from application.errors.crypto_errors import CryptoError, DuplicateIdError, DuplicateAlertError, InvalidCryptoError, InvalidCurrencyError, InvalidVariationError, InvalidModeError, NoAlertsFoundError, NoASpecificAlertCreatedError

class CommandLineUI:
    def __init__(self, alert_service: AlertService):
        self.alert_service = alert_service
    
    def create_alert_CLI(self, id, crypto, limite, variation, devise='USD', mode='valeur'):  
        try:
            message = self.alert_service.create_alert_AS(id, crypto, float(limite), variation, devise, mode) 
            print(message)
        except (DuplicateIdError, DuplicateAlertError, InvalidCryptoError, InvalidCurrencyError, InvalidVariationError, InvalidModeError, InvalidModeError) as e:  
            print(f"Erreur : {str(e)}")

    def list_alerts_CLI(self):
        alerts = self.alert_service.list_alerts_AS()
        for alert in alerts:
            print(alert)
            
    def modify_alert_CLI(self, id, crypto, devise, variation, limite, mode='valeur'):  
        message = self.alert_service.modify_alert_AS(id, crypto, limite, variation, devise, mode)  
        print(message)

    def delete_alert_CLI(self, id):
        message = self.alert_service.delete_alert_AS(id)
        print(message)

    def delete_all_alerts_CLI(self):
        message = self.alert_service.delete_all_alerts_AS()
        print(message)

    def check_alerts_CLI(self, crypto, devise):
        arret_programme=0
        try:
            alert_messages = self.alert_service.check_alerts_AS(crypto, devise)
            for message in alert_messages:
                print(message)
        except NoAlertsFoundError as e:
            print(e)
            exit(arret_programme)
        except NoASpecificAlertCreatedError as e:
            print(e)
            exit(arret_programme)
        except InvalidCryptoError as e:
            print(e)
            exit(arret_programme)
        except InvalidCurrencyError as e:
            print(e)
            exit(arret_programme)    
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

    def run(self):
        args = self.get_args()
        time_second_check_alerts_CLI = 10
        if args.add:
            id, crypto, devise, variation, limite, mode = args.add 
            self.create_alert_CLI(int(id), crypto, float(limite), variation, devise, mode)  
        elif args.modify:
            id, crypto, devise, variation, limite, mode = args.modify  
            self.modify_alert_CLI(int(id), crypto, devise, variation, float(limite), mode)
        elif args.delete:
            self.delete_alert_CLI(args.delete[0]) # Voit comme une liste
        elif args.D:
            self.delete_all_alerts_CLI()
        elif args.list:
            self.list_alerts_CLI()
        elif args.check:
            crypto, devise = args.check
            while True:
                self.check_alerts_CLI(crypto, devise)
                time.sleep(time_second_check_alerts_CLI)

    def get_args(self):
        parser = argparse.ArgumentParser(description='Gestionnaire d\'alertes de crypto-monnaie')
        parser.add_argument('-a', '--add', nargs=6, metavar=('id', 'crypto', 'devise', 'variation', 'limite', 'mode'), help='Ajouter une alerte pour une crypto-monnaie')  
        parser.add_argument('-m', '--modify', nargs=6, metavar=('id', 'crypto', 'devise', 'variation', 'limite', 'mode'), help='Modifier une alerte pour une crypto-monnaie')  
        parser.add_argument('-d', '--delete', nargs=1, type=int, help='Supprimer une alerte pour une crypto-monnaie')
        parser.add_argument('-D', '--D', action='store_true', help='Supprimer toutes les alertes')
        parser.add_argument('-l', '--list', action='store_true', help='Lister toutes les alertes')
        parser.add_argument('-c', '--check', nargs=2, metavar=('crypto', 'devise'), help='Vérifier les alertes en continu pour une crypto-monnaie spécifique et une devise')
        return parser.parse_args()
