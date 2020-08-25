'use strict'

// Event for unchecking radio input.
// Handle mousedown event on checked radio inputs for groups of product paramentrs.
// eg: "Фактура", "Цвет", "Покрытие" and etc.
$(document).on(
  'mousedown',
  '.catalog-item-detail__param-item:has(input[id^="param-"]:checked)',
  function (event) {
    const radioButton = this.querySelector('input')
    // Save indicator to accept change checked state of radio input in "change" event
    // and set "checked" attr to "false".
    radioButton.dataset._blockChange = true
    radioButton.checked = false
  }
)

$(document).on('change', 'input[id^="param-"]', function (event) {
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

  // Disable unrelated params-inputs and enable related. Current input maybe unchecked.
  activateRelatedParams(this)

  // Disable unrelated params-inputs and enable related for another checked radio.
  // TODO: do it on unchecking current input? (or always?)
  const anotherCheckedInputs = document.querySelectorAll(
    `input[id^="param-"]:checked:not(#${this.id})`
  )
  for (let input of anotherCheckedInputs) {
    activateRelatedParams(input)
  }
})

function activateRelatedParams(targetInput) {
  /*
  "ID комплектации": {
    "scope": [ "ID связанного товара", "ID связанного товара", ... ],
    "price": "цена комплектации"
  }
  */

  let prices = {}
  try {
    prices = JSON.parse(targetInput.dataset.prices)
  } catch (err) {
    console.error('Parsing prices for product parameters error: ', err)
    return null
  }

  const relatedParams = new Set()
  Object.entries(prices).forEach(([priceID, valuesObj]) => {
    valuesObj.scope.forEach((paramID) => {
      const _paramID = paramID.toString()
      if (_paramID !== targetInput.value.toString()) {
        relatedParams.add(_paramID)
      }
    })
  })

  const paramsInputs = document.querySelectorAll('input[id^="param-"]')

  for (let input of paramsInputs) {
    if (input.name === targetInput.name) {
      continue
    }

    // prettier-ignore
    input.disabled = (targetInput.checked)
      ? !relatedParams.has(input.value.toString())
      : false

    if (input.disabled) {
      input.checked = false
    }

    const paramItem = input.closest('.catalog-item-detail__param-item')
    if (paramItem) {
      paramItem.classList.toggle('catalog-item-detail__param-item__state_disabled', input.disabled)
    }
  }
}
