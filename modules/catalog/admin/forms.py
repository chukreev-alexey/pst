from django import forms

from itcase_catalog.shortcuts import get_product_model, get_category_model

from ..models.parametres import SeparateParametrPicking


Product = get_product_model()
Category = get_category_model()


class ProductAdminForm(forms.ModelForm):
    from mptt.forms import TreeNodeChoiceField

    category = TreeNodeChoiceField(queryset=Category.objects.all(),
                                   label=Category._meta.verbose_name)

    class Meta(object):
        model = Product
        fields = '__all__'


class SeparateParametrForm(forms.ModelForm):

    class Meta(object):
        model = SeparateParametrPicking
        fields = '__all__'
