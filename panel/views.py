from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuarios
from .models import Ventas
from .models import Anuncios
from .models import Asistencia
from .models import Campana
from .models import Cartera
from .models import Direccion
from .models import Estado
from .models import Modalidad
from .models import Observacion
from .models import Operador
from .models import Paquete_Movil
from .models import Potencia
from .models import Segmento
from .models import Tarifa
from .models import Tecnologia
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
        ventas = Ventas.objects.order_by('-id')[:10]
        datos = {'ventas': ventas}
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
    
    
def listar_anuncios(request):
    if request.method == 'POST':
        palabra = request.POST.get('keyword')
        lista = Anuncios.objects.all()

        if palabra is not None:
            resultado_busqueda = lista.filter(
                Q(id__icontains=palabra) |
                Q(nombre__icontains=palabra) |
                Q(apellido__icontains=palabra) |
                Q(correo__icontains=palabra) |
                Q(telefono__icontains=palabra) |
                Q(documento__icontains=palabra)
            )
            datos = {'anuncios': resultado_busqueda}
            return render(request, "crud_anuncios/listar_anuncios.html", datos)
        else:
            datos = {'anuncios': lista}
            return render(request, "crud_anuncios/listar_anuncios.html", datos)
    else:
        anuncios = Anuncios.objects.order_by('-id')[:10]
        datos = {'anuncios': anuncios}
        return render(request, "crud_anuncios/listar_anuncios.html", datos)

