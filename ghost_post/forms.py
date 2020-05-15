from django import forms


class NewPostForm(forms.Form):
    boast_or_roast = forms.ChoiceField(
        label='',
        choices=(('boast', 'Boast'), ('roast', 'Roast')),
        widget=forms.RadioSelect
    )
    content = forms.CharField(max_length=280, widget=forms.Textarea)
