from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('movie/',views.movie,name='movie'),
    path('<int:pk>/',views.MovieDetail,name='moviedetail'),
    path('signup/',views.user_signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('favourite/',views.favourites,name='favourites'),
    path('add_fav/<int:pk>/',views.add_to_favourites,name='add_fav'),
    path('remove_fav/<int:pk>/',views.remove_from_favourites,name='remove_fav'),
    path('search/',views.search_result,name='search'),
    path('logout/',views.user_logout,name='logout')
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
