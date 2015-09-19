from django.views.generic.edit import FormView
from django.views.generic import ListView
from taggit.models import Tag
from .forms import ImageForm
from .models import Image


class UploadView(FormView):
    template_name = 'imageview/upload.html'
    form_class = ImageForm
    success_url = '/'

    def form_valid(self, form):
        form.save()

        return super(UploadView, self).form_valid(form)


class MainView(ListView):
    template_name = 'imageview/list.html'
    model = Image

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context.update({"tags": Tag.objects.all()})

        return context
