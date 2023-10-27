from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuarios
from .models import Ventas
from datetime import datetime
from django.utils.timezone import now

TEMPLATE_DIRS =(
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
    return render(request, "index.html")


def listar(request):
    if request.method == 'POST':
        palabra = request.POST.get('keyword')
        lista = Usuarios.objects.all()

        if palabra is not None:
            resultado_busqueda = lista.filter(
                Q(id__icontains=palabra) |
                Q(nombre__icontains=palabra) |
                Q(apellido__icontains=palabra) |
                Q(correo__icontains=palabra) |
                Q(telefono__icontains=palabra) |
                Q(documento__icontains=palabra)
            )
            datos = {'usuarios': resultado_busqueda}
            return render(request, "crud_usuarios/listar.html", datos)
        else:
            datos = {'usuarios': lista}
            return render(request, "crud_usuarios/listar.html", datos)
    else:
        users = Usuarios.objects.order_by('-id')[:10]
        datos = {'usuarios': users}
        return render(request, "crud_usuarios/listar.html", datos)

def agregar(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
            user = Usuarios()
            user.nombre = request.POST.get('nombre')
            user.apellido = request.POST.get('apellido')
            user.correo = request.POST.get('correo')
            user.documento = request.POST.get('documento')
            user.f_nac = request.POST.get('f_nac')           
            user.save()            
            return redirect('listar')
    else:
        return render(request, "crud_usuarios/agregar.html")

def actualizar(request, idUsuario):
    try: 
        if request.method=='POST':
            if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
                user_id_old = request.POST.get('id')
                user_old = Usuarios()
                user_old = Usuarios.objects.get(id = user_id_old)
                        
                
                user = Usuarios()
                user.id = request.POST.get('id')
                user.nombre = request.POST.get('nombre')
                user.apellido = request.POST.get('apellido')
                user.correo = request.POST.get('correo')
                user.telefono = request.POST.get('telefono')
                user.documento = request.POST.get('documento')
                user.f_nac = request.POST.get('f_nac')  
                user.f_registro = user_old.f_registro         
                user.save()            
                return redirect('listar')      
        else:
            users = Usuarios.objects.all()
            user = Usuarios.objects.get(id=idUsuario)
            datos = { 'usuarios' : users, 'usuario': user}
            return render(request, "crud_usuarios/actualizar.html", datos)
        
    except Usuarios.DoesNotExist:
        users = Usuarios.objects.all()
        user = None
        datos = { 'usuarios' : users, 'usuario': user }
        return render(request, "crud_usuarios/actualizar.html", datos)
    

def eliminar(request, idUsuario):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                tupla = Usuarios.objects.get(id = id_a_borrar)
                tupla.delete()
                return redirect('listar')
        else:        
            users = Usuarios.objects.all()
            user = Usuarios.objects.get(id = idUsuario)
            datos = { 'usuarios' : users, 'usuario': user }
            return render(request, "crud_usuarios/eliminar.html",datos)
        
    except Usuarios.DoesNotExist:
        users = Usuarios.objects.all()
        user = None
        datos =  { 'usuarios' : users, 'usuario' : user }
        return render(request, "crud_usuarios/eliminar.html",datos)    


def listar_ventas(request):
    if request.method == 'POST':
        palabra = request.POST.get('keyword')
        lista = Ventas.objects.all()

        if palabra is not None:
            resultado_busqueda = lista.filter(
                Q(id__icontains=palabra) |
                Q(nombre__icontains=palabra) |
                Q(apellido__icontains=palabra) |
                Q(correo__icontains=palabra) |
                Q(telefono__icontains=palabra) |
                Q(documento__icontains=palabra)
            )
            datos = {'ventas': resultado_busqueda}
            return render(request, "crud_ventas/listar_ventas.html", datos)
        else:
            datos = {'ventas': lista}
            return render(request, "crud_ventas/listar_ventas.html", datos)
    else:
        users = Ventas.objects.order_by('-id')[:10]
        datos = {'ventas': users}
        return render(request, "crud_ventas/listar_ventas.html", datos)

def agregar_ventas(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
            venta = Ventas()
            venta.nombre = request.POST.get('nombre')
            venta.apellido = request.POST.get('apellido')
            venta.correo = request.POST.get('correo')
            venta.documento = request.POST.get('documento')
            venta.f_nac = request.POST.get('f_nac')           
            venta.save()            
            return redirect('listar_ventas')
    else:
        return render(request, "crud_ventas/agregar_ventas.html")

def actualizar_ventas(request, idVenta):
    try: 
        if request.method=='POST':
            if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
                venta_id_old = request.POST.get('id')
                venta_old = Ventas()
                venta_old = Ventas.objects.get(id = venta_id_old)
                        
                
                venta = Ventas()
                venta.id = request.POST.get('id')
                venta.nombre = request.POST.get('nombre')
                venta.apellido = request.POST.get('apellido')
                venta.correo = request.POST.get('correo')
                venta.telefono = request.POST.get('telefono')
                venta.documento = request.POST.get('documento')
                venta.f_nac = request.POST.get('f_nac')  
                venta.f_registro = venta_old.f_registro         
                venta.save()            
                return redirect('listar_ventas')      
        else:
            ventas = Ventas.objects.all()
            venta = Ventas.objects.get(id=idVenta)
            datos = { 'ventas' : ventas, 'venta': venta}
            return render(request, "crud_ventas/actualizar_ventas.html", datos)
        
    except Ventas.DoesNotExist:
        ventas = Ventas.objects.all()
        venta = None
        datos = { 'ventas' : ventas, 'venta': venta }
        return render(request, "crud_ventas/actualizar_ventas.html", datos)
    

def eliminar_ventas(request, idVenta):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                tupla = Ventas.objects.get(id = id_a_borrar)
                tupla.delete()
                return redirect('listar_ventas')
        else:        
            ventas = Ventas.objects.all()
            venta = Ventas.objects.get(id = idVenta)
            datos = { 'ventas' : ventas, 'venta': venta }
            return render(request, "crud_ventas/eliminar_ventas.html",datos)
        
    except Ventas.DoesNotExist:
        ventas = Ventas.objects.all()
        venta = None
        datos =  { 'ventas' : ventas, 'venta' : venta }
        return render(request, "crud_ventas/eliminar_ventas.html",datos)    
    
