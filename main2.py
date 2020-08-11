import cherrypy as cp

@cp.popargs('match_id')
class Matches(object):
    def __init__(self):
        self.matches = {}

    @cp.expose
    @cp.tools.json_in()
    def start(self, match_id):
        if not match_id in self.matches:
            self.matches[match_id] = cp.request.json
            cp.log("created new match: " + match_id)
        pass

    @cp.expose
    @cp.tools.json_in()
    def end(self, match_id):
        if match_id in self.matches:
            del self.matches[match_id]
            cp.log("ended match: " + match_id)
        pass

class Bot(object):
    @cp.expose
    @cp.tools.json_out()
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

cp.quickstart(root, '/', conf)
