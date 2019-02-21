from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from .models import *

def gerar_pdf(request):
    """Generate pdf."""
    # Model data
    obj = Pagamento.objects.all().select_related('pessoa').all()
    # Rendered
    html_string = render_to_string('pagamento/pdf_template.html', {'lista': obj})
    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/{}.pdf'.format(obj));

    fs = FileSystemStorage('/tmp')
    with fs.open('{}.pdf'.format(obj)) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(obj)
        return response

    return response