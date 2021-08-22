from django.urls import path
from personas import views as vista

app_name = 'apps'

urlpatterns = [
    path('', vista.inicio , name='inicio'),
    path('detail<int:id>/' , vista.detail, name='detail'),
    path('crear_persona/', vista.crear_persona , name='crear_person<a'),
    path('update<int:id>/', vista.actualizar_persona, name='update'),
    path('delete<int:id>/', vista.borrar_persona, name='delete')

]
