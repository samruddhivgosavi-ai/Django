from django.contrib import admin
from django.urls import path,include

from .import views
urlpatterns = [
   path('',views.index),
   path('home/',views.home),
   path('sub/',views.sub),
   path('mul/',views.mul),
   path('registration/',views.registration),
   path('formsave/',views.formsave),
   path('viewstudents/',views.viewstudents),
   path('delete/<int:id>',views.delete),
   path('update/<int:id>',views.update),
   path('profileupdate/',views.profileupdate),
   path('login/',views.login),
   path('logincheck/',views.logincheck),
   path('logout/',views.logout),
   path('dashboard/',views.dashboard),
   path('addcookie/',views.addcookie),
   path('viewcookie/',views.viewcookie),
]