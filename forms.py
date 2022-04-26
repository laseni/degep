from django import forms


class SignupForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput())
    
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput())
    
class CreateGameForm(forms.Form):
    dialogueID = forms.CharField()
    

class DialogueCreateForm(forms.Form):
    name1 = forms.CharField()
    name2 = forms.CharField()          
    
class ChatForm(forms.Form):
    dialogue1 = forms.CharField() 
    dialogue2 = forms.CharField()
    reply1 = forms.CharField()
    reply2 = forms.CharField() 
    
class DialogueMoves(forms.Form):
    dialogueID = forms.CharField()

class MoveForm(forms.Form):
        dialogueID = forms.CharField()
        
class GameForm(forms.Form):
        dialogueID = forms.CharField()
        chat = forms.CharField()
                                                                                                                                                                                                       