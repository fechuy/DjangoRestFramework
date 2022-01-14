from django.urls import path
from api.apiViews import ProductList, ProductDetalle     

urlpatterns = [
    path('v1/productos/', ProductList.as_view(),name='producto_list' ),
    path('v1/productos/<int:pk>', ProductDetalle.as_view(),name='producto_detalle' ),
]