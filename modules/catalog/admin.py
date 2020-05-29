from django import forms
from django.contrib import admin

from django_mptt_admin.admin import DjangoMpttAdmin

from itcase_catalog.shortcuts import get_product_model, get_category_model
from itcase_catalog.admin import ProductAdmin as ProductAdminBase
from itcase_catalog.admin import CategoryAdmin as CategoryAdminBase

from .models import ProductColors, ProductImage, Brand, PickingPrice

Product = get_product_model()
Category = get_category_model()

admin.site.unregister(Category)
admin.site.unregister(Product)

admin.site.register(ProductColors)
admin.site.register(Brand)


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin, CategoryAdminBase):

    fieldsets = (
        (None, {'fields': ('name', 'slug', 'parent', 'image')}),
        ('Контент', {
            'fields': ['content'],
            'classes': ('grp-collapse', 'grp-open'),
        }),
        ('SEO-информация', {
            'fields': ('seo_title', 'seo_description', 'seo_keywords',
                       'seo_other'),
            'classes': ('grp-collapse', 'grp-closed')
        }),
    )

    inlines = []

    prepopulated_fields = {'slug': ('name',)}

    # DjangoMpttAdmin
    change_tree_template = 'itcase_pages/django_mptt_admin/change_list.html'
    tree_load_on_demand = None
    use_context_menu = True


class ProductImageInline(admin.TabularInline):

    model = ProductImage
    extra = 0

    sortable_field_name = 'sort'


class PickingPriceInline(admin.TabularInline):

    model = PickingPrice
    extra = 0


class ProductAdminForm(forms.ModelForm):
    from mptt.forms import TreeNodeChoiceField

    category = TreeNodeChoiceField(queryset=Category.objects.all(),
                                   label=Category._meta.verbose_name)

    class Meta(object):
        model = Product
        fields = '__all__'


@admin.register(Product)
class ProductAdmin(ProductAdminBase):

    fieldsets = (
        (None, {
            'fields': ('name', 'price', 'article', ('category', 'brand'),
                       'related_products', 'description',
                       'pdf_instructtion', 'pdf_components', 'scheme')
        }),
        ('Характеристики', {
            'fields': ['options'],
            'classes': ('grp-collapse', 'grp-closed'),
        }),
    )
    filter_horizontal = ['related_products']

    form = ProductAdminForm

    inlines = [ProductImageInline, PickingPriceInline]
