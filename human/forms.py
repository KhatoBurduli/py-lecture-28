from django import forms


class HumanForm(forms.Form):
    name = forms.CharField(label="Human Name", max_length=100)
    lastname = forms.CharField(label="Human Lastname", max_length=100)
    age = forms.IntegerField(label="Human Age")
