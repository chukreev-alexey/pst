from django import forms

from ..models.parametres import SeparateParametrPicking


class SeparateParametrForm(forms.ModelForm):

    class Meta(object):
        model = SeparateParametrPicking
        fields = '__all__'
