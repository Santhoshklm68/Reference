from django.urls import path, include
from app.routes import router

urlpatterns = [
   
    path('', include(router.urls), name="app" )
    
]
