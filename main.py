import cherrypy

class Match(object):

    def __init__(self):
        self.id = None
        self.my_rolls = {}
        self.their_rolls = {}

    def create(self, id):
        self.id = id

class Bot(object):

    def __init__(self):
        self.matches = {}

    @cherrypy.expose
    def info(self):
        return "RomBot-1"

if __name__ == '__main__':
    bot = Bot()
    cherrypy.config.update({'server.socket_port': 8282})
    cherrypy.tree.mount(bot, '/bot', None)
    cherrypy.engine.start()
    cherrypy.engine.block()
    
