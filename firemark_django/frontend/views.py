from django.views.generic import TemplateView


class GameView(TemplateView):
    template_name = "frontend/index.html"

    @property
    def extra_context(self):
        return {
            "title": "Firemark"
        }
