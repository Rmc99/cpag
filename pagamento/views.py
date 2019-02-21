from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from weasyprint import HTML
from .models import *

@login_required
def relatorio_pagamento(request):
    l = Pagamento.objects.all()
    return render(request, 'pagamento/relatorio_pagamento.html', {'lista': l})

@login_required
def gerar_pdf(request, ano):
    """Generate pdf."""
    print(ano)
    # Model data
    obj = Pagamento.objects.get(ano=ano).select_related('pessoa').all()
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