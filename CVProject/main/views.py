from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from weasyprint import HTML
from django.template.loader import render_to_string

from .models import CV

def home(request: HttpRequest):
    cv_list = CV.objects.all()
    return render(request, 'home.html', {'cv_list': cv_list})

def cv(request: HttpRequest, id: int):
    cv = get_object_or_404(CV, pk=id)
    return render(request, 'detail.html', {'cv': cv})

def render_cv_pdf(request: HttpRequest, id: int):
    # Get html
    cv = get_object_or_404(CV, pk=id)
    html_string = render_to_string('detail.html', {'cv': cv, 'pdf': True})

    # Assemble pdf response
    pdf_file = HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="CV.pdf"'

    return response