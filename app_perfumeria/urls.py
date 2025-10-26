from django.urls import path
from . import views

app_name = 'app_perfumeria'
urlpatterns = [
    # Rutas para Productos (ahora la principal del sitio)
    path('', views.listar_productos, name='listar_productos'), # La raíz del sitio
    path('productos/', views.listar_productos, name='listar_productos'),
    path('producto/crear/', views.crear_producto, name='crear_producto'),
    path('producto/<int:id_producto>/', views.detalle_producto, name='detalle_producto'),
    path('producto/editar/<int:id_producto>/', views.editar_producto, name='editar_producto'),
    path('producto/borrar/<int:id_producto>/', views.borrar_producto, name='borrar_producto'),

    # Rutas para Marcas (secundarias)
    path('marcas/', views.listar_marcas, name='listar_marcas'),
    path('marca/crear/', views.crear_marca, name='crear_marca'),
    path('marca/<int:id_marca>/', views.detalle_marca, name='detalle_marca'),
    path('marca/editar/<int:id_marca>/', views.editar_marca, name='editar_marca'),
    path('marca/borrar/<int:id_marca>/', views.borrar_marca, name='borrar_marca'),
]