from application.interfaces.user_interface import UserInterface
from domain.entities.user import User

class AuthentificationService :
    def __init__(self, user_interface: UserInterface):
        self.user_interface = user_interface
    
    def signup_authentification_service(self, username, password):
        if self.user_interface.get_user(username):
            return False
        else:
            self.user_interface.save_user(username, password)
            return True
    
    def login_authentification_service(self, username, password):  
        user = User(username, password)
        stored_password = self.user_interface.get_user(user.username)
        if stored_password is None or stored_password != user.password:
            return False
        return True
