from django.urls import path
from .views import contact_list, create_contact, contact_detail, edit_contact, delete_contact

urlpatterns = [
    path('contacts/', contact_list, name='contact_list'),
    path('contacts/create/', create_contact, name='create_contact'),
    path('contacts/<int:pk>/', contact_detail, name='contact_detail'),
    path('contacts/<int:pk>/edit/', edit_contact, name='edit_contact'),
    path('contacts/<int:pk>/delete/', delete_contact, name='delete_contact'),
]