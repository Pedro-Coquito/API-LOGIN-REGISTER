from django.shortcuts import render, redirect
from django.contrib import messages
import httpx
from .forms import LoginForm, RegisterForm
from django.conf import settings
from django.contrib.auth.decorators import login_required

API_URL = settings.FASTAPI_URL  # Ajuste o valor padrão conforme necessário

# View para exibir o formulário de cadastro e cadastrar a pessoa
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            resp = httpx.post(f"{API_URL}/Register", json={
                "username": data['username'],
                "password": data['password'],
                "e_mail": data['e_mail'],
                "phone_number": data['phone_number'],
                "name": data['name'],
                "last_name": data['last_name'],
            })
            if resp.status_code == 200:
                messages.success(request, "Registro bem-sucedido. Faça login.") 
                return redirect("meu_app:login")
            else:
                messages.error(request, f"Erro: {resp.json().get('message', resp.text)}")
    else:
        form = RegisterForm()
    return render(request, "meu_app/Register.html", {"form": form})

# View para exibir o formulário de login e autenticar
def login_view(request):
    print("Iniciando a view de login")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print("Enviando para backend:", data)
            resp = httpx.post(f"{API_URL}/login", json={
                "username": data["username"],
                "password": data["password"]
            })
            print("Resposta do backend:", resp.status_code, resp.text)
            if resp.status_code == 200:
                data = resp.json()
                result = data.get("result")
                token = result.get("acess_token") if result else None
                if token:
                    request.session["jwt_token"] = token
                    messages.success(request, "Login bem-sucedido.")
                    return redirect("meu_app:dashboard")
                else:
                    messages.error(request, data.get("message", "Usuário ou senha inválido"))
            else:
                messages.error(request, resp.json().get("message", "Usuário ou senha inválido"))
        else:
            messages.error(request, "Formulário inválido.")
        form = LoginForm()
    else:
        form = LoginForm()
    return render(request, "meu_app/login.html", {"form": form})

# View simples para a home

def home(request):
        return render(request, "meu_app/home.html")


def dashboard(request):
    token = request.session.get('jwt_token')
    if not token:
        messages.error(request, "Você precisa estar logado para acessar o dashboard.")
        return redirect("meu_app:dashboard")
    return render(request, "meu_app/dashboard.html")