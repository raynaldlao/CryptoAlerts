import tkinter as tk
from tkinter import messagebox, simpledialog
from domain.use_cases.alert_service import AlertService
from domain.use_cases.authentification_service import AuthentificationService
from application.errors.crypto_errors import CryptoError, DuplicateIdError, DuplicateAlertError, InvalidCryptoError, InvalidCurrencyError, InvalidVariationError, InvalidModeError, NoAlertsFoundError, NoASpecificAlertCreatedError  

class TkinterUI(tk.Tk):
    def __init__(self, alert_service: AlertService, authentification_service: AuthentificationService):
        super().__init__()
        self.alert_service = alert_service
        self.authentification_service = authentification_service
        self.title("Crypto Alerts")
        self.geometry("500x500")
        self.create_login_signup()

    def create_login_signup(self):
        self.login_button = tk.Button(self, text="Identifiant", command=self.login)
        self.login_button.pack()
        self.signup_button = tk.Button(self, text="S'inscrire", command=self.signup)
        self.signup_button.pack()

    def signup(self):
        username = simpledialog.askstring("S'inscrire", "Création du nom de l'utilisateur")
        if username is None: 
            return 
        password = simpledialog.askstring("S'inscrire", "Création du mot de passe", show="*")
        if password is None: 
            return 
        signup_successful = self.authentification_service.signup_authentification_service(username, password)
        if signup_successful:  
            messagebox.showinfo("Succès", f"Compte créé pour {username} !")
        else:
            messagebox.showerror("Erreur", f"Le nom d'utilisateur {username} est déjà pris")

    def login(self):
        username = simpledialog.askstring("Identifiant", "Entrer le nom d'utilisateur")
        if username is None: 
            return  
        password = simpledialog.askstring("Identifiant", "Entrer le mot de passe", show="*")
        if password is None: 
            return
        login_successful = self.authentification_service.login_authentification_service(username, password)
        if not login_successful:
            stored_password = self.authentification_service.user_interface.get_user(username)
            if stored_password is None:
                messagebox.showerror("Erreur", 'Le nom d\'utilisateur n\'existe pas')
            else:
                messagebox.showerror("Erreur", 'Mot de passe incorrect')
        else:
            self.login_button.pack_forget()
            self.signup_button.pack_forget()
            self.create_menu()

    def create_menu(self):
        self.create_alert_button = tk.Button(self, text="Création d'alerte", command=self.create_alert_GUI)
        self.create_alert_button.pack()
        self.list_alerts_button = tk.Button(self, text="Liste d'une ou des alertes", command=self.list_alerts_GUI)
        self.list_alerts_button.pack()
        self.modify_alert_button = tk.Button(self, text="Modification de l'alerte", command=self.modify_alert_GUI)
        self.modify_alert_button.pack()
        self.delete_alert_button = tk.Button(self, text="Suppression de l'alerte", command=self.delete_alert_GUI)
        self.delete_alert_button.pack()
        self.delete_all_alerts_button = tk.Button(self, text="Supprimer toutes les alertes", command=self.delete_all_alerts_GUI)
        self.delete_all_alerts_button.pack()
        self.check_alerts_button = tk.Button(self, text="Vérification d'une ou des alertes", command=self.check_alerts_GUI)
        self.check_alerts_button.pack()

    def disable_menu(self):
        self.create_alert_button.config(state='disabled')
        self.list_alerts_button.config(state='disabled')
        self.modify_alert_button.config(state='disabled')
        self.delete_alert_button.config(state='disabled')
        self.delete_all_alerts_button.config(state='disabled')
        self.check_alerts_button.config(state='disabled')

    def enable_menu(self):
        self.create_alert_button.config(state='normal')
        self.list_alerts_button.config(state='normal')
        self.modify_alert_button.config(state='normal')
        self.delete_alert_button.config(state='normal')
        self.delete_all_alerts_button.config(state='normal')
        self.check_alerts_button.config(state='normal')

    def create_alert_GUI(self):
        id = simpledialog.askinteger("Création d'alerte", "Entrer un chiffre entier pour l\'id")
        if id is None:
            return
        crypto = simpledialog.askstring("Création d'alerte", "Entrer une crypto")
        if crypto is None:
            return
        devise = simpledialog.askstring("Création d'alerte", "Entrer une devise")
        if devise is None:
            return
        variation = simpledialog.askstring("Création d'alerte", "Enter une variation (augmentation/diminution)")
        if variation is None:
            return
        limite = simpledialog.askfloat("Création d'alerte", "Entrez un chiffre limite")
        if limite is None:
            return
        mode = simpledialog.askstring("Création d'alerte", "Choisisez le mode (valeur/pourcentage)")  
        if mode is None:
            return
        try:
            message = self.alert_service.create_alert_AS(id, crypto, float(limite), variation, devise, mode)  
            messagebox.showinfo("Création d'alerte", message)
        except (DuplicateIdError, DuplicateAlertError, InvalidCryptoError, InvalidCurrencyError, InvalidVariationError, InvalidModeError) as e:  
            messagebox.showerror("Erreur", str(e))

    def list_alerts_GUI(self):
        self.disable_menu() 
        alerts = self.alert_service.list_alerts_AS()
        alert_window = tk.Toplevel(self)
        alert_window.title("Liste des alertes")
        for alert in alerts:
            alert_label = tk.Label(alert_window, text=str(alert))
            alert_label.pack()
        alert_window.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(alert_window))

    def on_closing(self, window):
        window.destroy()
        self.enable_menu()

    def modify_alert_GUI(self):
        id = simpledialog.askinteger("Modification de l'alerte", "Entrer un chiffre entier pour l'id de l'alerte afin de le modifier")
        if id is None:
            return
        crypto = simpledialog.askstring("Modification de l'alerte", "Modifiez le crypto")
        if crypto is None:
            return
        devise = simpledialog.askstring("Modification de l'alerte", "Modifiez la devise")
        if devise is None:
            return
        variation = simpledialog.askstring("Modification de l'alerte", "Modifiez la variation (augmentation/diminution)")
        if variation is None:
            return
        limite = simpledialog.askfloat("Modification de l'alerte", "Modifiez le chiffre limite")
        if limite is None:
            return
        mode = simpledialog.askstring("Modification de l'alerte", "Modifiez le mode (valeur/pourcentage)")  
        if mode is None:
            return
        try:
            message = self.alert_service.modify_alert_AS(id, crypto, limite, variation, devise, mode)  
            messagebox.showinfo("Modification de l'alerte", message)
        except DuplicateAlertError as e:  
            messagebox.showerror("Erreur", str(e))

    def delete_alert_GUI(self):
        id = simpledialog.askinteger("Suppression d'une alerte", "Entrer un chiffre entier pour l'id afin de le supprimer")
        if id is None:
            return
        message = self.alert_service.delete_alert_AS(id)
        messagebox.showinfo("Suppresion d'une alerte", message)

    def delete_all_alerts_GUI(self):
        message = self.alert_service.delete_all_alerts_AS()
        messagebox.showinfo("Suppresion de tous les alertes", message)

    def check_alerts_GUI(self):
        crypto = simpledialog.askstring("Vérifications des alertes", "Entrer un crypto pour vérifier l'alerte")
        if crypto is None:
            return
        devise = simpledialog.askstring("Vérifications des alertes", "Entrer une devise pour vérifier l'alerte")
        if devise is None:
            return 
        self.alert_window = tk.Toplevel(self)
        self.alert_window.title("Alertes pour " + crypto + " " + devise)
        scrollbar = tk.Scrollbar(self.alert_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_widget = tk.Text(self.alert_window, yscrollcommand=scrollbar.set)
        self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=self.text_widget.yview)
        self.disable_menu()
        try:
            self._check_alerts_private_GUI(crypto, devise)
        except NoAlertsFoundError as e:
            messagebox.showinfo("Erreur", str(e))
            self.alert_window.destroy()  
        except NoASpecificAlertCreatedError as e:
            messagebox.showinfo("Erreur", str(e))
            self.alert_window.destroy() 
        except InvalidCryptoError as e:
            messagebox.showinfo("Erreur", str(e))
            self.alert_window.destroy()
        except InvalidCurrencyError as e:
            messagebox.showinfo("Erreur", str(e))
            self.alert_window.destroy() 
        finally:
            if self.alert_window.winfo_exists():
                self.wait_window(self.alert_window)
            self.enable_menu()

    def _check_alerts_private_GUI(self, crypto, devise):
        alert_messages = self.alert_service.check_alerts_AS(crypto, devise)
        time_second_check_alerts_GUI = 10000
        if self.text_widget.winfo_exists():
            for message in alert_messages:
                self.text_widget.insert(tk.END, message + "\n")
            self.after(time_second_check_alerts_GUI, self._check_alerts_private_GUI, crypto, devise)
