from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from weasyprint import HTML
from django.template.loader import render_to_string
from rest_framework.viewsets import ModelViewSet


from .models import CV
from .serializers import CVSerializer
from .forms import SendPDFForm, TranslateForm
from .tasks import senf_pdf
from .translation import *

def home(request: HttpRequest):
    cv_list = CV.objects.all()
    return render(request, 'home.html', {'cv_list': cv_list})

def cv(request: HttpRequest, id: int):
    cv = get_object_or_404(CV, pk=id)
    language = request.GET.get('language')
    translated_content = handle_translation(cv, language)

    if request.method == 'POST':
        form = SendPDFForm(request.POST)
        if form.is_valid():
            to_email = form.cleaned_data['email']
            html_string = render_to_string('detail.html', {'cv': cv, 'pdf': True, 'translated_content': translated_content})
            pdf_file = HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf()
            senf_pdf.delay(to_email, pdf_file)
            return redirect('cv', id=id)
    else:
        form = SendPDFForm()

    translate_form = TranslateForm(initial={'language': language})

    return render(
        request,
        'detail.html',
        {
            'cv': cv,
            'form': form,
            'translate_form': translate_form,
            'translated_content': translated_content,
            'selected_language': language
        }
    )


def render_cv_pdf(request: HttpRequest, id: int):
    # Get html
    cv = get_object_or_404(CV, pk=id)
    language = request.GET.get('language')
    translated_content = handle_translation(cv, language)
    html_string = render_to_string('detail.html', {'cv': cv, 'pdf': True, 'translated_content': translated_content})

    # Assemble pdf response
    pdf_file = HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="CV.pdf"'

    return response

# CV CRUD API
class CVViewSet(ModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializer

def settings_view(request: HttpRequest):
    return render(request, 'settings.html')

