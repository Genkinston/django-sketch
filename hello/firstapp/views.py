from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template.response import TemplateResponse


# Create your views here.


def index(request):
    # return render(request, "firstapp/home.html")
    #return TemplateResponse(request, "firstapp/home.html")
    data = {"header": "Передача данных в шаблон Django",
            "message":
            "Загружен шаблон templates/firstapp/index_app1.html"
            }
    return render(request, "firstapp/index_app1.html",
                  context=data)


def about(request):
    return HttpResponse("About")


def contact(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")


def products(request, productid):
    category = request.GET.get("cat", "")
    output = ("<h2>Продукт № {0} Категория: {1}</h2>"
              .format(productid, category))
    return HttpResponse(output)


def users(request, id=1, name="Максим"):
    id = request.GET.get("id", 1)
    output = ("<h2>Пользователь</h2><h3>id: {0} "
              "Имя:{1}</h3>".format(id, name))
    return HttpResponse(output)
