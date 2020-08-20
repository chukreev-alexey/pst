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
    this.value = this.dataset.prevValue || 1
    return event
  }

  this.value = this.value !== '' ? intValue : ''
  this.dataset.prevValue = this.value
})

$(document).on('change', '.catalog-item-detail__count-input', function (event) {
  let intValue = parseInt(this.value)
  const min = parseInt(this.dataset.min || this.min || 1) || 1
  const max = parseInt(this.dataset.max || this.max) || null

  if (isNaN(this.value) || isNaN(intValue)) {
    this.value = this.dataset.prevValue || min
    return event
  }

  if (intValue < min) {
    intValue = min
  }
  if (max !== null && intValue > max) {
    intValue = max
  }

  this.value = intValue
  this.dataset.prevValue = this.value
})
