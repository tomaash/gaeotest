from gaeo.controller import BaseController

class WelcomeController(BaseController):
    def index(self):
        self.redirect('/user')
