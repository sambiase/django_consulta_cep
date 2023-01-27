from django.urls import path
from .views import main_view, consulta_cep

urlpatterns = [
    path('', main_view, name='main_view'),
    path('consulta_cep/', consulta_cep, name='consulta_cep'),
   

]
