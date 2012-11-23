import logging
from twisted.web.resource import Resource
from md5 import md5
import json
import util


class SignIn(Resource):
    isLeaf = True
    template_HTML = util.tpl_lookup.get_template('user_signin.html')

    def __init__(self, mongodb):
        Resource.__init__(self)
        self.users = mongodb.users

    def render_GET(self, request):
        type_key = util.get_output_type_from_request(request)
        if type_key != 'HTML':
            return None
        if util.User(request.getSession()).login:
            return None
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        return self.template_HTML.render()

    def render_POST(self, request):
        logging.debug(str(request.args))
        email = str(request.args['email'][0])
        password_hash = md5(str(request.args['email'][0])).hexdigest()
        user = self.users.find_one({
            'email': email,
            'password_hash': password_hash,
            })
        util.User(request.getSession()).login = user['login']
        return 'Authenticated as %s' % user['login']
