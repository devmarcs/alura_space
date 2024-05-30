from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Loguin",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu login"
            }
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a sua senha"
            }
        )
    )