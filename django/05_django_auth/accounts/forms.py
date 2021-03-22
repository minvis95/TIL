from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        # 현재 활성화된 user model
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)