import cherrypy as cp

class Log(object):
    def info(msg, category=None):
        if category is None:
            cp.log(msg)
        else:
            cp.log("{" + category + "} - " + msg)

@cp.popargs('game_id')
@cp.popargs('match_id')
class GameController(object):
    def __init__(self):
        self.games = {}

    @cp.expose
    @cp.tools.json_in()
    def start(self, match_id, game_id):
        if not game_id in self.games:
            self.games[game_id] = cp.request.json
            Log.info("started new game: " + game_id)
        pass

    @cp.expose
    @cp.tools.json_in()
    def end(self, match_id, game_id):
        if game_id in self.games:
            del self.games[game_id] 
            Log.info("ended game: " + game_id)
        pass

@cp.popargs('match_id')
class MatchController(object):
    def __init__(self):
        self.matches = {}

    @cp.expose
    @cp.tools.json_in()
    def start(self, match_id):
        if not match_id in self.matches:
            self.matches[match_id] = cp.request.json
            Log.info("created new match: " + match_id)
        pass

    @cp.expose
    @cp.tools.json_in()
    def end(self, match_id):
        if match_id in self.matches:
            del self.matches[match_id]
            Log.info("ended match: " + match_id)
        pass

class BotController(object):
    @cp.expose
    @cp.tools.json_out()
    def info(self):
         return {"name":"Rombot"}

class RootController(object):
    pass

root = RootController()
root.match = MatchController()
root.match.game = GameController()
root.bot = BotController()

conf = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8282,
    },
}

cp.quickstart(root, '/', conf)
