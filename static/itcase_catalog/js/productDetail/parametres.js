'use strict'

// Event for unchecking radio input.
// Handle mousedown event on checked radio inputs for groups of product paramentrs.
// eg: "Фактура", "Цвет", "Покрытие" and etc.
$(document).on(
  'mousedown',
  '.catalog-item-detail__param-item:has(input[id^="product_parametr-"]:checked)',
  function (event) {
    const radioButton = this.querySelector('input')
    // Save indicator to accept change checked state of radio input in "change" event
    // and set "checked" attr to "false".
    radioButton.dataset._blockChange = true
    radioButton.checked = false
  }
)

$(document).on('change', 'input[id^="product_parametr-"]', function (event) {
  let blockChange
  try {
    // "blockChange" in dataset as string. Convert string to boolean.
    blockChange = JSON.parse(this.dataset._blockChange)
  } catch (e) {
    blockChange = false
  }

  // If input is "checked" and user click on it, we check indicator "blockChange"
  // and set "checked" attr to "false" for unchecking radio input.
  if (this.checked && blockChange) {
    this.checked = false
  }

  // Clean "blockChange" for next event handling.
  this.dataset._blockChange = false
})
