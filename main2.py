import cherrypy

@cherrypy.popargs('match_id')
class Matches(object):
    @cherrypy.expose
    @cherrypy.tools.json_in()
    def start(self, match_id):
        j = cherrypy.request.json
        return str( j["yourBotIndex"])


class Bot(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def info(self):
         return {"name":"Rombotblah"}

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
    #'/': {
    #    'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
    #},
}

cherrypy.quickstart(root, '/', conf)
