from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView)


urlpatterns = [
    path('authentications/tokens/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('authentications/tokens/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('authentications/tokens/verify/', TokenVerifyView.as_view(),
         name='token_verify'),
]
