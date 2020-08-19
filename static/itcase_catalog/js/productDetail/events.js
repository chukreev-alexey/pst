/* globals UserCart */

'use strict'

$(document).on('click', '.catalog-item-detail__count-button_action_plus', function (event) {
  UserCart.onAmountButtonClick(event, 1)
})

$(document).on('click', '.catalog-item-detail__count-button_action_minus', function (event) {
  UserCart.onAmountButtonClick(event, -1)
})

$(document).on('input', '.catalog-item-detail__count-input', function (event) {
  const intValue = parseInt(this.value)

  if (this.value !== '' && (isNaN(this.value) || isNaN(intValue))) {
    this.value = this.dataset.prevValue || 0
    return event
  }

  this.value = this.value !== '' ? intValue : ''
  this.dataset.prevValue = this.value
})

$(document).on('change', '.catalog-item-detail__count-input', function (event) {
  const intValue = parseInt(this.value)

  if (isNaN(this.value) || isNaN(intValue) || intValue < 0) {
    this.value = this.dataset.prevValue || 0
    return event
  }

  this.value = this.value !== '' ? intValue : ''
  this.dataset.prevValue = this.value
})
