from django.shortcuts import render, get_object_or_404, redirect
from .models import Marca, Producto
from .forms import MarcaForm, ProductoForm

# Vistas para Marcas
def listar_marcas(request):
    marcas = Marca.objects.all()
    return render(request, 'listar_marcas.html', {'marcas': marcas})

def detalle_marca(request, id_marca):
    marca = get_object_or_404(Marca, id_marca=id_marca)
    productos_marca = Producto.objects.filter(id_marca=marca)
    return render(request, 'detalle_marca.html', {'marca': marca, 'productos_marca': productos_marca})

def crear_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_perfumeria:listar_marcas')
    else:
        form = MarcaForm()
    return render(request, 'formulario_marca.html', {'form': form, 'titulo': 'Crear Marca'})

def editar_marca(request, id_marca):
    marca = get_object_or_404(Marca, id_marca=id_marca)
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('app_perfumeria:detalle_marca', id_marca=marca.id_marca)
    else:
        form = MarcaForm(instance=marca)
    return render(request, 'formulario_marca.html', {'form': form, 'titulo': 'Editar Marca'})

def borrar_marca(request, id_marca):
    marca = get_object_or_404(Marca, id_marca=id_marca)
    if request.method == 'POST':
        marca.delete()
        return redirect('app_perfumeria:listar_marcas')
    return render(request, 'confirmar_borrar_marca.html', {'marca': marca})

# Vistas para Productos (Principal)
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def detalle_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    return render(request, 'detalle_producto.html', {'producto': producto})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_perfumeria:listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'formulario_producto.html', {'form': form, 'titulo': 'Crear Producto'})

def editar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('app_perfumeria:detalle_producto', id_producto=producto.id_producto)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'formulario_producto.html', {'form': form, 'titulo': 'Editar Producto'})

def borrar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('app_perfumeria:listar_productos')
    return render(request, 'confirmar_borrar.html', {'producto': producto})