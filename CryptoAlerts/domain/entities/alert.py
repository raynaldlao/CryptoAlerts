class Alert:
    def __init__(self, id, crypto, limite, variation, devise, mode, reference_value=None):
        self.id = id
        self.crypto = crypto
        self.limite = limite
        self.variation = variation
        self.devise = devise
        self.mode = mode 
        self.reference_value = reference_value
