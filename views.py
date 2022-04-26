from django.shortcuts import render,redirect
import requests
import json
from django.http import HttpResponse
from .forms import SignupForm
from .forms import LoginForm
from .forms import CreateGameForm
from .forms import DialogueCreateForm
from .forms import ChatForm
from .forms import DialogueMoves
from .forms import MoveForm

def index(request):
    return render(request, 'index.html')


def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            url = "http://localhost:8888/dgep/v1/auth/login"
 
            headers = {
                "Content-Type": "application/json",
                "accept": "application/json"
                }
            
            data = {
                "username": username,
                "password": password,
            }
            
            response = requests.post(url, headers=headers, json=data)
            request.session['token'] = response.text
            if response.status_code==200:         
                return redirect(playgame)
            
    
def login(request):
    context ={}
    context['form']= LoginForm()
    return render(request, "login.html", context)

                    
def signup(request):            
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            url = "http://localhost:8888/dgep/v1/auth/register"
 
            headers = {
                "Content-Type": "application/json",
                "accept": "application/json"
                }
            
            data = {
                "username": username,
                "password": password,
            }
            response = requests.post(url, headers=headers, json=data)
            if response.status_code==200:
                return redirect(login)
            else:
                return render(request, "signup.html", {'message':'Bad request'})
    
    context ={}
    context['form']= SignupForm()
    return render(request, "signup.html", context)

#get list of moves
def chat(request):
        if request.method == 'POST':
            form = DialogueMoves(request.POST)
            if form.is_valid():
                dialogueID = form.cleaned_data['dialogueID']
                
                url = "http://localhost:8888/dgep/v1/dialogue/"+dialogueID+"/moves"
            
                headers = {
                            "accept": "application/json",
                            "X-AUTH-TOKEN":  request.session.get('token')
                            }
                    
                response = requests.get(url, headers=headers,)
                if response.status_code == 200:
                    data = response.text
                    request.session['dialogueID']=dialogueID
                    return render(request, "chat.html", {"message":data})
                        
                    
        context ={}
        context['form']=  DialogueMoves()
        return render(request, "chat.html", context)

def status(request):
    if request.method == 'POST':
            form = CreateGameForm(request.POST)
            if form.is_valid():
                    dialogueId = form.cleaned_data['dialogueID']
                    url = "http://localhost:8888/dgep/v1/dialogue/"+dialogueId+"/status"
        
                    headers = {
                            "accept": "application/json",
                            "X-AUTH-TOKEN":  request.session.get('token')
                            }
                   
                    response = requests.get(url, headers=headers)
                    if response.status_code == 200:
                        data = response.text
                        return HttpResponse(data)
                    
    context ={}
    context['form']=  CreateGameForm()
    return render(request, "chat.html", context)
                    

def move(request):
    if request.method == 'POST':
            form = CreateGameForm(request.POST)
            if form.is_valid():
                    dialogueId = form.cleaned_data['dialogueID']
                    url = "http://localhost:8888/dgep/v1/dialogue/"+dialogueId+"/moves"
        
                    headers = {
                            "accept": "application/json",
                            "X-AUTH-TOKEN":  request.session.get('token')
                            }
                   
                    response = requests.get(url, headers=headers)
                    if response.status_code == 200:
                        data = response.text
                        return HttpResponse(data)   
    context ={}
    context['form']=  CreateGameForm()
    return render(request, "chat.html", context) 


def sayHello(request):
    print(request.POST)
    return render(request, 'hello.html')

def playgame(request):
         
    url = "http://localhost:8888/dgep/v1/protocol/list"
    
    headers = {
        "accept": "application/json"
        }
    
    response = requests.get(url, headers=headers)
    
    protocol = response.text
    return render(request, 'protocol.html', {'protocol':protocol})



def dialogue(request):
    if request.method == 'POST':
        form = DialogueCreateForm(request.POST)
        if form.is_valid():
            name1 = form.cleaned_data['name1']
            name2 = form.cleaned_data['name2']
            
            url = "http://localhost:8888/dgep/v1/dialogue/new/SimplePersuasion"
            
            headers = {
                    "Content-Type": "application/json",
                    "accept": "application/json",
                    "X-AUTH-TOKEN": request.session.get('token')
                    }
            
            data = {
                    "participants": [
                        {
                            "name": name1,
                            "player": "Person1",
                        },
                        {
                            "name": name2,
                            "player": "Person2",
                        }
                    ]
                }
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                    request.session['dialogue'] = response.text
                    return render(request, "reg_dialogue.html", {'message':request.session.get('dialogue')})
            else:
                    return render(request, "reg_dialogue.html", {'message':'Bad request'})
                        
    context ={}
    context['form']= DialogueCreateForm()
    return render(request, "reg_dialogue.html", context)

def dgdl(request):
    url ="http://localhost:8888/dgep/v1/protocol/SimplePersuasion"
    headers={
       "accept": "application/json" 
    }
    response = requests.get(url, headers=headers)
    dgdl_spec = response.text
    return render (request, "game.html", {"dgdl_spec": dgdl_spec})
# Create your views here.
