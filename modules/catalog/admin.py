from django import forms
from django.contrib import admin

from django_mptt_admin.admin import DjangoMpttAdmin

from itcase_catalog.shortcuts import get_product_model, get_category_model
from itcase_catalog.admin import ProductAdmin as ProductAdminBase
from itcase_catalog.admin import CategoryAdmin as CategoryAdminBase

from .models.catalog import Brand, Parametr, ProductParametr
from .models.parametres import ProductImage, Price


Product = get_product_model()
Category = get_category_model()

admin.site.unregister(Category)
admin.site.unregister(Product)

admin.site.register(Brand)


class ProductParametrAdminInline(admin.TabularInline):

    model = ProductParametr
    extra = 0


@admin.register(Parametr)
class ParametrAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {'fields': ('name', 'query_name', 'is_affects_price',
                           'filter_by')}),
    )

    prepopulated_fields = {'query_name': ('name',)}

    list_display = ('name', 'query_name', 'filter_by', 'is_affects_price')
    list_editable = ['is_affects_price', 'filter_by']

    inlines = [ProductParametrAdminInline]


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
        if db_field.name == 'color':
            if request._obj_ is not None:
                field.queryset = request._obj_.parametres.filter(
                    parametr__name__exact='Цвет')
            else:
                field.queryset = field.queryset.none()
        return field


class PickingPriceInline(admin.TabularInline):

    model = Price
    extra = 0

    filter_horizontal = ['parametr']

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        field = super().formfield_for_manytomany(db_field, request, **kwargs)
        if db_field.name == 'parametr':
            if request._obj_ is not None:
                field.queryset = request._obj_.parametres.filter(
                    parametr__is_affects_price=True,
                )
            else:
                field.queryset = field.queryset.none()
        return field


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
                       'related_products', 'description', 'parametres',
                       'pdf_instructtion', 'pdf_components', 'scheme',
                       'product_actions')
        }),
        ('Характеристики', {
            'fields': ['options'],
            'classes': ('grp-collapse', 'grp-closed'),
        }),
    )
    filter_horizontal = ['related_products', 'parametres']

    form = ProductAdminForm

    inlines = [ProductImageInline, PickingPriceInline]

    readonly_fields = ('product_actions',)

    def get_form(self, request, obj=None, **kwargs):
        request._obj_ = obj
        return super().get_form(request, obj, **kwargs)

    def product_actions(self, obj):
        return ', '.join(action.name for action in obj.action_set.all())

    product_actions.short_description = "Действующие акции"
