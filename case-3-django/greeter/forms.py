from django import forms


class UserNameForm(forms.Form):
    name = forms.CharField(
        label="Ваше имя",
        max_length=100,
        required=True,
        error_messages={
            "required": "Пожалуйста, введите имя."
        }
    )