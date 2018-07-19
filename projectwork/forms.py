from django import forms

class urlForm(forms.Form):
    url = forms.URLField(widget =forms.TextInput(
                    attrs ={
                    "class":"form-control mr-sm-2 ",
                    "placeholder":"Enter URL"
                }
                )
            )
    