from django.urls import path
from renovations.views import (
    AllProducts, ProductNew, ProductUpdate, ProductDelete, AllRooms,
    RoomNew, RoomUpdate, RoomDelete, AddProductView, AddProductToRoom, RemoveProductFromRoom)

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
    path('rooms/<int:room_id>/', AddProductView.as_view(), name='add-product-view'),
    path('room/<int:room_id>/add_product/<int:product_id>', AddProductToRoom.as_view(), name='add-product-to-room'),
    path('room/<int:room_id>/remove_product/<int:product_id>', RemoveProductFromRoom.as_view(),
         name='remove-product-from-room'),
    path('renovations/', AllRenovations.as_view(), name='all-renovations'),
]
