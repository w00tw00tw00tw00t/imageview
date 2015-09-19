from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import ImageForm
from .models import Image



class UploadView(FormView):
    template_name = 'imageview/upload.html'
    form_class = ImageForm
    success_url = '/'

    def form_valid(self, form):
        # try:
        form.save()
        # except ValueError as e:
        #     raise FieldError(e)
        # return self.form_invalid(form)

        return super(UploadView, self).form_valid(form)


class MainView(ListView):
    template_name = 'imageview/list.html'
    model = Image
