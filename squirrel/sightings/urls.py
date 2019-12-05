from django.urls import path
from . import views

urlpatterns = [
        path('stats/',views.stats,name = 'stats'),
        path('',views.all_squirrels,name='index'),
        path('add/',views.add_sighting,name='add'),
        path('thanks/',views.thank_you,name='thanks'),
        path('no_update/',views.update_nothing,name='no_update'),
        path('success/',views.update_successful,name='success'),
        path('<str:unique_id>/',views.update_sighting,name='update'),
        path('<str:unique_id>/delete/',views.delete,name='delete'),
        ]
