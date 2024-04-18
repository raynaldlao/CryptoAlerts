"""
CryptoAlerts Application

Description : 

CryptoAlerts est une application qui offre aux utilisateurs la possibilité de mettre en place des alertes basées sur les fluctuations de prix des crypto-monnaies.
Les utilisateurs peuvent ajouter une alerte pour une crypto-monnaie spécifique et recevoir des notifications lorsque le prix de cette crypto-monnaie atteint un certain seuil. 
Les alertes peuvent être créées, modifiées, supprimées et listées via une interface en ligne de commande ou une interface utilisateur graphique Tkinter.
L'application utilise l'API CoinAPI pour récupérer les données de prix des crypto-monnaies et stocke les alertes dans une base de données locale au format JSON. 
L'application prend également en charge l'authentification des utilisateurs, mais seulement pour l'utilisation de l'interface graphique.

Prérequis (À LIRE ABSOLUMENT !): 

L'application a été testée sur Visual Studio Code. Pour l'exécuter, vous aurez besoin de Python 3 et de quelques librairies, dont Requests et Tkinter pour bénéficier de l'interface utilisateur graphique.
Vous devez également vous inscrire sur CoinAPI pour obtenir des clés API. Ces clés ont une durée d’utilisation limitée, mais elles peuvent être réutilisées après un certain temps.
LANCER LE CODE DE CETTE MANIÈRE : nom@nom-XXXX-XXXX:~/Bureau/CryptoAlerts$ python3 main.py.

Si vous utilisez l'interface utilisateur graphique, vérifier que dans le main ui = TkinterUI(alert_service, auth_service)
Si vous voulez effacer l’identifiant et le mot de passe que vous avez créés, vous devez aller sur le fichier users.json et les effacer. 
Si vous utilisez l'interface en ligne de commande, vérifier que dans le main ui = CommandLineUI(alert_service) 

En ce qui concerne l'affichage des alertes, elle s'affiche tous les 10 secondes d'intervalle. Si vous mettez des alertes qui ne respecte pas les conditions, eLles ne s'afficheront pas.
Vous pouvez à tout moment changer le temps, je recommande d'utiliser le mode "valeur" mais vous pouvez aussi utiliser le mode "pourcentage" avec de très petite valeur comme 0.02 par exemple.

Pour utiliser l'interface en ligne de commande de CryptoAlerts, vous pouvez exécuter le fichier main.py dans le répertoire CryptoAlerts avec différents arguments pour effectuer différentes actions.
Voici une liste des arguments que vous pouvez utiliser :

- `-a` ou `--add` : Ajouter une alerte. Vous devez fournir 6 arguments supplémentaires : id, crypto, devise, variation, limite, mode.
    Exemple : `nom@nom-XXXX-XXXX:~/Bureau/CryptoAlerts$ python3 main.py -a 1 BTC USD augmentation 10000 valeur`

- `-m` ou `--modify` : Modifier une alerte existante. Vous devez fournir 6 arguments supplémentaires : id, crypto, devise, variation, limite, mode.
    Exemple : `nom@nom-XXXX-XXXX:~/Bureau/CryptoAlerts$ python3 main.py -m 1 BTC USD diminution 5000 valeur`

- `-d` ou `--delete` : Supprimer une alerte spécifique. Vous devez fournir 1 argument supplémentaire : id.
    Exemple : `nom@nom-XXXX-XXXX:~/Bureau/CryptoAlerts$ python3 main.py -d 1`

- `-D` ou `--D` : Supprimer toutes les alertes.
    Exemple : `nom@nom-XXXX-XXXX:~/Bureau/CryptoAlerts$ python3 main.py -D`

- `-l` ou `--list` : Lister toutes les alertes.
    Exemple : `nom@nom-XXXX-XXXX:~/Bureau/CryptoAlerts$ python3 main.py -l`

- `-c` ou `--check` : Vérifier les alertes pour une crypto-monnaie et une devise spécifiques. Vous devez fournir 2 arguments supplémentaires : crypto, devise.
    Exemple : `nom@nom-XXXX-XXXX:~/Bureau/CryptoAlerts$ python3 main.py -c BTC USD`

Notez que vous ne pouvez utiliser qu'un seul argument à la fois. Par exemple, vous ne pouvez pas ajouter et supprimer une alerte en une seule commande.

Cryptos disponibles : BTC (Bitcoin), ETH (Ethereum), XRP (Ripple), LTC (Litecoin), BCH (Bitcoin Cash), BNB (Binance Coin), USDT (Tether), EOS, BSV (Bitcoin SV), XLM (Stellar), ADA (Cardano), DOT (Polkadot), UNI (Uniswap), USDC (USD Coin), DOGE (Dogecoin).

Devises disponibles : USD (Dollar américain), EUR (Euro), GBP (Livre sterling), JPY (Yen japonais), AUD (Dollar australien), CAD (Dollar canadien), CHF (Franc suisse), CNY (Yuan chinois), SEK (Couronne suédoise), NZD (Dollar néo-zélandais).

Auteur : Raynald LAOKHAMTHONG
Date : 18/04/2024
"""

from application.errors.crypto_errors import CryptoError, InvalidCryptoError, InvalidCurrencyError, ApiError, DuplicateIdError, DuplicateAlertError, InvalidVariationError, InvalidModeError 
from domain.use_cases.alert_service import AlertService
from domain.use_cases.authentification_service import AuthentificationService
from application.interfaces.alert_interface import AlertInterface
from application.interfaces.user_interface import UserInterface
from application.interfaces.api_interface import ApiInterface
from infrastructure.api.coin_api_adapter import CoinApiAdapter
from infrastructure.db.json_file_alert_db import JsonFileAlertDb
from infrastructure.db.json_file_ui_db import JsonFileUserDb
from infrastructure.ui.command_line_ui import CommandLineUI
from infrastructure.ui.tkinter_ui import TkinterUI
import config

def main():
    try:
        api_interface: ApiInterface = CoinApiAdapter(config.API_KEY)
        alert_interface: AlertInterface = JsonFileAlertDb(config.ALERTS_FILE)
        user_interface: UserInterface = JsonFileUserDb()
        alert_service = AlertService(alert_interface, user_interface, api_interface)
        auth_service = AuthentificationService(user_interface)
        ui = CommandLineUI(alert_service) # CommandLineUI(alert_service) pour le CLI et TkinterUI(alert_service, auth_service) pour le GUI
        ui.run() # CommandLineUI pour run() et TkinterUI pour mainloop()
    except (CryptoError, InvalidCryptoError, InvalidCurrencyError, ApiError, DuplicateIdError, DuplicateAlertError, InvalidVariationError, InvalidModeError) as e:  
        print(f"Une erreur s'est produite : {e}")
if __name__ == "__main__":
    main()