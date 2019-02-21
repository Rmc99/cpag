from django.urls import path
from .views import gerar_pdf, relatorio_pagamento

app_name = 'pagamento'
urlpatterns = [
    path('pagamento/gerar_pdf', gerar_pdf, name='gerar_pdf'),
    path('pagamento/relatorio_pagamento', relatorio_pagamento, name='relatorio_pagamento'),
]