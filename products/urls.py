from django.urls import path
from .views import index, show, new, edit, delete

urlpatterns = [
    path('', index, name='list_products'),
    path('<int:product_id>', show, name='product'),
    path('<int:product_id>/edit', edit, name='edit_product'),
    path('<int:product_id>/delete', delete, name='delete_product'),
    path('new', new, name='new_product'),

]
