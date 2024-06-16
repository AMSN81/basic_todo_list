from django.contrib import admin
from django.urls import include, path
from Goals.views import NewTodoAPI,TodoDetailAPI
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Django Admin Panel
    path('admin/', admin.site.urls),

    # Authentication
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Todo
    path('api/v1/todo/new', NewTodoAPI.as_view(), name='todo-new'),
    path('api/v1/todo/<int:pk>/', TodoDetailAPI.as_view(), name='todo-detail'),
]
