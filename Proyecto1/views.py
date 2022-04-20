from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.shortcuts import render
from django.template import Template, Context
from django.template import loader
from .forms import NameForm
import pickle
import joblib


def home(request):
    external_doc = loader.get_template('index.html')
    documento = external_doc.render()
    return HttpResponse(documento)


# our result page view
def result(request):
    typeModel = request.GET['model']
    model = joblib.load(typeModel)
    print(typeModel)


    lis = []

    lis.append(request.GET['km'])
    lis.append(request.GET['year'])
    lis.append(request.GET['cubicCapacity'])
    lis.append(request.GET['doors'])
    lis.append(request.GET['hp'])

    ans = model.predict([lis])

    print(ans)

    external_doc = loader.get_template('result.html')
    documento = external_doc.render(
        {'ans': ("%.2f" % ans).rstrip('0').rstrip('.')})
    return HttpResponse(documento)
