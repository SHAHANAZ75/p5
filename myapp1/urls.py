from django.urls import path
from myapp1 import views
app_name="myapp1"# is used to create a namespace

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('fact/<n>',views.fact,name='fact'),
    #path("secondarysuffix",address of function,name of mapping)
    path('parent',views.parent,name='parent'),
    path('child',views.child,name='child'),
]
