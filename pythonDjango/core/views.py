from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, num1, num2, algarismo):
    if algarismo == '+':
        soma = num1 + num2
        return HttpResponse('<h1>{} + {} = {}</h1>'.format(num1, num2, soma))
    if algarismo == '-':
        subtracao = num1 - num2
        return HttpResponse('<h1>{} - {} = {}</h1>'.format(num1, num2, subtracao))
    if algarismo == '*':
        multiplicacao = num1 * num2
        return HttpResponse('<h1>{} * {} = {}</h1>'.format(num1, num2, multiplicacao))
    if algarismo == 'divisao':
        divisao = num1 / num2
        return HttpResponse('<h1>{} / {} = {}</h1>'.format(num1, num2, divisao))
