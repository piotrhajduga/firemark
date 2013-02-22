import logging
from twisted.web.resource import Resource


class SignIn(Resource):
    isLeaf = True

    def __init__(self, user_service):
        Resource.__init__(self)
        self.usrs = user_service

    def render_POST(self, request):
        session = util.Session(request.getSession())
        email = str(request.args['email'][0])
        password = str(request.args['password'][0])
        user = self.usrs.sign_in(email, password)
        session.user = user
        logging.info('Logged user: %s', session.user)
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        return json.dumps({'errno': 0, 'error': 'OK'})


class Logout(Resource):
    isLeaf = True

    def render_POST(self, request):
        request.getSession().expire()
        session = util.Session(request.getSession())
        session.user = None
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        return json.dumps({'error': 0})


class User(Resource):
    def __init__(self, user_service):
        Resource.__init__(self)
        self.putChild('signin', SignIn(user_service))
        self.putChild('logout', Logout())
