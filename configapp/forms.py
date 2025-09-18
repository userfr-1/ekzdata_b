from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Ismingiz", "class": "form-control"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email manzilingiz", "class": "form-control"}),
            "message": forms.Textarea(attrs={"placeholder": "Xabarni yozing...", "rows": 4, "class": "form-control"}),
        }
