from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def default_response(request):
    return HttpResponse('<h1>¡Hola!</h1><br><body>' +
                        'Introduce tu operación en la URL</body>')


def suma(request, op1, op2):
    result = int(op1) + int(op2)
    return HttpResponse(('<head><b>El resultado de tu suma es:</b><br>'
                         '</head><body>' + op1 + ' + ' + op2 + ' = ' +
                         str(result) + '</body>'))


def resta(request, op1, op2):
    result = int(op1) - int(op2)
    return HttpResponse(('<head><b>El resultado de tu resta es:</b><br>'
                         '</head><body>' + op1 + ' - ' + op2 + ' = ' +
                         str(result) + '</body>'))


def multiplicacion(request, op1, op2):
    result = int(op1) * int(op2)
    return HttpResponse(('<head><b>El resultado de tu multiplicacion es:'
                         '</b><br></head><body>' + op1 + ' * ' + op2 +
                         ' = ' + str(result) + '</body>'))


def division(request, op1, op2):
    result = int(op1) / int(op2)
    return HttpResponse(('<head><b>El resultado de tu division es:'
                         '</b><br></head><body>' + op1 + ' / ' + op2 +
                         ' = ' + str(result) + '</body>'))


def not_found(request):
    return HttpResponseNotFound('<h1>Recurso no encontrado. Revisa tu URL,'
                                ' por favor</h1>')
    # esto, además de devolver el texto HTML,
    # devuelve al navegador un código 404
