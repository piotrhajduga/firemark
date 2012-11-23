from twisted.web.resource import Resource
import util


class HomePage(Resource):
    template_HTML = util.tpl_lookup.get_template('home.html')

    def render_GET(self, request):
        session = util.Session(request.getSession())
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        return self.template_HTML.render(session=session)
