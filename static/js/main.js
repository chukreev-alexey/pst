/* globals SearchClass UserCartClass, ItcaseFilterClass ItcaseFilter */

'use strict'

if (typeof SearchClass !== 'undefined') {
  global.ItcaseSearch = new SearchClass()
}

if (typeof UserCartClass !== 'undefined') {
  global.UserCart = new UserCartClass({
    headerCartButton: 'cart-button',
    headerCartButtonText: 'cart-button__text',
    headerCartButtonCount: 'cart-button__count',

    addToCartButton: '.catalog-item__button, .search-result-list__item-button',

    // baseAddToButtonClass: 'button_color_blue',
    // inOrderAddToButtonClass: 'button_border_orange',
    // inOrderAddToButtonText: 'В заказе',

    productAmountInput: 'cart-list__item-count-input',
    productAmountMinusButton: 'cart-list__item-count-button_action_minus',
    productAmountPlusButton: 'cart-list__item-count-button_action_plus',

    deleteFromCartButton: 'cart-list__item-action-link',

    orderPaymentItem: 'cart-order__payment-item',
    orderPaymentItemChecked: 'cart-order__payment-item_state_checked',
    orderAgreeCheckbox: 'cart-order__agree-checkbox',
    orderAgreeCheckboxChecked: 'cart-order__agree_state_checked',

    // productCountVariants: ['позиция', 'позиции', 'позиций'],
    // priceFractionDigits: 0,
    // emptyCartText: 'Ваш заказ',

    cartListContainer: 'cart-list',
    cartListProductRow: 'cart-list__item',
    cartListProductSum: 'cart-list__item-cost-second',
    cartListOrderSum: 'cart-list-sum__amount',
  })
}

// initialize ionRangeSlider for "price" fields in filter form.
const initializeRangeSliders = () => {
  const $priceMin = $('input[data-price-min]')
  const $priceMax = $('input[data-price-max]')

  if ($priceMin.length && $priceMax.length) {
    const valFrom = parseInt($priceMin.val(), 10) || 0
    const valTo = parseInt($priceMax.val(), 10) || 100000

    // Save first min price value in catalog object for replacement filter block
    if (!ItcaseFilter.rangeFirstMinVal || valFrom < ItcaseFilter.rangeFirstMinVal) {
      ItcaseFilter.rangeFirstMinVal = valFrom
    }

    // Save first max price value in catalog object for replacement filter block
    if (!ItcaseFilter.rangeFirstMaxVal || valTo > ItcaseFilter.rangeFirstMaxVal) {
      ItcaseFilter.rangeFirstMaxVal = valTo
    }

    // Create range slider from empty div (no "input" is important)
    $('*[data-range-slider]').ionRangeSlider({
      type: 'double',
      min: ItcaseFilter.rangeFirstMinVal,
      max: ItcaseFilter.rangeFirstMaxVal,
      hide_min_max: true,
      hide_from_to: false,
      from: valFrom,
      to: valTo,
      postfix: ' р',
      onStart: (data) => {
        $priceMin.val(data.from)
        $priceMax.val(data.to)
      },
      onChange: (data) => {
        $priceMin.val(data.from)
        $priceMax.val(data.to)
      },
      onFinish: (data) => {
        ItcaseFilter.sendCheckedFilters()
      },
    })
  }
}

if (typeof ItcaseFilterClass !== 'undefined') {
  global.ItcaseFilter = new ItcaseFilterClass({
    dropPagination: true,
    productListClass: 'catalog-list',
    sortBlockClass: 'catalog-sort',
    contentRequestCB: initializeRangeSliders,
  })
}

$(document).ready(() => {
  // Range sliders for catalog filters
  initializeRangeSliders()
})

if (module.hot) {
  module.hot.accept()
}
