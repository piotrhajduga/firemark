from twisted.web.resource import Resource
from actions.desktop import tpl_lookup


class HomePage(Resource):
    template_HTML = tpl_lookup.get_template('home.html')

    def render_GET(self, request):
        session = util.Session(request.getSession())
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        return self.template_HTML.render(session=session)
