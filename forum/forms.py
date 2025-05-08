from django import forms
from .models import Message
from django.core.exceptions import ValidationError

class MessageForm(forms.ModelForm):

    def clean_image(self):
        picture = self.cleaned_data.get('image')
        if picture:
            if picture.size > 2 * 1024 * 1024:
                raise ValidationError("Изображение слишком большое (макс. 2MB)")
        return picture

    class Meta:
        model = Message
        fields = ['text', 'picture']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите ваше сообщение...',
                'rows': 3
            })
        }

