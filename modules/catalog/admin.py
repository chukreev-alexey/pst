from django.contrib import admin
from django.utils.safestring import mark_safe

from django_mptt_admin.admin import DjangoMpttAdmin
import nested_admin

from itcase_catalog.admin import CategoryAdmin as CategoryAdminBase
from itcase_catalog.shortcuts import get_product_model, get_category_model

from .models import (Brand, CategorySectionAtribute, Measurement,
                     OptionalProduct, Parametr, Price, ProductImage,
                     ProductParametr, SectionAtribute, SeparateParametrPicking)

Product = get_product_model()
Category = get_category_model()

admin.site.unregister(Category)
admin.site.unregister(Product)

admin.site.register(Measurement)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):

    list_display = ('name', 'sort')
    list_editable = ['sort']
    search_fields = ['name']


class CategorySectionAtributeInline(admin.TabularInline):

    model = CategorySectionAtribute
    extra = 0

    sortable_field_name = 'sort'

    fieldsets = [(None, {'fields': (('name', 'sort', 'show'), 'content')})]


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin, CategoryAdminBase):

    fieldsets = (
        (None, {
            'fields': (('active', 'on_main_page',
                        'in_menu'), 'name', 'slug', 'parent', 'image',
                       'filter_brand', 'filter_parametres', 'rotator_units')
        }),
        ('Шаблоны', {
            'fields': ('template_categories_list',
                       'template_groups_type_selector'),
            'classes': ['grp-collapse'],
        }),
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

    inlines = [CategorySectionAtributeInline]

    prepopulated_fields = {'slug': ['name']}

    filter_horizontal = ['filter_parametres', 'rotator_units']

    # DjangoMpttAdmin
    change_tree_template = 'itcase_pages/django_mptt_admin/change_list.html'
    tree_load_on_demand = None
    use_context_menu = True


class ProductParametrAdminInline(admin.TabularInline):

    extra = 0
    model = ProductParametr


@admin.register(Parametr)
class ParametrAdmin(admin.ModelAdmin):

    fieldsets = ((None, {
        'fields': ('name', 'query_name', 'is_affects_price', 'filter_by')
    }), )

    prepopulated_fields = {'query_name': ('name', )}

    list_display = ('name', 'query_name', 'filter_by', 'is_affects_price')
    list_editable = ['is_affects_price', 'filter_by']

    inlines = [ProductParametrAdminInline]


class OptionalProductInline(admin.TabularInline):

    model = OptionalProduct
    extra = 0

    sortable_field_name = 'sort'

    fieldsets = ((None, {'fields': (('name', 'sort', 'show'), 'products')}), )

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


class SectionAtributeInline(admin.TabularInline):

    model = SectionAtribute
    extra = 0
    classes = ('grp_inline_tinymce', )

    sortable_field_name = 'sort'

    fieldsets = ((None, {
        'fields': (('section_name', 'sort', 'show'), 'section_content')
    }), )


class SeparateParametrPickingInline(nested_admin.NestedTabularInline):

    model = SeparateParametrPicking
    extra = 0

    sortable_field_name = 'sort'


class PickingPriceInline(nested_admin.NestedStackedInline):

    model = Price
    extra = 1

    fieldsets = ((None, {
        'fields': ('product_article', 'price', 'old_price', 'amount', 'image',
                   'image_description', 'show')
    }), )

    inlines = [SeparateParametrPickingInline]


@admin.register(Product)
class ProductAdmin(nested_admin.NestedModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'sort', 'measuring', ('in_hit',
                                                             'border'),
                       ('in_recommended', 'in_action'), 'brand', 'categories',
                       'recommend_categories', 'parametres', 'product_actions',
                       'short_description', 'content')
        }),
        ('SEO-информация', {
            'fields': ('seo_title', 'seo_description', 'seo_keywords',
                       'seo_other'),
            'classes': ('grp-collapse', 'grp-closed')
        }),
    )
    filter_horizontal = ('categories', 'recommend_categories', 'parametres')

    inlines = [
        OptionalProductInline, SectionAtributeInline, ProductImageInline,
        PickingPriceInline
    ]

    list_display = ('name', 'get_categories', 'sort')
    list_editable = ['sort']
    list_filter = ('border', 'brand', 'categories', 'in_action', 'in_hit',
                   'in_recommended')

    prepopulated_fields = {'slug': ['name']}

    search_fields = ('name', 'slug', 'prices__price',
                     'prices__product_article')

    readonly_fields = ['product_actions']

    def get_categories(self, obj):
        return mark_safe('<br>'.join(
            str(category) for category in obj.categories.iterator()))

    def get_form(self, request, obj=None, **kwargs):
        request._obj_ = obj
        return super().get_form(request, obj, **kwargs)

    def product_actions(self, obj):
        return ', '.join(action.name for action in obj.action_set.all())

    product_actions.short_description = 'Действующие акции'


@admin.register(ProductParametr)
class ProductParametrAdmin(admin.ModelAdmin):

    list_display = ('parametr', 'value')
    list_filter = ['parametr']
    search_fields = list_display
