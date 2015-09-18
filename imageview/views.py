from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Imageview
from .forms import ImageviewForm

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = ImageviewForm(request.POST, request.FILES)
        if form.is_valid():
            newimage = Imageview(imagefile = request.FILES['imagefile'])
            newimage.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('imageview.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    images = Imageview.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'imageview/list.html',
        {'images': images, 'form': form},
        context_instance=RequestContext(request)
    )