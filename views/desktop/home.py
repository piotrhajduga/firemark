from twisted.web.resource import Resource
from meta import tpl_lookup
from util import Session


class HomePage(Resource):
    template_HTML = tpl_lookup.get_template('home.html')

    def render_GET(self, request):
        session = Session(request.getSession())
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        return self.template_HTML.render(session=session)
