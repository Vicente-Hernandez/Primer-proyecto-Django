from django.shortcuts import render , HttpResponse, redirect
from django.http.response import JsonResponse
from time import gmtime, strftime, localtime
from django.utils.crypto import get_random_string

# Create your views here.

def root(request):
    return redirect('/mi_app') 

def index(request):
    return HttpResponse('placeholder para luego mostrar una lista de todos los blogs')

def new(request):
    return HttpResponse('placeholder para mostrar un nuevo formulario para crear un nuevo blog')

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f'placeholder para mostrar el blog numero: {number}')

def edit(request,number):
    return HttpResponse(f'placeholder para editar el blog {number}')

def destroy(request, number):
    return redirect ('/mi_app')

def json(request):
    return JsonResponse({
        'nombre':'Andres',
        'ciudad':'Santiago de Chile',
        'estado civil':'casado',
        'hijos':2
    })

def home(request):
    context = {
    'imagenes' : ['https://www.autopistarock.com/images/easyblog_articles/4081/b2ap3_large_SA.jpg',
                'https://www.autopistarock.com/images/easyblog_articles/4081/b2ap3_large_S12.jpg',
                'https://www.autopistarock.com/images/easyblog_articles/4081/b2ap3_large_S30.jpg',
                'https://www.autopistarock.com/images/easyblog_articles/4081/b2ap3_large_S31.jpg',
                'https://www.autopistarock.com/images/easyblog_articles/4081/b2ap3_large_S19.jpg',
                'https://www.autopistarock.com/images/easyblog_articles/4081/b2ap3_large_S20.jpg',
    ]   
    }
    return render(request, 'index.html', context)

def time(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M:%S %p", localtime())
    }
    return render(request,'time.html', context)


USUARIOS = [
    {'nombre': 'Marcela', 'password': '12345'},
    {'nombre': 'Monty', 'password': '67890'},
    {'nombre': 'Matias', 'password': '54321'},
    {'nombre': 'Andres', 'password': '09876'},
]


def user(request, name):
    request.session['name'] = name
    return redirect('/random_word')


def random_word(request):
    counter = request.session.get('counter')
    if 'counter' not in request.session:
        request.session['counter'] = 0
        
    request.session['counter'] +=1
    context = {'random_word':get_random_string(length=14),
        'counter': counter
    }
    
    if counter >= 10:
        context = {'random_word': "Sobrepasaste los 10 intentos"}
    return render(request, 'words.html', context)

def reset(request):
    request.session['counter'] = 1
    return redirect('/random_word')   

def login(request):
    #si llega un GET, cargamos formulario
    if request.method == 'GET':
        return render(request, 'login.html')
    
    # else:
        # print ('Nombre: ', request.POST['nombre'])
        # print ('Password: ', request.POST['password'])
        
        # request.session['name'] = request.POST['nombre']
        
        # return redirect('/time_display')
    
    
        # return HttpResponse('Logueando al usuario')
        
    user = next((u for u in USUARIOS if u['nombre'] == request.POST['nombre']), None)
    
    if user is None:
        return redirect('/login')
    
    if user['password'] != request.POST['password']:
        return redirect('/login')
    
    request.session['name'] = request.POST['nombre']
    request.session['password'] = request.POST['password']
    
    return redirect('/time_display')
