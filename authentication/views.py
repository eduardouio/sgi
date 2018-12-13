from  django.views.generic import TemplateView

class LoginTemplateView(TemplateView):
    template_name = 'base/base.html'    

    def get(self, request, *args, **kwargs):
        context = super(LoginTemplateView, self).get_context_data(*args, **kwargs)
        return self.render_to_response(context)