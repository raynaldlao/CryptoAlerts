import unittest
from unittest.mock import Mock, patch
from infrastructure.ui.command_line_ui import CommandLineUI
from domain.use_cases.alert_service import AlertService
from application.errors.crypto_errors import DuplicateIdError

class TestCommandLineUI(unittest.TestCase):
    def setUp(self):
        self.alert_service = Mock(spec=AlertService)
        self.ui = CommandLineUI(self.alert_service)

    @patch('builtins.input', return_value='1')
    def test_create_alert_CLI(self, input):
        self.alert_service.create_alert_AS.return_value = "Alerte créée avec succès"
        self.ui.create_alert_CLI(1, 'BTC', 10000, 'augmentation', 'USD', 'valeur')
        self.alert_service.create_alert_AS.assert_called_once_with(1, 'BTC', 10000, 'augmentation', 'USD', 'valeur')

    @patch('builtins.input', return_value='1')
    @patch('builtins.print')
    def test_create_alert_CLI_duplicate_id(self, mock_print, mock_input):
        self.alert_service.create_alert_AS.side_effect = DuplicateIdError("L'ID existe déjà")
        self.ui.create_alert_CLI(1, 'BTC', 10000, 'augmentation', 'USD', 'valeur')
        mock_print.assert_called_once_with("Erreur : Une alerte avec l'id L'ID existe déjà existe déjà")

    def test_list_alerts_CLI(self):
        self.alert_service.list_alerts_AS.return_value = []
        self.ui.list_alerts_CLI()
        self.alert_service.list_alerts_AS.assert_called_once()

    @patch('builtins.input', return_value='1')
    def test_modify_alert_CLI(self, input):
        self.alert_service.modify_alert_AS.return_value = "Alerte modifiée avec succès"
        self.ui.modify_alert_CLI(1, 'ETH', 2000, 'diminution', 'USD', 'valeur')
        self.alert_service.modify_alert_AS.assert_called_once_with(1, 'ETH', 'USD', 'diminution', 2000, 'valeur')

    @patch('builtins.input', return_value='1')
    def test_delete_alert_CLI(self, input):
        self.alert_service.delete_alert_AS.return_value = "Alerte supprimée avec succès"
        self.ui.delete_alert_CLI(1)
        self.alert_service.delete_alert_AS.assert_called_once_with(1)

    def test_delete_all_alerts_CLI(self):
        self.alert_service.delete_all_alerts_AS.return_value = "Toutes les alertes ont été supprimées"
        self.ui.delete_all_alerts_CLI()
        self.alert_service.delete_all_alerts_AS.assert_called_once()

    def test_check_alerts_CLI(self):
        self.alert_service.check_alerts_AS.return_value = ["Alerte 1", "Alerte 2"]
        self.ui.check_alerts_CLI('BTC', 'USD')
        self.alert_service.check_alerts_AS.assert_called_once_with('BTC', 'USD')

if __name__ == '__main__':
    unittest.main()
