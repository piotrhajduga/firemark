from django.views.generic import TemplateView

from game.models import ActorPlayer


class GameView(TemplateView):
    template_name = "index.html"

    @property
    def extra_context(self):
        return {
            "title": "Firemark"
        }

class GameMainWidgetView(TemplateView):
    template_name = "main_widget.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            player = ActorPlayer.objects.get(user=self.request.user)
            context['location'] = player.location
        return context