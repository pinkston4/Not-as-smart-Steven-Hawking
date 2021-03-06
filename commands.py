import subprocess
from answer import Fetcher


class Commander:
    """
    The Commander class determines what the user wants it to do. It will tell
    its name, tell you its purpose, look up information for you, and launch/open
    apps for you
    methods:
        __init__()
        respond()
        discover()
    """

    def __init__(self):
        self.confirm = ['yes', 'affirmative', 'sure', 'si',
                        'do it', 'gotcha', 'yeah', 'confirm']
        self.cancel = ['no', 'negative', 'negatory', 'negative soldier',
                       'wait', 'cancel', 'stop']

    @staticmethod
    def respond(response):
        """
        the respond method takes one argument. The respond method runs a subprocess
        that will output audio
        arguments:
            response = the text you want read out loud
        """
        subprocess.call('say ' + response, shell=True)

    def discover(self, text):
        """
        the discover method takes one argument. The discover method determines
        what happens next with a user command. Whether it be responding with
        info about itself, running the command as a subprocess, searching google
        for an answer to user command, or returning if answer is was not properly understood
        argument:
            text = user spoken command
        """
        if 'what' in text and 'your' in text:
            if 'name' in text:
                self.respond("My name is not so smart Steven hawking")
            if 'purpose' in text or 'exist' in text:
                self.respond("The purpose of my existence is to make your life easier. Tell me what to do.")
        elif 'launch' in text or 'open' in text:
            app = text.split(' ', 1)[-1]
            open_app = app.lower()
            subprocess.call(open_app, shell=True)
        else:
            f = Fetcher('https://www.google.com/#q=' + text)
            answer = f.lookup()
            if answer is None:
                return
            else:
                self.respond(answer)
