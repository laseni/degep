from django.shortcuts import render,redirect
import requests
import json
from django.http import HttpResponse
from .forms import SignupForm
from .forms import LoginForm
from .forms import CreateGameForm
from .forms import DialogueCreateForm
from .forms import ChatForm

def index(request):
    return render(request, 'index.html')


def login(request):
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
            if response.status_code==200:         
                return redirect(playgame)
            
    context ={}
    context['form']= LoginForm()
    return render(request, "login.html", context)

# def reg(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
            
#             url = "http://localhost:8888/dgep/v1/auth/register"
 
#             headers = {
#                 "Content-Type": "application/json",
#                 "accept": "application/json"
#                 }
            
#             data = {
#                 "username": username,
#                 "password": password,
#             }
#             response = requests.post(url, headers=headers, json=data)
#             if response.status_code==200:
#                 return redirect(login)
#             else:
#                 return render(request, "signup.html", {'message':'Bad request'})
                    
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
    if request.method == 'GET':
                    
                    url = "http://localhost:8888/dgep/v1/dialogue/deb3e517-3615-47dc-95c7-d4746837a2a3/moves"
        
                    headers = {
                        "Content-Type": "application/json",
                        "accept": "application/json",
                        "X-AUTH-TOKEN": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InNvbmcifQ.WPM60pl1lpOubYVJXashr6BMiRG3PiOD4UnCzdBscmQ"
                        }
                    
                    data = {
                            "Gen": [
                                {
                                "moveID": "Assert",
                                "opener": "\"I assert \""+dialogue,
                                "reply": {
                                    "p": "This is so true"
                                },
                                "target": "Gan"
                                }
                            ]
                            }
                    response = requests.get(url, headers=headers, json=data)
                    if response.status_code == 200:
                        data = response.text
                        return  HttpResponse(response)
                        
                    
    context ={}
    context['form']= ChatForm()
    return render(request, "chat.html", context)

def chat1(request):
    if request.method == 'GET':
                    dialogue = "that you are strong"
                    
                    url = "http://localhost:8888/dgep/v1/dialogue/deb3e517-3615-47dc-95c7-d4746837a2a3/moves"
        
                    headers = {
                        "Content-Type": "application/json",
                        "accept": "application/json",
                        "X-AUTH-TOKEN": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InNvbmcifQ.WPM60pl1lpOubYVJXashr6BMiRG3PiOD4UnCzdBscmQ"
                        }
                    
                    data = {
                            "Gen": [
                                {
                                "moveID": "Assert",
                                "opener": "\"I assert \""+dialogue,
                                "reply": {
                                    "p": "This is so true"
                                },
                                "target": "Gan"
                                }
                            ]
                            }
                    response = requests.get(url, headers=headers, json=data)
                    if response.status_code == 200:
                        data = response.text
                        return HttpResponse(response)
                    else:
                        return render(request, "chat.html", {'message':'Bad request'})
                    
    context ={}
    context['form']= ChatForm()
    return render(request, "chat.html", context)

def chat2(request):
    if request.method == 'GET':
                    dialogue = "that you are strong"
                    
                    url = "http://localhost:8888/dgep/v1/dialogue/0f087900-6cb9-48b5-a07a-f5fedeb8be92/status"
        
                    headers = {
                        "accept": "application/json",
                        "X-AUTH-TOKEN": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InNvbmcifQ.WPM60pl1lpOubYVJXashr6BMiRG3PiOD4UnCzdBscmQ"
                        }
                    
                    data = {
                            "dialogueID": "0f087900-6cb9-48b5-a07a-f5fedeb8be92"
                            }
                    response = requests.get(url, headers=headers, json=data)
                    if response.status_code == 200:
                        data = response.text
                        return HttpResponse(response)
                    else:
                        return render(request, "chat.html", {'message':'Bad request'})
                    
    context ={}
    context['form']= ChatForm()
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
            print(request.session.get('token'))
            if 'token'in  request.session:
                request.session.session_key
                token = request.session['token']
                headers = {
                    "Content-Type": "application/json",
                    "accept": "application/json",
                    "X-AUTH-TOKEN": token
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
                    return redirect(chat)
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
