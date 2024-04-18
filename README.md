# CryptoAlerts

## Prérequis

- Python 3
- Librairies : Requests, Tkinter
- Clés API de CoinAPI (Note : Vous devez vous inscrire pour les obtenir. Ces clés ont une durée d’utilisation limitée, mais elles peuvent être réutilisées après un certain temps)

## Utilisation de l'interface utilisateur graphique

1. Assurez-vous que dans le main, les instructions `ui = TkinterUI(alert_service, auth_service)` et `ui.mainloop()` sont définies.
2. Si vous voulez effacer l’identifiant et le mot de passe que vous avez créés, vous devez aller sur le fichier users.json et les effacer.

## Utilisation de l'interface en ligne de commande

1. Assurez-vous que dans le main, `ui = CommandLineUI(alert_service)` et `ui.run()` sont définies.
2. Exécutez le fichier main.py avec différents arguments pour effectuer différentes actions. Par exemple :
    - Ajouter une alerte : `python3 main.py -a 1 BTC USD augmentation 10000 valeur`
    - Modifier une alerte existante : `python3 main.py -m 1 BTC USD diminution 5000 valeur`
    - Supprimer une alerte spécifique : `python3 main.py -d 1`
    - Supprimer toutes les alertes : `python3 main.py -D`
    - Lister toutes les alertes : `python3 main.py -l`
    - Vérifier les alertes pour une crypto-monnaie et une devise spécifiques : `python3 main.py -c BTC USD`

Note : Vous ne pouvez utiliser qu'un seul argument à la fois.

## Cryptos disponibles

BTC (Bitcoin), ETH (Ethereum), XRP (Ripple), LTC (Litecoin), BCH (Bitcoin Cash), BNB (Binance Coin), USDT (Tether), EOS, BSV (Bitcoin SV), XLM (Stellar), ADA (Cardano), DOT (Polkadot), UNI (Uniswap), USDC (USD Coin), DOGE (Dogecoin)

## Devises disponibles

USD (Dollar américain), EUR (Euro), GBP (Livre sterling), JPY (Yen japonais), AUD (Dollar australien), CAD (Dollar canadien), CHF (Franc suisse), CNY (Yuan chinois), SEK (Couronne suédoise), NZD (Dollar néo-zélandais)

## Captures d'écran

1. Menus :
   
!![Interface_Login_Signup](https://github.com/raynaldlao/CryptoAlerts/assets/131525323/5c2e3f89-c4de-4d42-ba40-8b3decfd7b9b)
![Menu](https://github.com/raynaldlao/CryptoAlerts/assets/131525323/cccad743-eb6c-488f-862e-0fd1bb4e9975)

2. Opérations CRUD :

![Create_Alert](https://github.com/raynaldlao/CryptoAlerts/assets/131525323/d6570499-79bd-4506-bbec-d1d0fd989737)
![List_Alerts](https://github.com/raynaldlao/CryptoAlerts/assets/131525323/c6db6c4c-cb1f-4f60-81f1-a0f4c8951935)
![Modify_Alerts](https://github.com/raynaldlao/CryptoAlerts/assets/131525323/8d0ac6c6-6af2-49ce-ad32-015e493cd6b6)
![Delete_All_Alerts](https://github.com/raynaldlao/CryptoAlerts/assets/131525323/149e8fd9-a994-47cc-b180-6037fd49f1bc)

3. Affichage des alertes :

![Check_Alerts](https://github.com/raynaldlao/CryptoAlerts/assets/131525323/09bbd27d-d2ba-4481-980a-aff1fbfc6318)

5. Interface en ligne de commande :

![CLI](https://github.com/raynaldlao/CryptoAlerts/assets/131525323/353f8365-0e73-45d4-b29d-e83193badc38)
