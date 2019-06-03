from django.urls import path
from renovations.views import (
    AllProducts, ProductNew, ProductUpdate, ProductDelete, AllRooms,
    RoomNew, RoomUpdate, RoomDelete, EditRoom)

app_name = "renovations"

urlpatterns = [
    path('products/', AllProducts.as_view(), name='all-products'),
    path('products/new/', ProductNew.as_view(), name='new-product'),
    path('products/update/<int:pk>/', ProductUpdate.as_view(), name='update-product'),
    path('products/delete/<int:pk>/', ProductDelete.as_view(), name='delete-product'),
    path('rooms/', AllRooms.as_view(), name='all-rooms'),
    path('rooms/new/', RoomNew.as_view(), name='new-room'),
    path('rooms/update/<int:pk>/', RoomUpdate.as_view(), name='update-room'),
    path('rooms/delete/<int:pk>/', RoomDelete.as_view(), name='delete-room'),
]
