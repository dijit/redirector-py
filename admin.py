from rivr.views import TemplateView

class Admin(TemplateView):
    template_name = 'admin.html'

    def get_context_data(self, **kwargs):
        return{'hostnames': self.connection}


