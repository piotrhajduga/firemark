import logging
from twisted.web.resource import Resource
from twisted.web.util import redirectTo, Redirect
from meta import tpl_lookup
from util import Session


class SignIn(Resource):
    isLeaf = True
    template_HTML = tpl_lookup.get_template('user_signin.html')

    def __init__(self, user_service):
        Resource.__init__(self)
        self.usrs = user_service

    def render_GET(self, request):
        session = Session(request.getSession())
        if session.user:
            logging.info('User already signed in. Redirecting to homepage.')
            return redirectTo('/', request)
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        return self.template_HTML.render(session=session)

    def render_POST(self, request):
        session = Session(request.getSession())
        email = str(request.args['email'][0])
        password = str(request.args['password'][0])
        user = self.usrs.sign_in(email, password)
        session.user = user
        logging.info('Logged user: %s', session.user)
        return redirectTo('/', request)


class Logout(Resource):
    isLeaf = True

    def render_POST(self, request):
        request.getSession().expire()
        session = Session(request.getSession())
        session.user = None
        return redirectTo('/', request)


class SignUp(Resource):
    isLeaf = True
    template_HTML = tpl_lookup.get_template('user_signup.html')

    def __init__(self, user_service):
        Resource.__init__(self)
        self.usrs = user_service

    def render_GET(self, request):
        session = Session(request.getSession())
        if session.user:
            return redirectTo('/', request)
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        return self.template_HTML.render(session=session)

    def render_POST(self, request):
        session = Session(request.getSession())
        email = str(request.args['email'][0])
        password = str(request.args['password'][0])
        password2 = str(request.args['password2'][0])
        if password2 != password:
            logging.warn('Passwords don\'t match')
            session.errno, session.error = 15, 'Passwords don\'t match'
            return redirectTo('/', request)
        login = str(request.args['login'][0])
        self.usrs.register(email, login, password)
        return redirectTo('/user/signin', request)


class User(Resource):
    def __init__(self, user_service):
        Resource.__init__(self)
        self.putChild('signin', SignIn(user_service))
        self.putChild('signup', SignUp(user_service))
        self.putChild('logout', Logout())
        self.putChild('', Redirect('/'))

    def render_GET(self, request):
        return redirectTo('/', request)
