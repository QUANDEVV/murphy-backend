from django.urls import path, include
from rest import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import UserListCreateView, UserDetailView 
from django.contrib import admin
# from .views import VideoListCreateView
from .views import create_password, get_passwords


schema_view = get_schema_view(
    openapi.Info(
        title="aifans",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('girls/', views.girls_list, name='girls_list'),
    path('girls/<int:pk>/', views.girls_detail, name='girls_detail'),
    path('girls/name/<str:name>/', views.girl_by_name, name='girl_by_name'),  # URL pattern for fetching by name
    
    path('girls/<int:pk>/photos/', views.girls_photos, name='girls_photos'),
    path('videos/', views.video_list, name='video_list'),
    path('videos/<int:pk>/', views.video_detail, name='video_detail'),
    path('videos/girl/<int:girl_id>/', views.videos_by_girl, name='videos_by_girl'),
   
    # path('girls/<int:pk>/media/', views.girls_media, name='girls_media'), #
    
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),


    ### Creators by username you logged in with in localstorage
    path('creator/<str:username>/', views.get_creator_by_username, name='get_creator_by_username'),


    path('admin/', admin.site.urls),
    path('insights/', include('aifans.insights.urls')),
    path('chats/', include('aifans.chats.urls')),  # Updated from 'messages'
    path('moderation/', include('aifans.moderation.urls')),
    path('notifications/', include('aifans.notifications.urls')),
    path('payments/', include('aifans.payments.urls')),
    path('posts/', include('aifans.posts.urls')),
    path('profile/', include('aifans.profile.urls')),
    path('search/', include('aifans.search.urls')),
    path('subscriptions/', include('aifans.subscriptions.urls')),
    path('users/', include('aifans.user.urls')),

    path('api/get_passwords/', get_passwords, name='get_passwords'),
    # path('api/create_password/', create_password, name='create_password'),  # New URL pattern for POST
    path('api/create_password/', create_password, name='create_password'),
    #### CEO WHO HAS POWER TO MANIPULATE EVERYTHING

    path('admin1/', include('manager.admin1.urls')),





    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
