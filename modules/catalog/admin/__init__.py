from django.contrib import admin

import nested_admin
from django_mptt_admin.admin import DjangoMpttAdmin

from itcase_catalog.shortcuts import get_product_model, get_category_model
from itcase_catalog.admin import CategoryAdmin as CategoryAdminBase

from ..models.catalog import (Brand, Parametr, ProductParametr, Measurement,
                              SectionAtribute, OptionalProduct)
from ..models.parametres import (ProductImage, Price, PriceCombinations,
                                 SeparateParametrPicking)

from .forms import ProductAdminForm


Product = get_product_model()
Category = get_category_model()

admin.site.unregister(Category)
admin.site.unregister(Product)

admin.site.register(Brand)
admin.site.register(Measurement)
admin.site.register(ProductParametr)


@admin.register(PriceCombinations)
class PriceCombinationsAdmin(admin.ModelAdmin):

    filter_horizontal = ['data', ]

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        field = super().formfield_for_manytomany(db_field, request, **kwargs)
        if db_field.name == 'data':
            field.queryset = ProductParametr.objects.filter(
                parametr__in=Parametr.objects.filter(
                    is_affects_price=True))
        return field


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
        (None, {'fields': (('on_main_page', 'in_menu', 'other_template'),
                           'name', 'slug', 'parent', 'image',
                           'filter_parametres')}),
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

    filter_horizontal = ['filter_parametres']

    # DjangoMpttAdmin
    change_tree_template = 'itcase_pages/django_mptt_admin/change_list.html'
    tree_load_on_demand = None
    use_context_menu = True


class SectionAtributeInline(admin.TabularInline):

    model = SectionAtribute
    extra = 0

    sortable_field_name = 'sort'

    fieldsets = (
        (None, {'fields': (('section_name', 'sort', 'show'),
                           'section_content')}),
    )


class OptionalProductInline(admin.TabularInline):

    model = OptionalProduct
    extra = 0

    sortable_field_name = 'sort'

    fieldsets = (
        (None, {'fields': (('name', 'sort', 'show'), 'products')}),
    )

    filter_horizontal = ['products']


class ProductImageInline(admin.TabularInline):

    model = ProductImage
    extra = 0

    sortable_field_name = 'sort'

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super().formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == '':
            if Parametr.objects.filter(name__icontains='цвет').exists():
                field.queryset = Parametr.objects.get(
                    name__icontains='цвет').product_parametres.all()
            else:
                field.queryset = ProductParametr.objects.none()
        return field


class SeparateParametrPickingInline(nested_admin.NestedTabularInline):

    model = SeparateParametrPicking
    extra = 0


class PickingPriceInline(nested_admin.NestedTabularInline):

    model = Price
    extra = 1

    fieldsets = (
        (None, {'fields': ('product_article', 'price', 'old_price',
                           'amount', 'image')}),
    )

    inlines = [SeparateParametrPickingInline]


@admin.register(Product)
class ProductAdmin(nested_admin.NestedModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('name', 'measuring',
                       ('in_hit', 'border'),
                       ('in_recommended', 'in_action'), ('category', 'brand'),
                       'recommend_categories', 'parametres',
                       'product_actions')
        }),
        ('SEO-информация', {
            'fields': ('seo_title', 'seo_description', 'seo_keywords',
                       'seo_other'),
            'classes': ('grp-collapse', 'grp-closed')
        }),
    )
    filter_horizontal = ['recommend_categories', 'parametres']

    form = ProductAdminForm

    inlines = [OptionalProductInline, SectionAtributeInline,
               ProductImageInline, PickingPriceInline]

    list_display = ('name', 'category')

    prepopulated_fields = {}

    search_fields = ('name', 'prices__price', 'prices__article',
                     'category__name')

    readonly_fields = ('product_actions',)

    def get_form(self, request, obj=None, **kwargs):
        request._obj_ = obj
        return super().get_form(request, obj, **kwargs)

    def product_actions(self, obj):
        return ', '.join(action.name for action in obj.action_set.all())

    product_actions.short_description = "Действующие акции"
