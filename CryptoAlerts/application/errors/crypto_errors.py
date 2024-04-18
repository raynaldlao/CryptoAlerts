class CryptoError(Exception):
    """Exception de base pour les erreurs liées à la crypto-monnaie"""
    pass

class InvalidCryptoError(CryptoError):
    """Exception levée pour une crypto-monnaie invalide"""
    def __init__(self, crypto):
        self.message = f'Format de crypto-monnaie invalide : {crypto}. Veuillez utiliser le format CoinAPI'
        super().__init__(self.message)

class InvalidCurrencyError(CryptoError):
    """Exception levée pour une devise invalide"""
    def __init__(self, devise):
        self.message = f'Format de devise invalide : {devise}. Les devises valides sont USD, EUR, GBP, JPY, etc.'
        super().__init__(self.message)

class ApiError(CryptoError):
    """Exception levée pour une erreur d'API"""
    def __init__(self, message):
        self.message = f'Erreur lors de l\'envoi de la requête à l\'API : {message}'
        super().__init__(self.message)

class DuplicateAlertError(CryptoError):
    """Exception levée lorsqu'une alerte avec les mêmes attributs existe déjà"""
    def __init__(self, crypto, limite, variation, devise, mode):
        self.message = f'Une alerte en {crypto} avec une limite de {limite}, une variation {variation}, une devise {devise} et un mode {mode} existe déjà'
        super().__init__(self.message)

class DuplicateIdError(CryptoError):
    """Exception levée lorsqu'un ID d'alerte identique existe déjà"""
    def __init__(self, id):
        self.message = f'Une alerte avec l\'id {id} existe déjà'
        super().__init__(self.message)

class InvalidVariationError(CryptoError):
    """Exception levée pour une variation d'alerte invalide"""
    def __init__(self, variation):
        self.message = f'Type d\'alerte invalide : {variation}. Les variations d\'alerte valides sont "augmentation" et "diminution"'
        super().__init__(self.message)

class InvalidModeError(CryptoError):
    """Exception levée pour un mode d'alerte invalide"""
    def __init__(self, mode):
        if mode not in ['valeur', 'pourcentage']:
            self.message = f'Type d\'alerte invalide : {mode}. Les modes d\'alerte valides sont "valeur" et "pourcentage"'
            super().__init__(self.message)

class NoAlertsFoundError(CryptoError):
    """Exception levée lorsqu'aucune alerte n'est trouvée pour une certaine crypto-monnaie et devise"""
    def __init__(self, crypto, devise):
        self.message = f'Pas d\'alertes trouvées pour {crypto} en {devise}'
        super().__init__(self.message)

class NoASpecificAlertCreatedError(CryptoError):
    """Exception levée lorsqu'aucune alerte n'a été créée pour une certaine crypto-monnaie et devise"""
    def __init__(self, crypto, devise):
        self.message = f'Aucune alerte n\'a été créée pour {crypto} en {devise}'
        super().__init__(self.message)
