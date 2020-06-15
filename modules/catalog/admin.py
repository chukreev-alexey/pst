from django import forms
from django.contrib import admin

from django_mptt_admin.admin import DjangoMpttAdmin

from itcase_catalog.shortcuts import get_product_model, get_category_model
from itcase_catalog.admin import ProductAdmin as ProductAdminBase
from itcase_catalog.admin import CategoryAdmin as CategoryAdminBase

from .models import Brand
from .models.parametres import Parametr, ProductParametr, ProductImage, Price


Product = get_product_model()
Category = get_category_model()

admin.site.unregister(Category)
admin.site.unregister(Product)

admin.site.register(Parametr)
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

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super().formfield_for_foreignkey(db_field, request, **kwargs)
        print(db_field.name)
        if db_field.name == 'color':

            if request._obj_ is not None:
                field.queryset = field.queryset.filter(
                    product__exact=request._obj_,
                    parametr__name__exact='Цвет')
            else:
                field.queryset = field.queryset.none()

        return field


class PickingPriceInline(admin.TabularInline):

    model = Price
    extra = 0

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        field = super().formfield_for_manytomany(db_field, request, **kwargs)
        print(db_field.name)
        if db_field.name == 'parametr':

            if request._obj_ is not None:
                field.queryset = field.queryset.filter(
                    product__exact=request._obj_)
            else:
                field.queryset = field.queryset.none()

        return field


class ProductParametrInline(admin.TabularInline):

    model = ProductParametr
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
                       'pdf_instructtion', 'pdf_components', 'scheme',
                       'product_actions')
        }),
        ('Характеристики', {
            'fields': ['options'],
            'classes': ('grp-collapse', 'grp-closed'),
        }),
    )
    filter_horizontal = ['related_products']

    form = ProductAdminForm

    inlines = [ProductParametrInline, ProductImageInline, PickingPriceInline]

    readonly_fields = ('product_actions',)

    def get_form(self, request, obj=None, **kwargs):
        request._obj_ = obj
        return super().get_form(request, obj, **kwargs)

    def product_actions(self, obj):
        return ', '.join(action.name for action in obj.action_set.all())

    product_actions.short_description = "Действующие акции"
