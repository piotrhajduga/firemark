import logging
from twisted.web.resource import Resource
from twisted.web.util import redirectTo, Redirect
import util


class PasswordMismatch(Exception):
    pass


class SignIn(Resource):
    isLeaf = True
    template_HTML = util.tpl_lookup.get_template('user_signin.html')

    def __init__(self, user_service):
        Resource.__init__(self)
        self.usrs = user_service

    def render_GET(self, request):
        session = util.Session(request.getSession())
        if session.user:
            logging.info('User already signed in. Redirecting to homepage.')
            return redirectTo('/', request)
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        return self.template_HTML.render(session=session)

    def render_POST(self, request):
        session = util.Session(request.getSession())
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
        sessiot = util.Session(request.getSession())
        session.user = None
        return redirectTo('/', request)


class SignUp(Resource):
    isLeaf = True
    template_HTML = util.tpl_lookup.get_template('user_signup.html')

    def __init__(self, user_service):
        Resource.__init__(self)
        self.usrs = user_service

    def render_GET(self, request):
        session = util.Session(request.getSession())
        if session.user:
            return redirectTo('/', request)
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        return self.template_HTML.render(session=session)

    def render_POST(self, request):
        type_key = util.get_output_type_from_request(request)
        session = util.Session(request.getSession())
        errinfo = {'errno': 0, 'error': None}
        try:
            email = str(request.args['email'][0])
            password = str(request.args['password'][0])
            password2 = str(request.args['password2'][0])
            if password2 != password:
                raise PasswordMismatch()
            login = str(request.args['login'][0])
            self.usrs.register(email, login, password)
        except PasswordMismatch:
            logging.warn('Passwords don\'t match')
            errinfo['errno'], errinfo['error'] = 15, 'Passwords don\'t match'
        if type_key == 'JSON':
            request.setHeader("Content-Type", "text/html; charset=utf-8")
            return json.dumps(errinfo)
        if errinfo['errno']:
            session.errno, session.error = errinfo['errno'], errinfo['error']
            return redirectTo('/', request)
        return redirectTo('/user/signup', request)


class User(Resource):
    def __init__(self, user_service):
        Resource.__init__(self)
        self.putChild('signin', SignIn(user_service))
        self.putChild('signup', SignUp(user_service))
        self.putChild('logout', Logout())
        self.putChild('', Redirect('/'))

    def render_GET(self, request):
        return redirectTo('/', request)
