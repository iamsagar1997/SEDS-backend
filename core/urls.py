from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view 
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('api/user', include('users.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('post.urls', namespace='post')),
    path('docs/', include_docs_urls(title='API')),
    path('schema', get_schema_view(
        title="API",
        description="API for the folder API",
        version="3.0.2"
    ), name='openapi-schema'),
    
]
