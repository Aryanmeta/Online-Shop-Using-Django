from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
# from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        # models = CustomUser
        model = get_user_model()
        fields = ('email', 'username', )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        # models = CustomUser
        model = get_user_model()
        fields = ('email', 'username',)
