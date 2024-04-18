import unittest
from unittest.mock import Mock
from domain.use_cases.alert_service import AlertService
from application.errors.crypto_errors import DuplicateIdError

class TestAlertService(unittest.TestCase):
    def setUp(self):
        self.alert_interface = Mock()
        self.alert_interface.get_all_alerts.return_value = []
        self.user_interface = Mock()
        self.api_interface = Mock()
        self.alert_service = AlertService(self.alert_interface, self.user_interface, self.api_interface)

    def test_create_alert_AS(self):
        self.alert_interface.get_alert.return_value = None
        self.api_interface.is_valid_crypto.return_value = True
        self.api_interface.is_valid_currency.return_value = True
        result = self.alert_service.create_alert_AS(1, 'BTC', 10000, 'augmentation', 'USD', 'valeur')
        self.assertEqual(result, "Alerte créée avec l'id 1, en BTC, une devise USD, une variation augmentation, une limite de 10000 et un mode valeur")

    def test_create_alert_AS_duplicate_id(self):
        self.alert_interface.get_alert.return_value = Mock()
        with self.assertRaises(DuplicateIdError):
            self.alert_service.create_alert_AS(1, 'BTC', 10000, 'augmentation', 'USD', 'valeur')

    def test_list_alerts_AS(self):
        self.alert_interface.get_all_alerts.return_value = []
        result = self.alert_service.list_alerts_AS()
        self.assertEqual(result, ["Pas d'alerte trouvé."])

    def test_modify_alert_AS(self):
        self.alert_interface.get_alert.return_value = Mock()
        self.api_interface.is_valid_crypto.return_value = True
        self.api_interface.is_valid_currency.return_value = True
        result = self.alert_service.modify_alert_AS(1, 'ETH', 2000, 'diminution', 'USD', 'valeur')
        self.assertEqual(result, "Alerte modifiée à l'id 1, avec ETH, une devise USD, une variation diminution, une limite de 2000 et un mode valeur")

    def test_delete_alert_AS(self):
        self.alert_interface.get_alert.return_value = Mock()
        result = self.alert_service.delete_alert_AS(1)
        self.assertEqual(result, "Alerte à l'id 1 a été supprimée")

    def test_delete_all_alerts_AS(self):
        result = self.alert_service.delete_all_alerts_AS()
        self.assertEqual(result, "Toutes les alertes ont été supprimées")

    def test_check_alerts_AS(self):
        self.api_interface.is_valid_crypto.return_value = True
        self.api_interface.is_valid_currency.return_value = True
        mock_alert = Mock()
        mock_alert.devise = 'USD'
        self.alert_interface.get_alerts_for_crypto.return_value = [mock_alert]
        result = self.alert_service.check_alerts_AS('BTC', 'USD')
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()
