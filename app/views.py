from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import ListView,TemplateView,CreateView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
import pandas as pd
    
# class home(TemplateView):
#     template_name='app/home.html'

def home(request):
    # item=json.objects.all().values()
    # df=pd.DataFrame(item)
    # df1=df.title.tolist()
    # df=df["likelihood"].tolist()
    # mydic={
    #     'df':df,'df1':df1
    # }

    return render(request,'app/home.html')


class json_listview(ListView):
    model=json
    context_object_name='data'

class jsoncreate(CreateView):
    model=json
    fields="__all__"

class deatillist(DetailView):
    model=json
    context_object_name="data"

class jsonupdate(UpdateView):
    model=json
    fields="__all__"

class jsondelate(DeleteView):
    model=json
    context_object_name="data"
    success_url=reverse_lazy('json_listview')




    

