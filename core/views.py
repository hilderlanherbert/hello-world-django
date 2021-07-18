from django.shortcuts import render, HttpResponse

# Create your views here.

def soma(request, valor1, valor2):
    soma = valor1 + valor2;
    return HttpResponse('<h1>A soma é {} </h1>'.format(soma))

def subtracao(request, valor1, valor2):
    subtracao = valor1 - valor2
    return HttpResponse('<h1>A sub é {}'.format(subtracao))

def mult(request, valor1, valor2):
    mult = valor1 * valor2
    return HttpResponse('<h1>A mult é {}'.format(mult))

def div(request, valor1, valor2):
    if(valor2 != 0):
        div = valor1 / valor2
        return HttpResponse('<h1>A div é {}'.format(div))
    else:
        return HttpResponse('<h1> Não é possível dividir por zero')