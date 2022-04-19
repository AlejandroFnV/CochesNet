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

    # print(typeModel)

    lis = []

    lis.append(request.GET['km'])
    lis.append(request.GET['year'])
    lis.append(request.GET['cubicCapacity'])
    lis.append(request.GET['doors'])
    lis.append(request.GET['hp'])

    ans = model.predict([lis])

    external_doc = loader.get_template('result.html')
    documento = external_doc.render(
        {'ans': ("%.2f" % ans).rstrip('0').rstrip('.')})
    return HttpResponse(documento)


def getPredictions(km, year, cubicCapacity, doors, hp):
    model = pickle.load(open("Proyecto1/finalized_model.sav", "rb"))
    prediction = model.predict(sc.transform(
        [[km, year, cubicCapacity, doors, hp]]))
    # return prediction
    prediction = 1
    if prediction == 0:
        return "not survived"
    elif prediction == 1:
        return "survived"
    else:
        return "error"
