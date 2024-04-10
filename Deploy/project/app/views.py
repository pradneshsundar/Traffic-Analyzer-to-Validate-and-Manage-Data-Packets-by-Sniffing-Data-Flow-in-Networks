from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
#from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import sklearn
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory, models
from . forms import CreateUserForm
from django.contrib import messages
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import numpy as np
import joblib
from . import forms

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (12, 12)
mpl.rcParams['axes.grid'] = False
import time
from  joblib import load


model = joblib.load('C:/Users/pradn/Downloads/FINAL_PROJECT/proj.pkl')

Model = model


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def landingpage(request):
    return render(request, 'landingpage.html')

def about(request):
    return render(request, 'about.html')


def ishemic_cancer(request):
    return render(request, 'ishemic_Cancer.html')




def register(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'registration/register1.html', context)


def loginpage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'registration/login1.html', context)

def logoutusers(request):
    logout(request)
    return redirect('login')



  
def predict(request):

    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        int_features = int_features[1:]
        print(int_features)
        final_features = [np.array(int_features, dtype=float)]
        print(final_features)
        prediction = Model.predict(final_features)
        print(type(prediction))
        output = prediction[0]
        print(f'output{output}')
        if output == 0:
            return render(request, 'output.html', {"prediction_text":"Brute_Force"})
        elif output == 1:
            return render(request, 'output.html', {"prediction_text":"HTTP_DDoS"})
        elif output == 2:
            return render(request, 'output.html', {"prediction_text":"ICMP_Flood"})
        elif output == 3:
            return render(request, 'output.html', {"prediction_text":"Normal"})
        elif output == 4:
            return render(request, 'output.html', {"prediction_text":"Port_Scan"})
        elif output == 5:
            return render(request, 'output.html', {"prediction_text":"Web_Crwling"})

    return render(request, 'model3.html')




