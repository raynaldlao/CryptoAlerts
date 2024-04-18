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

Voici quelques captures d'écran de l'application :

!Interface_Login_Signup.png
