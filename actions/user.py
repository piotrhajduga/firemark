import logging
import json
from twisted.web.resource import Resource
from twisted.web.util import redirectTo
import util
from engine.userservice import UserNotFound, EmailRegistered, LoginRegistered


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
        if session.login:
            return redirectTo('/', request)
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        return self.template_HTML.render(session=session)

    def render_POST(self, request):
        type_key = util.get_output_type_from_request(request)
        session = util.Session(request.getSession())
        try:
            email = str(request.args['email'][0])
            password = str(request.args['password'][0])
            user = self.usrs.sign_in(email, password)
            session.login = user['login']
            if type_key == 'JSON':
                return json.dumps({'errno': 0, 'error': ''})
            return redirectTo('/', request)
        except UserNotFound:
            logging.warn('User not found, probably bad email address')
            if type_key == 'JSON':
                return json.dumps({'errno': 12, 'error': 'User not found'})
            session.errno = 12
            session.error = 'User not found'
            return redirectTo('/user/signin', request)


class SignUp(Resource):
    isLeaf = True
    template_HTML = util.tpl_lookup.get_template('user_signup.html')

    def __init__(self, user_service):
        Resource.__init__(self)
        self.usrs = user_service

    def render_GET(self, request):
        session = util.Session(request.getSession())
        if session.login:
            return redirectTo('/', request)
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        return self.template_HTML.render(session=session)

    def render_POST(self, request):
        type_key = util.get_output_type_from_request(request)
        session = util.Session(request.getSession())
        try:
            email = str(request.args['email'][0])
            password = str(request.args['password'][0])
            password2 = str(request.args['password2'][0])
            if password2 != password:
                raise PasswordMismatch()
            login = str(request.args['login'][0])
            self.usrs.register(email, login, password)
            return redirectTo('/', request)
        except EmailRegistered:
            logging.warn('Given email is already registered')
            session.errno = 13
            session.error = 'Given email is already registered'
        except LoginRegistered:
            logging.warn('Given login already registered')
            session.errno = 14
            session.error = 'Given login is already registered'
        except PasswordMismatch:
            logging.warn('Passwords don\'t match')
            session.errno = 15
            session.error = 'Passwords don\'t match'
        return redirectTo('/user/signup', request)
