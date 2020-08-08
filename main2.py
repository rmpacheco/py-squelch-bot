import cherrypy

@cherrypy.popargs('match_id')
class Matches(object):
    def __init__(self):
        self.matches = {}

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def start(self, match_id):
        #return str( j["yourBotIndex"])
        if not match_id in self.matches:
            self.matches[match_id] = cherrypy.request.json
        pass

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def end(self, match_id):
        if match_id in self.matches:
            del self.matches[match_id]
        pass

class Bot(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def info(self):
         return {"name":"Rombot"}

class Root(object):
    pass

root = Root()
root.match = Matches()
root.bot = Bot()

conf = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8282,
    },
}

cherrypy.quickstart(root, '/', conf)