def agregar_anuncios(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
            anuncio = Anuncios()
            anuncio.nombre = request.POST.get('nombre')
            anuncio.apellido = request.POST.get('apellido')
            anuncio.correo = request.POST.get('correo')
            anuncio.documento = request.POST.get('documento')
            anuncio.f_nac = request.POST.get('f_nac')           
            anuncio.save()            
            return redirect('listar_anuncios')
    else:
        return render(request, "crud_anuncios/agregar_anuncios.html")

def actualizar_anuncios(request, idAnuncio):
    try: 
        if request.method=='POST':
            if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
                anuncio_id_old = request.POST.get('id')
                anuncio_old = Anuncios()
                anuncio_old = Anuncios.objects.get(id = anuncio_id_old)
                        
                
                anuncio = Anuncios()
                anuncio.id = request.POST.get('id')
                anuncio.nombre = request.POST.get('nombre')
                anuncio.apellido = request.POST.get('apellido')
                anuncio.correo = request.POST.get('correo')
                anuncio.telefono = request.POST.get('telefono')
                anuncio.documento = request.POST.get('documento')
                anuncio.f_nac = request.POST.get('f_nac')  
                anuncio.f_registro = anuncio_old.f_registro         
                anuncio.save()            
                return redirect('listar_anuncios')      
        else:
            anuncios = Anuncios.objects.all()
            anuncio = Anuncios.objects.get(id=idAnuncio)
            datos = { 'anuncios' : anuncios, 'anuncio': anuncio}
            return render(request, "crud_anuncios/actualizar_anuncios.html", datos)
        
    except Anuncios.DoesNotExist:
        anuncios = Anuncios.objects.all()
        anuncio = None
        datos = { 'anuncios' : anuncios, 'anuncio': anuncio }
        return render(request, "crud_anuncios/actualizar_anuncios.html", datos)
    

def eliminar_anuncios(request, idAnuncio):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                tupla = Anuncios.objects.get(id = id_a_borrar)
                tupla.delete()
                return redirect('listar_anuncios')
        else:        
            anuncios = Anuncios.objects.all()
            anuncio = Anuncios.objects.get(id = idAnuncio)
            datos = { 'anuncios' : anuncios, 'anuncio': anuncio }
            return render(request, "crud_anuncios/eliminar_anuncios.html",datos)
        
    except Anuncios.DoesNotExist:
        anuncios = Anuncios.objects.all()
        anuncio = None
        datos =  { 'anuncios' : anuncios, 'anuncio' : anuncio }
        return render(request, "crud_anuncios/eliminar_anuncios.html",datos)  


def listar_asistencia(request):
    if request.method == 'POST':
        palabra = request.POST.get('keyword')
        lista =Asistencia.objects.all()

        if palabra is not None:
            resultado_busqueda = lista.filter(
                Q(id__icontains=palabra) |
                Q(nombre__icontains=palabra) |
                Q(apellido__icontains=palabra) |
                Q(correo__icontains=palabra) |
                Q(telefono__icontains=palabra) |
                Q(documento__icontains=palabra)
            )
            datos = {'asistencia': resultado_busqueda}
            return render(request, "crud_asistencia/listar_asistencia.html", datos)
        else:
            datos = {'asistencia': lista}
            return render(request, "crud_asistencia/listar_asistencia.html", datos)
    else:
        asistencia = Asistencia.objects.order_by('-id')[:10]
        datos = {'asistencia': asistencia}
        return render(request, "crud_asistencia/listar_asistencia.html", datos)

def agregar_asistencia(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
            asistencia = Asistencia()
            asistencia.nombre = request.POST.get('nombre')
            asistencia.apellido = request.POST.get('apellido')
            asistencia.correo = request.POST.get('correo')
            asistencia.documento = request.POST.get('documento')
            asistencia.f_nac = request.POST.get('f_nac')           
            asistencia.save()            
            return redirect('listar_asistencia')
    else:
        return render(request, "crud_asistencia/agregar_asistencia.html")

def actualizar_asistencia(request, idAsistencia):
    try: 
        if request.method=='POST':
            if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
                asistencia_id_old = request.POST.get('id')
                asistencia_old = Asistencia()
                asistencia_old = Asistencia.objects.get(id = asistencia_id_old)
                        
                
                asistencia = Asistencia()
                asistencia.id = request.POST.get('id')
                asistencia.nombre = request.POST.get('nombre')
                asistencia.apellido = request.POST.get('apellido')
                asistencia.correo = request.POST.get('correo')
                asistencia.telefono = request.POST.get('telefono')
                asistencia.documento = request.POST.get('documento')
                asistencia.f_nac = request.POST.get('f_nac')  
                asistencia.f_registro = asistencia_old.f_registro         
                asistencia.save()            
                return redirect('listar_asistencia')      
        else:
            asistencias = Asistencia.objects.all()
            asistencia = Asistencia.objects.get(id=idAsistencia)
            datos = { 'asistencias' : asistencias, 'asistencia': asistencia}
            return render(request, "crud_asistencia/actualizar_asistencia.html", datos)
        
    except Asistencia.DoesNotExist:
        asistencias = Asistencia.objects.all()
        asistencia = None
        datos = { 'asistencias' : asistencias, 'asistencia': asistencia }
        return render(request, "crud_asistencia/actualizar_asistencia.html", datos)
    

def eliminar_asistencia(request, idAsistencia):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                tupla = Asistencia.objects.get(id = id_a_borrar)
                tupla.delete()
                return redirect('listar_asistencia')
        else:        
            asistencias = Asistencia.objects.all()
            asistencia = Asistencia.objects.get(id = idAsistencia)
            datos = { 'asistenciaS' : asistencias, 'asistencia': asistencia }
            return render(request, "crud_asistencia/eliminar_asistencia.html",datos)
        
    except Asistencia.DoesNotExist:
        asistencias = Asistencia.objects.all()
        asistencia = None
        datos =  { 'asistencias' : asistencias, 'asistencia' : asistencia }
        return render(request, "crud_asistencia/eliminar_asistencia.html",datos)  


def listar_campana(request):
    if request.method == 'POST':
        palabra = request.POST.get('keyword')
        lista = Campana.objects.all()

        if palabra is not None:
            resultado_busqueda = lista.filter(
                Q(id__icontains=palabra) |
                Q(nombre__icontains=palabra) |
                Q(apellido__icontains=palabra) |
                Q(correo__icontains=palabra) |
                Q(telefono__icontains=palabra) |
                Q(documento__icontains=palabra)
            )
            datos = {'campana': resultado_busqueda}
            return render(request, "crud_campana/listar_campana.html", datos)
        else:
            datos = {'campana': lista}
            return render(request, "crud_campana/listar_campana.html", datos)
    else:
        campana = Campana.objects.order_by('-id')[:10]
        datos = {'campana': campana}
        return render(request, "crud_campana/listar_campana.html", datos)

def agregar_campana(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
            campana = Campana()
            campana.nombre = request.POST.get('nombre')
            campana.apellido = request.POST.get('apellido')
            campana.correo = request.POST.get('correo')
            campana.documento = request.POST.get('documento')
            campana.f_nac = request.POST.get('f_nac')           
            campana.save()            
            return redirect('listar_campana')
    else:
        return render(request, "crud_campana/agregar_campana.html")

def actualizar_campana(request, idCampana):
    try: 
        if request.method=='POST':
            if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
                campana_id_old = request.POST.get('id')
                campana_old = Campana()
                campana_old = Campana.objects.get(id = campana_id_old)
                        
                
                campana = Campana()
                campana.id = request.POST.get('id')
                campana.nombre = request.POST.get('nombre')
                campana.apellido = request.POST.get('apellido')
                campana.correo = request.POST.get('correo')
                campana.telefono = request.POST.get('telefono')
                campana.documento = request.POST.get('documento')
                campana.f_nac = request.POST.get('f_nac')  
                campana.f_registro = campana_old.f_registro         
                campana.save()            
                return redirect('listar_campana')      
        else:
            campanas = Campana.objects.all()
            campana = Campana.objects.get(id=idCampana)
            datos = { 'campanas' : campanas, 'campana': campana}
            return render(request, "crud_campana/actualizar_campana.html", datos)
        
    except Campana.DoesNotExist:
        campanas = Campana.objects.all()
        campana = None
        datos = { 'campanas' : campanas, 'campana': campana }
        return render(request, "crud_campana/actualizar_campana.html", datos)
    

def eliminar_campana(request, idCampana):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                tupla = Campana.objects.get(id = id_a_borrar)
                tupla.delete()
                return redirect('listar_campana')
        else:        
            campanas = Campana.objects.all()
            campana = Campana.objects.get(id = idCampana)
            datos = { 'campanas' : campanas, 'campana': campana }
            return render(request, "crud_campana/eliminar_campana.html",datos)
        
    except Campana.DoesNotExist:
        campanas = Campana.objects.all()
        campana = None
        datos =  { 'campanas' : campanas, 'campana' : campana }
        return render(request, "crud_campana/eliminar_campana.html",datos)  

    
def listar_cartera(request):
    if request.method == 'POST':
        palabra = request.POST.get('keyword')
        lista = Cartera.objects.all()

        if palabra is not None:
            resultado_busqueda = lista.filter(
                Q(id__icontains=palabra) |
                Q(nombre__icontains=palabra) |
                Q(apellido__icontains=palabra) |
                Q(correo__icontains=palabra) |
                Q(telefono__icontains=palabra) |
                Q(documento__icontains=palabra)
            )
            datos = {'cartera': resultado_busqueda}
            return render(request, "crud_cartera/listar_cartera.html", datos)
        else:
            datos = {'cartera': lista}
            return render(request, "crud_cartera/listar_cartera.html", datos)
    else:
        carteras = Cartera.objects.order_by('-id')[:10]
        datos = {'cartera': carteras}
        return render(request, "crud_cartera/listar_cartera.html", datos)

def agregar_cartera(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
            cartera = cartera()
            cartera.nombre = request.POST.get('nombre')
            cartera.apellido = request.POST.get('apellido')
            cartera.correo = request.POST.get('correo')
            cartera.documento = request.POST.get('documento')
            cartera.f_nac = request.POST.get('f_nac')           
            cartera.save()            
            return redirect('listar_cartera')
    else:
        return render(request, "crud_cartera/agregar_cartera.html")

def actualizar_cartera(request, idCartera):
    try: 
        if request.method=='POST':
            if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
                cartera_id_old = request.POST.get('id')
                cartera_old = Cartera()
                cartera_old = Cartera.objects.get(id = cartera_id_old)
                        
                
                cartera = Cartera()
                cartera.id = request.POST.get('id')
                cartera.nombre = request.POST.get('nombre')
                cartera.apellido = request.POST.get('apellido')
                cartera.correo = request.POST.get('correo')
                cartera.telefono = request.POST.get('telefono')
                cartera.documento = request.POST.get('documento')
                cartera.f_nac = request.POST.get('f_nac')  
                cartera.f_registro = cartera_old.f_registro         
                cartera.save()            
                return redirect('listar_cartera')      
        else:
            carteras = Cartera.objects.all()
            cartera = Cartera.objects.get(id=idCartera)
            datos = { 'carteras' : carteras, 'cartera': cartera}
            return render(request, "crud_cartera/actualizar_cartera.html", datos)
        
    except Cartera.DoesNotExist:
        carteras = Cartera.objects.all()
        cartera = None
        datos = { 'carteras' : carteras, 'cartera': cartera }
        return render(request, "crud_cartera/actualizar_cartera.html", datos)
    

def eliminar_cartera(request, idCartera):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                tupla = Cartera.objects.get(id = id_a_borrar)
                tupla.delete()
                return redirect('listar_cartera')
        else:        
            carteras = Cartera.objects.all()
            cartera = Cartera.objects.get(id = idCartera)
            datos = { 'carteras' : carteras, 'cartera': cartera }
            return render(request, "crud_cartera/eliminar_cartera.html",datos)
        
    except Cartera.DoesNotExist:
        carteras = Cartera.objects.all()
        cartera = None
        datos =  { 'carteras' : carteras, 'cartera' : cartera }
        return render(request, "crud_cartera/eliminar_cartera.html",datos)  



def listar_direccion(request):
    if request.method == 'POST':
        palabra = request.POST.get('keyword')
        lista = Direccion.objects.all()

        if palabra is not None:
            resultado_busqueda = lista.filter(
                Q(id__icontains=palabra) |
                Q(nombre__icontains=palabra) |
                Q(apellido__icontains=palabra) |
                Q(correo__icontains=palabra) |
                Q(telefono__icontains=palabra) |
                Q(documento__icontains=palabra)
            )
            datos = {'direccion': resultado_busqueda}
            return render(request, "crud_direccion/listar_direccion.html", datos)
        else:
            datos = {'direccion': lista}
            return render(request, "crud_direccion/listar_direccion.html", datos)
    else:
        direcciones = Direccion.objects.order_by('-id')[:10]
        datos = {'direccion': direcciones}
        return render(request, "crud_direccion/listar_direccion.html", datos)

def agregar_direccion(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
            direccion = Direccion()
            direccion.nombre = request.POST.get('nombre')
            direccion.apellido = request.POST.get('apellido')
            direccion.correo = request.POST.get('correo')
            direccion.documento = request.POST.get('documento')
            direccion.f_nac = request.POST.get('f_nac')           
            direccion.save()            
            return redirect('listar_direccion')
    else:
        return render(request, "crud_direccion/agregar_direccion.html")

def actualizar_direccion(request, idDireccion):
    try: 
        if request.method=='POST':
            if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
                direccion_id_old = request.POST.get('id')
                direccion_old = Direccion()
                direccion_old = Direccion.objects.get(id = direccion_id_old)
                        
                
                direccion = Direccion()
                direccion.id = request.POST.get('id')
                direccion.nombre = request.POST.get('nombre')
                direccion.apellido = request.POST.get('apellido')
                direccion.correo = request.POST.get('correo')
                direccion.telefono = request.POST.get('telefono')
                direccion.documento = request.POST.get('documento')
                direccion.f_nac = request.POST.get('f_nac')  
                direccion.f_registro =direccion_old.f_registro         
                direccion.save()            
                return redirect('listar_direccion')      
        else:
            direcciones = Direccion.objects.all()
            direccion = Direccion.objects.get(id=idDireccion)
            datos = { 'direcciones' : direcciones, 'direccion': direccion}
            return render(request, "crud_direccion/actualizar_direccion.html", datos)
        
    except Direccion.DoesNotExist:
        direcciones = Direccion.objects.all()
        direccion = None
        datos = { 'direcciones' : direcciones, 'direccion': direccion }
        return render(request, "crud_direccion/actualizar_direccion.html", datos)
    

def eliminar_direccion(request, idDireccion):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                tupla = Direccion.objects.get(id = id_a_borrar)
                tupla.delete()
                return redirect('listar_direccion')
        else:        
            direcciones = Direccion.objects.all()
            direccion = Direccion.objects.get(id = idDireccion)
            datos = { 'direcciones' : direcciones, 'direccion': direccion }
            return render(request, "crud_direccion/eliminar_direccion.html",datos)
        
    except Direccion.DoesNotExist:
        direcciones = Direccion.objects.all()
        direccion = None
        datos =  { 'direcciones' : direcciones, 'direccion' : direccion }
        return render(request, "crud_direccion/eliminar_direccion.html",datos)  

    
def listar_estado(request):
    if request.method == 'POST':
        palabra = request.POST.get('keyword')
        lista = Estado.objects.all()

        if palabra is not None:
            resultado_busqueda = lista.filter(
                Q(id__icontains=palabra) |
                Q(nombre__icontains=palabra) |
                Q(apellido__icontains=palabra) |
                Q(correo__icontains=palabra) |
                Q(telefono__icontains=palabra) |
                Q(documento__icontains=palabra)
            )
            datos = {'estado': resultado_busqueda}
            return render(request, "crud_estado/listar_estado.html", datos)
        else:
            datos = {'estado': lista}
            return render(request, "crud_estado/listar_estado.html", datos)
    else:
        estados = Estado.objects.order_by('-id')[:10]
        datos = {'estado': estados}
        return render(request, "crud_estado/listar_estado.html", datos)

def agregar_estado(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
            estado = Estado()
            estado.nombre = request.POST.get('nombre')
            estado.apellido = request.POST.get('apellido')
            estado.correo = request.POST.get('correo')
            estado.documento = request.POST.get('documento')
            estado.f_nac = request.POST.get('f_nac')           
            estado.save()            
            return redirect('listar_estado')
    else:
        return render(request, "crud_estado/agregar_estado.html")

def actualizar_estado(request, idEstado):
    try: 
        if request.method=='POST':
            if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
                estado_id_old = request.POST.get('id')
                estado_old = Estado()
                estado_old = Estado.objects.get(id = estado_id_old)
                        
                
                estado = Estado()
                estado.id = request.POST.get('id')
                estado.nombre = request.POST.get('nombre')
                estado.apellido = request.POST.get('apellido')
                estado.correo = request.POST.get('correo')
                estado.telefono = request.POST.get('telefono')
                estado.documento = request.POST.get('documento')
                estado.f_nac = request.POST.get('f_nac')  
                estado.f_registro =estado_old.f_registro         
                estado.save()            
                return redirect('listar_estado')      
        else:
            estados = Estado.objects.all()
            estado = Estado.objects.get(id=idEstado)
            datos = { 'estados' : estados, 'estado': estado}
            return render(request, "crud_estado/actualizar_estado.html", datos)
        
    except Estado.DoesNotExist:
        estados = Estado.objects.all()
        estado = None
        datos = { 'estados' : estados, 'estado': estado }
        return render(request, "crud_estado/actualizar_estado.html", datos)
    

def eliminar_estado(request, idEstado):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                tupla = Estado.objects.get(id = id_a_borrar)
                tupla.delete()
                return redirect('listar_estado')
        else:        
            estados = Estado.objects.all()
            estado = Estado.objects.get(id = idEstado)
            datos = { 'estados' : estados, 'estado': estado }
            return render(request, "crud_estado/eliminar_estado.html",datos)
        
    except Estado.DoesNotExist:
        estados = Estado.objects.all()
        estado = None
        datos =  { 'estados' : estados, 'estado' : estado }
        return render(request, "crud_estado/eliminar_estado.html",datos)  


def listar_modalidad(request):
    if request.method == 'POST':
        palabra = request.POST.get('keyword')
        lista = Modalidad.objects.all()

        if palabra is not None:
            resultado_busqueda = lista.filter(
                Q(id__icontains=palabra) |
                Q(nombre__icontains=palabra) |
                Q(apellido__icontains=palabra) |
                Q(correo__icontains=palabra) |
                Q(telefono__icontains=palabra) |
                Q(documento__icontains=palabra)
            )
            datos = {'modalidad': resultado_busqueda}
            return render(request, "crud_modalidad/listar_modalidad.html", datos)
        else:
            datos = {'modalidad': lista}
            return render(request, "crud_modalidad/listar_modalidad.html", datos)
    else:
        modalidades = Modalidad.objects.order_by('-id')[:10]
        datos = {'modalidad': modalidades}
        return render(request, "crud_modalidad/listar_modalidad.html", datos)

def agregar_modalidad(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
            modalidad = Modalidad()
            modalidad.nombre = request.POST.get('nombre')
            modalidad.apellido = request.POST.get('apellido')
            modalidad.correo = request.POST.get('correo')
            modalidad.documento = request.POST.get('documento')
            modalidad.f_nac = request.POST.get('f_nac')           
            modalidad.save()            
            return redirect('listar_modalidad')
    else:
        return render(request, "crud_modalidad/agregar_modalidad.html")

def actualizar_modalidad(request, idModalidad):
    try: 
        if request.method=='POST':
            if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
                modalidad_id_old = request.POST.get('id')
                modalidad_old = Modalidad()
                modalidad_old = Modalidad.objects.get(id = modalidad_id_old)
                        
                
                modalidad = Modalidad()
                modalidad.id = request.POST.get('id')
                modalidad.nombre = request.POST.get('nombre')
                modalidad.apellido = request.POST.get('apellido')
                modalidad.correo = request.POST.get('correo')
                modalidad.telefono = request.POST.get('telefono')
                modalidad.documento = request.POST.get('documento')
                modalidad.f_nac = request.POST.get('f_nac')  
                modalidad.f_registro =modalidad_old.f_registro         
                modalidad.save()            
                return redirect('listar_modalidad')      
        else:
            modalidades = Modalidad.objects.all()
            modalidad = Modalidad.objects.get(id=idModalidad)
            datos = { 'modalidades' : modalidades, 'modalidad': modalidad}
            return render(request, "crud_modalidad/actualizar_modalidad.html", datos)
        
    except Modalidad.DoesNotExist:
        modalidades = Modalidad.objects.all()
        modalidad = None
        datos = { 'modalidades' : modalidades, 'modalidad': modalidad }
        return render(request, "crud_modalidad/actualizar_modalidad.html", datos)
    

def eliminar_modalidad(request, idModalidad):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                tupla = Modalidad.objects.get(id = id_a_borrar)
                tupla.delete()
                return redirect('listar_modalidad')
        else:        
            modalidades = Modalidad.objects.all()
            modalidad = Modalidad.objects.get(id = idModalidad)
            datos = { 'modalidades' : modalidades, 'modalidad': modalidad }
            return render(request, "crud_modalidad/eliminar_modalidad.html",datos)
        
    except Modalidad.DoesNotExist:
        modalidades = Modalidad.objects.all()
        modalidad = None
        datos =  { 'modalidades' : modalidades, 'modalidad' : modalidad }
        return render(request, "crud_modalidad/eliminar_modalidad.html",datos)  
    

def listar_observacion(request):
    if request.method == 'POST':
        palabra = request.POST.get('keyword')
        lista = Observacion.objects.all()

        if palabra is not None:
            resultado_busqueda = lista.filter(
                Q(id__icontains=palabra) |
                Q(nombre__icontains=palabra) |
                Q(apellido__icontains=palabra) |
                Q(correo__icontains=palabra) |
                Q(telefono__icontains=palabra) |
                Q(documento__icontains=palabra)
            )
            datos = {'observacion': resultado_busqueda}
            return render(request, "crud_observacion/listar_observacion.html", datos)
        else:
            datos = {'observacion': lista}
            return render(request, "crud_observacion/listar_observacion.html", datos)
    else:
        observaciones = Observacion.objects.order_by('-id')[:10]
        datos = {'observacion': observaciones}
        return render(request, "crud_observacion/listar_observacion.html", datos)

def agregar_observacion(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
            observacion = Observacion()
            observacion.nombre = request.POST.get('nombre')
            observacion.apellido = request.POST.get('apellido')
            observacion.correo = request.POST.get('correo')
            observacion.documento = request.POST.get('documento')
            observacion.f_nac = request.POST.get('f_nac')           
            observacion.save()            
            return redirect('listar_observacion')
    else:
        return render(request, "crud_observacion/agregar_observacion.html")

def actualizar_observacion(request, idObservacion):
    try: 
        if request.method=='POST':
            if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
                observacion_id_old = request.POST.get('id')
                observacion_old = Observacion()
                observacion_old = Observacion.objects.get(id = observacion_id_old)
                        
                
                observacion = Observacion()
                observacion.id = request.POST.get('id')
                observacion.nombre = request.POST.get('nombre')
                observacion.apellido = request.POST.get('apellido')
                observacion.correo = request.POST.get('correo')
                observacion.telefono = request.POST.get('telefono')
                observacion.documento = request.POST.get('documento')
                observacion.f_nac = request.POST.get('f_nac')  
                observacion.f_registro =observacion_old.f_registro         
                observacion.save()            
                return redirect('listar_observacion')      
        else:
            observaciones = Observacion.objects.all()
            observacion = Observacion.objects.get(id=idObservacion)
            datos = { 'observaciones' : observaciones, 'observacion': observacion}
            return render(request, "crud_observacion/actualizar_observacion.html", datos)
        
    except Observacion.DoesNotExist:
        observaciones = Observacion.objects.all()
        observacion = None
        datos = { 'observaciones' : observaciones, 'observacion': observacion }
        return render(request, "crud_observacion/actualizar_observacion.html", datos)
    

def eliminar_observacion(request, idObservacion):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                tupla = Observacion.objects.get(id = id_a_borrar)
                tupla.delete()
                return redirect('listar_observacion')
        else:        
            observaciones = Observacion.objects.all()
            observacion = Observacion.objects.get(id = idObservacion)
            datos = { 'observaciones' : observaciones, 'observacion': observacion }
            return render(request, "crud_observacion/eliminar_observacion.html",datos)
        
    except Observacion.DoesNotExist:
        observaciones = Observacion.objects.all()
        observacion = None
        datos =  { 'observaciones' : observaciones, 'observacion' : observacion }
        return render(request, "crud_observacion/eliminar_observacion.html",datos) 
    

def listar_operador(request):
    if request.method == 'POST':
        palabra = request.POST.get('keyword')
        lista = Operador.objects.all()

        if palabra is not None:
            resultado_busqueda = lista.filter(
                Q(id__icontains=palabra) |
                Q(nombre__icontains=palabra) |
                Q(apellido__icontains=palabra) |
                Q(correo__icontains=palabra) |
                Q(telefono__icontains=palabra) |
                Q(documento__icontains=palabra)
            )
            datos = {'operador': resultado_busqueda}
            return render(request, "crud_operador/listar_operador.html", datos)
        else:
            datos = {'operador': lista}
            return render(request, "crud_operador/listar_operador.html", datos)
    else:
        operadores = Operador.objects.order_by('-id')[:10]
        datos = {'operador': operadores}
        return render(request, "crud_operador/listar_operador.html", datos)

def agregar_operador(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
            operador = Operador()
            operador.nombre = request.POST.get('nombre')
            operador.apellido = request.POST.get('apellido')
            operador.correo = request.POST.get('correo')
            operador.documento = request.POST.get('documento')
            operador.f_nac = request.POST.get('f_nac')           
            operador.save()            
            return redirect('listar_operador')
    else:
        return render(request, "crud_operador/agregar_operador.html")

def actualizar_operador(request, idOperador):
    try: 
        if request.method=='POST':
            if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
                operador_id_old = request.POST.get('id')
                operador_old = Operador()
                operador_old = Operador.objects.get(id = operador_id_old)
                        
                
                operador = Operador()
                operador.id = request.POST.get('id')
                operador.nombre = request.POST.get('nombre')
                operador.apellido = request.POST.get('apellido')
                operador.correo = request.POST.get('correo')
                operador.telefono = request.POST.get('telefono')
                operador.documento = request.POST.get('documento')
                operador.f_nac = request.POST.get('f_nac')  
                operador.f_registro =operador_old.f_registro         
                operador.save()            
                return redirect('listar_operador')      
        else:
            operadores = Operador.objects.all()
            operador = Operador.objects.get(id=idOperador)
            datos = { 'operadores' : operadores, 'operador': operador}
            return render(request, "crud_operador/actualizar_operador.html", datos)
        
    except Operador.DoesNotExist:
        operadores = Operador.objects.all()
        operador = None
        datos = { 'operadores' : operadores, 'operador': operador }
        return render(request, "crud_operador/actualizar_operador.html", datos)
    

def eliminar_operador(request, idOperador):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                tupla = Operador.objects.get(id = id_a_borrar)
                tupla.delete()
                return redirect('listar_operador')
        else:        
            operadores = Operador.objects.all()
            operador = Operador.objects.get(id = idOperador)
            datos = { 'operadores' : operadores, 'operador': operador }
            return render(request, "crud_operador/eliminar_operador.html",datos)
        
    except Operador.DoesNotExist:
        operadores = Operador.objects.all()
        operador = None
        datos =  { 'operadores' : operadores, 'operador' : operador }
        return render(request, "crud_operador/eliminar_operador.html",datos) 
    

def listar_paquete_movil(request):
    if request.method == 'POST':
        palabra = request.POST.get('keyword')
        lista = Paquete_Movil.objects.all()

        if palabra is not None:
            resultado_busqueda = lista.filter(
                Q(id__icontains=palabra) |
                Q(nombre__icontains=palabra) |
                Q(apellido__icontains=palabra) |
                Q(correo__icontains=palabra) |
                Q(telefono__icontains=palabra) |
                Q(documento__icontains=palabra)
            )
            datos = {'paquete_movil': resultado_busqueda}
            return render(request, "crud_paquete_movil/listar_paquete_movil.html", datos)
        else:
            datos = {'paquete_movil': lista}
            return render(request, "crud_paquete_movil/listar_paquete_movil.html", datos)
    else:
        operadores = Paquete_Movil.objects.order_by('-id')[:10]
        datos = {'paquete_movil': operadores}
        return render(request, "crud_paquete_movil/listar_paquete_movil.html", datos)

def agregar_paquete_movil(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
            paquete_movil = Paquete_Movil()
            paquete_movil.nombre = request.POST.get('nombre')
            paquete_movil.apellido = request.POST.get('apellido')
            paquete_movil.correo = request.POST.get('correo')
            paquete_movil.documento = request.POST.get('documento')
            paquete_movil.f_nac = request.POST.get('f_nac')           
            paquete_movil.save()            
            return redirect('listar_paquete_movil')
    else:
        return render(request, "crud_paquete_movil/agregar_paquete_movil.html")

def actualizar_paquete_movil(request, idPaquete_Movil):
    try: 
        if request.method=='POST':
            if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
                paquete_movil_id_old = request.POST.get('id')
                paquete_movil_old = Paquete_Movil()
                paquete_movil_old = Paquete_movil.objects.get(id = paquete_movil_id_old)
                        
                
                paquete_movil = Paquete_Movil()
                paquete_movil.id = request.POST.get('id')
                paquete_movil.nombre = request.POST.get('nombre')
                paquete_movil.apellido = request.POST.get('apellido')
                paquete_movil.correo = request.POST.get('correo')
                paquete_movil.telefono = request.POST.get('telefono')
                paquete_movil.documento = request.POST.get('documento')
                paquete_movil.f_nac = request.POST.get('f_nac')  
                paquete_movil.f_registro =paquete_movil_old.f_registro         
                paquete_movil.save()            
                return redirect('listar_paquete_movil')      
        else:
            paquete_moviles = Paquete_Movil.objects.all()
            paquete_movil = Paquete_Movil.objects.get(id=idPaquete_Movil)
            datos = { 'paquete_moviles' : paquete_moviles, 'paquete_movil': paquete_movil}
            return render(request, "crud_paquete_movil/actualizar_paquete_movil.html", datos)
        
    except Paquete_Movil.DoesNotExist:
        paquete_moviles = Paquete_Movil.objects.all()
        paquete_movil = None
        datos = { 'paquete_moviles' : paquete_moviles, 'paquete_movil': paquete_movil }
        return render(request, "crud_paquete_movil/actualizar_paquete_movil.html", datos)
    

def eliminar_paquete_movil(request, idPaquete_Movil):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                tupla = Paquete_Movil.objects.get(id = id_a_borrar)
                tupla.delete()
                return redirect('listar_paquete_movil')
        else:        
            paquete_moviles = Paquete_Movil.objects.all()
            paquete_movil = Paquete_Movil.objects.get(id = idPaquete_Movil)
            datos = { 'paquete_moviles' : paquete_moviles, 'paquete_movil': paquete_movil }
            return render(request, "crud_paquete_movil/eliminar_paquete_movil.html",datos)
        
    except Paquete_Movil.DoesNotExist:
        paquete_moviles = Paquete_Movil.objects.all()
        paquete_movil = None
        datos =  { 'paquete_moviles' : paquete_moviles, 'paquete_movil' : paquete_movil }
        return render(request, "crud_paquete_movil/eliminar_paquete_movil.html",datos) 
    

def listar_potencia(request):
    if request.method == 'POST':
        palabra = request.POST.get('keyword')
        lista = Potencia.objects.all()

        if palabra is not None:
            resultado_busqueda = lista.filter(
                Q(id__icontains=palabra) |
                Q(nombre__icontains=palabra) |
                Q(apellido__icontains=palabra) |
                Q(correo__icontains=palabra) |
                Q(telefono__icontains=palabra) |
                Q(documento__icontains=palabra)
            )
            datos = {'potencia': resultado_busqueda}
            return render(request, "crud_potencia/listar_potencia", datos)
        else:
            datos = {'potencia': lista}
            return render(request, "crud_potencia/listar_potencia.html", datos)
    else:
        potencias = Potencia.objects.order_by('-id')[:10]
        datos = {'potencia': potencias}
        return render(request, "crud_potencia/listar_potencia.html", datos)

def agregar_potencia(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
            potencia = Potencia()
            potencia.nombre = request.POST.get('nombre')
            potencia.apellido = request.POST.get('apellido')
            potencia.correo = request.POST.get('correo')
            potencia.documento = request.POST.get('documento')
            potencia.f_nac = request.POST.get('f_nac')           
            potencia.save()            
            return redirect('listar_potencia')
    else:
        return render(request, "crud_potencia/agregar_potencia.html")

def actualizar_potencia(request, idPotencia):
    try: 
        if request.method=='POST':
            if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
                potencia_id_old = request.POST.get('id')
                potencia_old = Potencia()
                potencia_old = Potencia.objects.get(id = potencia_id_old)
                        
                
                potencia = Potencia()
                potencia.id = request.POST.get('id')
                potencia.nombre = request.POST.get('nombre')
                potencia.apellido = request.POST.get('apellido')
                potencia.correo = request.POST.get('correo')
                potencia.telefono = request.POST.get('telefono')
                potencia.documento = request.POST.get('documento')
                potencia.f_nac = request.POST.get('f_nac')  
                potencia.f_registro =potencia_old.f_registro         
                potencia.save()            
                return redirect('listar_potencia')      
        else:
            potencias = Potencia.objects.all()
            potencia = Potencia.objects.get(id=idPotencia)
            datos = { 'potencias' : potencias, 'potencia': potencia}
            return render(request, "crud_potencia/actualizar_potencia.html", datos)
        
    except Potencia.DoesNotExist:
        potencias = Potencia.objects.all()
        potencia = None
        datos = { 'potencias' : potencias, 'potencia': potencia }
        return render(request, "crud_potencia/actualizar_potencia.html", datos)
    

def eliminar_potencia(request, idPotencia):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                tupla = Potencia.objects.get(id = id_a_borrar)
                tupla.delete()
                return redirect('listar_potencia')
        else:        
            potencias = Potencia.objects.all()
            potencia = Potencia.objects.get(id = idPotencia)
            datos = { 'potencias' : potencias, 'potencia': potencia }
            return render(request, "crud_potencia/eliminar_potencia.html",datos)
        
    except Potencia.DoesNotExist:
        potencias = Potencia.objects.all()
        potencia = None
        datos =  { 'potencias' : potencias, 'potencia' : potencia }
        return render(request, "crud_potencia/eliminar_potencia.html",datos) 
        

def listar_segmento(request):
    if request.method == 'POST':
        palabra = request.POST.get('keyword')
        lista = Segmento.objects.all()

        if palabra is not None:
            resultado_busqueda = lista.filter(
                Q(id__icontains=palabra) |
                Q(nombre__icontains=palabra) |
                Q(apellido__icontains=palabra) |
                Q(correo__icontains=palabra) |
                Q(telefono__icontains=palabra) |
                Q(documento__icontains=palabra)
            )
            datos = {'segmento': resultado_busqueda}
            return render(request, "crud_segmento/listar_segmento.html", datos)
        else:
            datos = {'segmento': lista}
            return render(request, "crud_segmento/listar_segmento.html", datos)
    else:
        segmentos = Segmento.objects.order_by('-id')[:10]
        datos = {'segmento': segmentos}
        return render(request, "crud_segmento/listar_segmento.html", datos)

def agregar_segmento(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
            segmento = Segmento()
            segmento.nombre = request.POST.get('nombre')
            segmento.apellido = request.POST.get('apellido')
            segmento.correo = request.POST.get('correo')
            segmento.documento = request.POST.get('documento')
            segmento.f_nac = request.POST.get('f_nac')           
            segmento.save()            
            return redirect('listar_segmento')
    else:
        return render(request, "crud_segmento/agregar_segmento.html")

def actualizar_segmento(request, idSegmento):
    try: 
        if request.method=='POST':
            if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
                segmento_id_old = request.POST.get('id')
                segmento_old = Segmento()
                segmento_old = Segmento.objects.get(id = segmento_id_old)
                        
                
                segmento = Segmento()
                segmento.id = request.POST.get('id')
                segmento.nombre = request.POST.get('nombre')
                segmento.apellido = request.POST.get('apellido')
                segmento.correo = request.POST.get('correo')
                segmento.telefono = request.POST.get('telefono')
                segmento.documento = request.POST.get('documento')
                segmento.f_nac = request.POST.get('f_nac')  
                segmento.f_registro =segmento_old.f_registro         
                segmento.save()            
                return redirect('listar_segmento')      
        else:
            segmentos = Segmento.objects.all()
            segmento = Segmento.objects.get(id=idSegmento)
            datos = { 'segmentos' : segmentos, 'segmento': segmento}
            return render(request, "crud_segmento/actualizar_segmento.html", datos)
        
    except Segmento.DoesNotExist:
        segmentos = Segmento.objects.all()
        segmento = None
        datos = { 'segmentos' : segmentos, 'segmento': segmento }
        return render(request, "crud_segmento/actualizar_segmento.html", datos)    

def eliminar_segmento(request, idSegmento):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                tupla = Segmento.objects.get(id = id_a_borrar)
                tupla.delete()
                return redirect('listar_Segmento')
        else:        
            segmentos = Segmento.objects.all()
            segmento = Segmento.objects.get(id = idSegmento)
            datos = { 'segmentos' : segmentos, 'segmento': segmento }
            return render(request, "crud_segmento/eliminar_segmento.html",datos)
        
    except Segmento.DoesNotExist:
        segmentos = Segmento.objects.all()
        segmento = None
        datos =  { 'segmentos' : segmentos, 'segmento' : segmento }
        return render(request, "crud_segmento/eliminar_segmento.html",datos) 

def listar_tarifa(request):
    if request.method == 'POST':
        palabra = request.POST.get('keyword')
        lista = Tarifa.objects.all()

        if palabra is not None:
            resultado_busqueda = lista.filter(
                Q(id__icontains=palabra) |
                Q(nombre__icontains=palabra) |
                Q(apellido__icontains=palabra) |
                Q(correo__icontains=palabra) |
                Q(telefono__icontains=palabra) |
                Q(documento__icontains=palabra)
            )
            datos = {'tarifa': resultado_busqueda}
            return render(request, "crud_tarifa/listar_tarifa.html", datos)
        else:
            datos = {'tarifa': lista}
            return render(request, "crud_tarifa/listar_tarifa.html", datos)
    else:
        tarifas = Tarifa.objects.order_by('-id')[:10]
        datos = {'tarifa': tarifas}
        return render(request, "crud_tarifa/listar_tarifa.html", datos)

def agregar_tarifa(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
            tarifa = Tarifa()
            tarifa.nombre = request.POST.get('nombre')
            tarifa.apellido = request.POST.get('apellido')
            tarifa.correo = request.POST.get('correo')
            tarifa.documento = request.POST.get('documento')
            tarifa.f_nac = request.POST.get('f_nac')           
            tarifa.save()            
            return redirect('listar_tarifa')
    else:
        return render(request, "crud_tarifa/agregar_tarifa.html")

def actualizar_tarifa(request, idTarifa):
    try: 
        if request.method=='POST':
            if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
                tarifa_id_old = request.POST.get('id')
                tarifa_old = Tarifa()
                tarifa_old = Tarifa.objects.get(id = tarifa_id_old)
                        
                
                tarifa = Tarifa()
                tarifa.id = request.POST.get('id')
                tarifa.nombre = request.POST.get('nombre')
                tarifa.apellido = request.POST.get('apellido')
                tarifa.correo = request.POST.get('correo')
                tarifa.telefono = request.POST.get('telefono')
                tarifa.documento = request.POST.get('documento')
                tarifa.f_nac = request.POST.get('f_nac')  
                tarifa.f_registro =tarifa_old.f_registro         
                tarifa.save()            
                return redirect('listar_tarifa')      
        else:
            tarifas = Tarifa.objects.all()
            tarifa = Tarifa.objects.get(id=idTarifa)
            datos = { 'tarifas' : tarifas, 'tarifa': tarifa}
            return render(request, "crud_tarifa/actualizar_tarifa.html", datos)
        
    except Tarifa.DoesNotExist:
        tarifas = Tarifa.objects.all()
        tarifa = None
        datos = { 'tarifas' : tarifas, 'tarifa': tarifa }
        return render(request, "crud_tarifa/actualizar_tarifa.html", datos)
   

def eliminar_tarifa(request, idTarifa):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                tupla = Tarifa.objects.get(id = id_a_borrar)
                tupla.delete()
                return redirect('listar_tarifa')
        else:        
            tarifas = Tarifa.objects.all()
            tarifa = Tarifa.objects.get(id = idTarifa)
            datos = { 'tarifas' : tarifas, 'tarifa': tarifa }
            return render(request, "crud_tarifa/eliminar_tarifa.html",datos)
        
    except Tarifa.DoesNotExist:
        tarifas = Tarifa.objects.all()
        tarifa = None
        datos =  { 'tarifas' : tarifas, 'tarifa' : tarifa }
        return render(request, "crud_tarifa/eliminar_tarifa.html",datos) 

    
    
def listar_tecnologia(request):
    if request.method == 'POST':
        palabra = request.POST.get('keyword')
        lista = Tecnologia.objects.all()

        if palabra is not None:
            resultado_busqueda = lista.filter(
                Q(id__icontains=palabra) |
                Q(nombre__icontains=palabra) |
                Q(apellido__icontains=palabra) |
                Q(correo__icontains=palabra) |
                Q(telefono__icontains=palabra) |
                Q(documento__icontains=palabra)
            )
            datos = {'tecnologia': resultado_busqueda}
            return render(request, "crud_tecnologia/listar_tecnologia.html", datos)
        else:
            datos = {'tecnologia': lista}
            return render(request, "crud_tecnologia/listar_tecnologia.html", datos)
    else:
        tecnologias = Tecnologia.objects.order_by('-id')[:10]
        datos = {'tecnologia': tecnologias}
        return render(request, "crud_tecnologia/listar_tecnologia.html", datos)

def agregar_tecnologia(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
            tecnologia = Tecnologia()
            tecnologia.nombre = request.POST.get('nombre')
            tecnologia.apellido = request.POST.get('apellido')
            tecnologia.correo = request.POST.get('correo')
            tecnologia.documento = request.POST.get('documento')
            tecnologia.f_nac = request.POST.get('f_nac')           
            tecnologia.save()            
            return redirect('listar_tecnologia')
    else:
        return render(request, "crud_tecnologia/agregar_tecnologia.html")

def actualizar_tecnologia(request, idTecnologia):
    try: 
        if request.method=='POST':
            if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('documento') and request.POST.get('f_nac'):
                tecnologia_id_old = request.POST.get('id')
                tecnologia_old = Tecnologia()
                tecnologia_old = Tecnologia.objects.get(id = tecnologia_id_old)
                        
                
                tecnologia = Tecnologia()
                tecnologia.id = request.POST.get('id')
                tecnologia.nombre = request.POST.get('nombre')
                tecnologia.apellido = request.POST.get('apellido')
                tecnologia.correo = request.POST.get('correo')
                tecnologia.telefono = request.POST.get('telefono')
                tecnologia.documento = request.POST.get('documento')
                tecnologia.f_nac = request.POST.get('f_nac')  
                tecnologia.f_registro =tecnologia_old.f_registro         
                tecnologia.save()            
                return redirect('listar_tecnologia')      
        else:
            tecnologias = Tecnologia.objects.all()
            tecnologia = Tecnologia.objects.get(id=idTarifa)
            datos = { 'tecnologias' : tecnologias, 'tecnologia': tecnologia}
            return render(request, "crud_tecnologia/actualizar_tecnologia.html", datos)
        
    except Tecnologia.DoesNotExist:
        tecnologias = Tecnologia.objects.all()
        tecnologia = None
        datos = { 'tecnologias' : tecnologias, 'tecnologia': tecnologia }
        return render(request, "crud_tecnologia/actualizar_tecnologia.html", datos)
    

def eliminar_tecnologia(request, idTecnologia):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                tupla = Tecnologia.objects.get(id = id_a_borrar)
                tupla.delete()
                return redirect('listar_Tecnologia')
        else:        
            tecnologias = Tecnologia.objects.all()
            tecnologia = Tecnologia.objects.get(id = idTecnologia)
            datos = { 'tecnologias' : tecnologias, 'tecnologia': tecnologia }
            return render(request, "crud_tecnologia/eliminar_tecnologia.html",datos)
        
    except Tecnologia.DoesNotExist:
        tecnologias = Tecnologia.objects.all()
        tecnologia = None
        datos =  { 'tecnologias' : tecnologias, 'tecnologia' : tecnologia }
        return render(request, "crud_tecnologia/eliminar_tecnologia.html",datos) 