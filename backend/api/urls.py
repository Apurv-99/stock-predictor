from django.urls import path, include
from users import views as UserViews
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView    
from api.views import StockPredictionAPIView
urlpatterns = [
    path('register/', UserViews.RegisterView.as_view(), name='register'),


    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('predict/', StockPredictionAPIView.as_view(), name='stock_prediction')
]