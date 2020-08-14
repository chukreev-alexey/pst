'use strict'

$(document).on(
  'mousedown',
  '.catalog-item-detail__param-item:has(input[id^="product_parametr-"]:checked)',
  function (event) {
    const radioButton = this.querySelector('input')
    radioButton.dataset._blockChange = true
    radioButton.checked = false
  }
)

$(document).on('change', 'input[id^="product_parametr-"]', function (event) {
  let blockChange
  try {
    blockChange = JSON.parse(this.dataset._blockChange)
  } catch (e) {
    blockChange = false
  }

  if (this.checked && blockChange) {
    this.checked = false
  }

  this.dataset._blockChange = false
})
