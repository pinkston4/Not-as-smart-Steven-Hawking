import subprocess
import os

class Commander:

    def __init__(self):
        self.confirm = ['yes', 'affirmative', 'sure', 'si',
                        'do it', 'gotcha', 'yeah', 'confirm']
        self.cancel = ['no', 'negative', 'negatory', 'negative soldier',
                        'wait', 'cancel', 'stop']

    def respond(self, response):
        subprocess.call('say ' + response, shell=True)

    def discover(self, text):
        if 'what' in text and 'your' in text:
            if 'name' in text:
                self.respond("My name is not so smart Steven hawking")
            if 'purpose' in text or 'exist' in text:
                self.respond("The purpose of my existence is to make your life easier. Tell me what to open for you")
        if 'launch' in text or 'open' in text:
            app = text.split(' ', 1)[-1]
            openApp = app.lower()
            subprocess.call(openApp, shell=True)
