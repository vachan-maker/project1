from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("vachan",views.vachan,name="vachan"),
    path("david",views.david,name="david"),
    path("<str:name>",views.greet,name='greet')
    
]
