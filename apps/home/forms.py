from django import forms


class Gate1Form(forms.ModelForm):

    class Meta:
        widgets = {
            'age': forms.TextInput(attrs={'size': 3}),
        }
