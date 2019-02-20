from django.urls import path
from .views import gerar_pdf

app_name = 'pagamento'
urlpatterns = [
    path('pagamento/gerar_pdf', gerar_pdf, name='gerar_pdf'),
]