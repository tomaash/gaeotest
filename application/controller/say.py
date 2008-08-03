from gaeo.controller import BaseController

class SayController(BaseController):
    def hello(self):
        self.render(text='hello, world')

    