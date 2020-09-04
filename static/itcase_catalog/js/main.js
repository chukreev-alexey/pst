/* globals UserCartClass, ItcaseFilterClass, UserCart, ItcaseFilter */

'use strict'

require('./catalogGroups')
require('./catalogSort')
require('./catalogFilterPopup')
require('./itemGallery')
require('./popupMenu')
require('./productDetail/contentTabs')
require('./productDetail/parametres')
require('./productDetail/events')

// Create "Cart" instance for work with catalog and cart
if (typeof UserCartClass !== 'undefined') {
  global.UserCart = new UserCartClass({
    // Header button(cart link) with total price and count text
    headerCartButton: 'cart-button',
    headerCartButtonText: 'cart-button__text-sum', // 'cart-button__text'
    headerCartButtonCount: 'cart-button__text-count',
    emptyCartText: 'Заказ',
    changeCartText: (count, price, hint) => {
      const cartButton = document.querySelector(`.${UserCart.props.headerCartButton}`)
      const priceText = UserCart.getCartPriceText(price, 'р') // '₽'

      if (cartButton.innerHTML.includes(UserCart.props.emptyCartText)) {
        const cartButtonText = cartButton.querySelector('.cart-button__text')
        UserCart.replaceHeaderCartButtonEmptyText(cartButtonText || cartButton, count, priceText)
      }

      if (UserCart.cartCountBlock.length) {
        UserCart.cartCountBlock.text(count)
      }

      if (UserCart.cartTextBlock.length) {
        UserCart.cartTextBlock.text(priceText)
      }

      if (UserCart.orderSumTitleBlock.length) {
        UserCart.orderSumTitleBlock.text(priceText) // `${count} ${countText} на сумму`
      }

      // const countText = UserCart.getNumEnding(count, UserCart.props.productCountVariants)
      // if (!hint) {
      //   const priceText = UserCart.getCartPriceText(price)
      //   hint = `В заявке ${count} ${countText} на сумму ${priceText}`
      // }
      // if (UserCart.cartHintBlock.length) {
      //   UserCart.cartHintBlock.text(hint)
      // }
    },

    // Button for add item to cart
    addToCartButton: '.catalog-item__button, .search-result-list__item-button-add',
    // baseAddToButtonClass: 'button_color_blue',
    // inOrderAddToButtonClass: 'button_border_orange',
    // inOrderAddToButtonText: 'В заказе',

    // Input and "+/-" buttons on cart page for change item count.
    productAmountInput: 'cart-list__item-count-input',
    productAmountMinusButton: 'cart-list__item-count-button_action_minus',
    productAmountPlusButton: 'cart-list__item-count-button_action_plus',

    // Button for delete item from cart
    deleteFromCartButton: 'cart-list__item-action-link',

    // Items(divs) for "payment"(Способ оплаты) and "agree"(обработка ПД) fields
    orderPaymentItem: 'cart-order__payment-item',
    orderPaymentItemChecked: 'cart-order__payment-item_state_checked',
    orderAgreeCheckbox: 'cart-order__agree-checkbox',
    orderAgreeCheckboxChecked: 'cart-order__agree_state_checked',

    // Count of numbers after decimal point in prices
    priceFractionDigits: 2,
    // productCountVariants: ['позиция', 'позиции', 'позиций'],

    // Cart page container and items in product list
    cartListContainer: 'cart-list',
    cartListProductRow: 'cart-list__item',
    cartListProductSum: 'cart-list__item-cost-second',
    cartListOrderSum: 'cart-list-sum__amount',
  })

  UserCart.getCartPriceText = function (price, currency) {
    if (currency) {
      currency = currency.toUpperCase()
    } else {
      currency = this.getNumEnding(price, ['рубль', 'рубля', 'рублей'])
    }

    const numberPrice = parseFloat(price)

    const isInteger = isFinite(numberPrice) && Math.floor(numberPrice) === numberPrice

    const priceFractionDigits = isInteger ? 0 : this.props.priceFractionDigits

    const cleanPrice = numberPrice.toLocaleString('ru-RU', {
      minimumFractionDigits: priceFractionDigits,
      maximumFractionDigits: priceFractionDigits,
    })

    return `${cleanPrice} ${currency}`
  }

  UserCart.calculateOrderSum = function () {
    const { productAmountInput, cartListOrderSum } = this.props

    // Change sum for order
    const $orderSum = $(`.${cartListOrderSum}`)

    if (!$orderSum.length) {
      return null
    }

    let allSum = 0

    $(`.${productAmountInput}`).each((i, input) => {
      const cleanPrice = input.dataset.price.toString().replace(/\s/g, '')
      allSum += input.value * parseFloat(cleanPrice.replace(',', '.'))
    })

    const orderSumParts = $orderSum
      .text()
      .replace(/\r?\n|\r/g, '')
      .trim()
      .split(' ')
      .filter(Boolean)

    // prettier-ignore
    const orderCurrency = (orderSumParts.length > 1)
      ? orderSumParts[1] || ''
      : orderSumParts[0] || ''

    if (orderCurrency.toLowerCase() === 'р' || orderCurrency.toLowerCase().startsWith('руб')) {
      const isInteger = isFinite(allSum) && Math.floor(allSum) === allSum
      const priceFractionDigits = isInteger ? 0 : this.props.priceFractionDigits
      const priceFormat = {
        minimumFractionDigits: priceFractionDigits,
        maximumFractionDigits: priceFractionDigits,
      }
      allSum = allSum.toLocaleString('ru-RU', priceFormat)
    } else {
      allSum = allSum.toFixed(2)
    }

    $orderSum.text(`${allSum} ${orderCurrency}`)
  }
}

// initialize ionRangeSlider for "price" fields in filter form.
const initializeRangeSliders = () => {
  const $priceMin = $('input[data-price-min]')
  const $priceMax = $('input[data-price-max]')

  const filterData = ItcaseFilter.getCurrentFiltersFromUrl()
  if ('price-max' in filterData) {
    $priceMax.val(filterData['price-max'])
  }
  if ('price-min' in filterData) {
    $priceMin.val(filterData['price-min'])
  }

  if ($priceMin.length && $priceMax.length) {
    // prettier-ignore
    const valFrom = parseInt($priceMin.val(), 10) || 0

    // prettier-ignore
    const valTo = parseInt($priceMax.val(), 10) || 100000

    // Save first min price value in catalog object for replacement filter block
    if (!ItcaseFilter.rangeFirstMinVal || valFrom < ItcaseFilter.rangeFirstMinVal) {
      ItcaseFilter.rangeFirstMinVal = parseInt($priceMin.data('price-min'), 10) || valFrom
    }

    // Save first max price value in catalog object for replacement filter block
    if (!ItcaseFilter.rangeFirstMaxVal || valTo > ItcaseFilter.rangeFirstMaxVal) {
      ItcaseFilter.rangeFirstMaxVal = parseInt($priceMax.data('price-max'), 10) || valTo
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
    filterClearButtonClass: 'catalog-filter__clear',
    sortItemClass: ['catalog-sort__group-item', 'catalog-sort-dropdown__item'],
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
