from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ClienteForm, LocalidadForm
from .models import Persona, Localidad

# Create your views here.
def index(request, template_name="entidad/index.html"):
    dato = {
        "nombre": "Rodolfo",
        "edad": 30,
        "direccion": {
            "calle": "Av. San Martín 1350",
            "localidad": "C.A.B.A",
        },
        "cant_hijos": 3,
        "hijos": ["Ana", "Juan", "Mateo"]
    }
    return render(request, template_name, dato)


def acerca_de(request):
    return HttpResponse('Curso de Django')


def clientes(request, template_name='entidad/clientes.html'):
    clientes_list = Persona.objects.all()
    dato = {"clientes": clientes_list}
    return render(request, template_name, dato)


def localidades(request, template_name='entidad/localidades.html'):
    localidades_list = Localidad.objects.all()
    dato = {"localidades": localidades_list}
    return render(request, template_name, dato)


def nuevo_cliente(request, template_name='entidad/cliente_form.html'):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return redirect('clientes')
        
    else:
        form = ClienteForm()
    dato = {"form": form}
    return render(request, template_name, dato)


def nueva_localidad(request, template_name='entidad/localidad_form.html'):
    if request.method == 'POST':
        form = LocalidadForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return redirect('localidades')
        
    else:
        form = LocalidadForm()
    dato = {"form": form}
    return render(request, template_name, dato)


def modificar_cliente(request, pk, template_name='entidad/cliente_form.html'):
    cliente = Persona.objects.get(id=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            return redirect('clientes')
    dato = {'form': form}
    return render(request, template_name, dato)


def eliminar_cliente(request, pk, template_name='entidad/cliente_confirmar_eliminacion.html'):
    cliente = Persona.objects.get(id=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')
    dato = {'form':cliente}
    return render(request, template_name, dato)


def modificar_localidad(request, pk, template_name='entidad/localidad_form.html'):
    cliente = Localidad.objects.get(id=pk)
    form = LocalidadForm(request.POST or None, instance=localidad)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            return redirect('localidades')
    dato = {'form': form}
    return render(request, template_name, dato)


def eliminar_localidad(request, pk, template_name='entidad/localidad_confirmar_eliminacion.html'):
    localidad = Localidad.objects.get(id=pk)
    if request.method == 'POST':
        localidad.delete()
        return redirect('localidades')
    dato = {'form': localidad}
    return render(request, template_name, dato)


# def clientes(request, template_name="entidad/clientes.html"):
#     conn = sqlite3.connect("contabilidad.sqlite")
#     cliente = conn.cursor()
#     cliente.execute("SELECT nombre, edad FROM personas")
#     cliente_list = cliente.fetchall()
#     conn.close()
#     dato = {
#         "clientes": cliente_list,
#     }
#     return render(request, template_name, dato)


# def cliente(request, nombre_cliente, template_name="entidad/cliente.html"):
#     conn = sqlite3.connect("contabilidad.sqlite")
#     cursor = conn.cursor()
#     cursor.execute("SELECT nombre, edad FROM personas WHERE nombre = ?", [nombre_cliente])
#     cliente_seleccionado = cursor.fetchone()
#     conn.close()
#     dato = {"cliente": cliente_seleccionado}
#     return render(request, template_name, dato)


# def nuevo_cliente(request, template_name="entidad/cliente_form.html"):
#     if request.method == 'POST':
#         form = ClienteForm(request.POST)
        
#         if form.is_valid():
#             conn = sqlite3.connect('contabilidad.sqlite')
#             cursor = conn.cursor()
#             cursor.execute('INSERT INTO personas VALUES (?, ?)',
#                            (form.cleaned_data["nombre"], form.cleaned_data["edad"]))
#             conn.commit()
#             conn.close()
#             return redirect('clientes')
#     else:
#         form = ClienteForm()
#     dato = {"form": form}
#     return render(request, template_name, dato)