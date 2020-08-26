/* globals Parametres */

'use strict'

/*
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
  // "ID комплектации": {
  //   "scope": [ "ID связанного товара", "ID связанного товара", ... ],
  //   "price": "цена комплектации"
  // }

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

  showInfoForSelectedParams()
}

function showInfoForSelectedParams() {
  const checkedInputs = document.querySelectorAll('input[id^="param-"]:checked')
  const firstInput = checkedInputs[0]

  if (!firstInput) {
    return null
  }

  let prices = {}
  try {
    prices = JSON.parse(firstInput.dataset.prices)
  } catch (err) {
    console.error('Parsing prices for product parameters error: ', err)
    return null
  }

  const activeParams = Array.from(checkedInputs).map((input) => input.value)
}
*/

import maxBy from 'lodash/maxBy'
import isEqual from 'lodash/isEqual'
import sortBy from 'lodash/sortBy'

class ParametresClass {
  constructor() {
    this.priorityList = new Set()
    this.groupBloks = document.querySelectorAll('*[data-group-pk]')

    const firstDiv = this.groupBloks[0]

    if (firstDiv) {
      const paramCount = firstDiv.querySelectorAll('input[id^="param-"]').length
      if (paramCount > 1) {
        this.priorityList.add(firstDiv.dataset.groupPk)
      } else {
        // prettier-ignore
        const divMaxParams = maxBy(this.groupBloks, (div) => {
          return div.querySelectorAll('input[id^="param-"]').length
        })
        this.priorityList.add(divMaxParams.dataset.groupPk)
      }
    }

    this.groupBloks.forEach((div, i) => {
      this.priorityList.add(div.dataset.groupPk)
    })
  }

  activateRelatedParams(targetInput) {
    const targetGroupPk = targetInput.closest('*[data-group-pk]').dataset.groupPk
    const groupBlocks = Array.from(this.groupBloks)

    const priorityList = Array.from(this.priorityList)
    // eslint-disable-next-line
    const priorityIndex = priorityList.findIndex((pk) => pk == targetGroupPk)

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

    priorityList.forEach((groupPk, index) => {
      if (priorityIndex >= index) {
        return null
      }
      const groupBlock = groupBlocks.find((div) => div.dataset.groupPk === groupPk)
      const inputs = groupBlock.querySelectorAll('input[id^="param-"]')

      for (let input of inputs) {
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
    })

    this.showInfoForSelectedParams()
  }

  showInfoForSelectedParams() {
    const checkedInputs = document.querySelectorAll('input[id^="param-"]:checked')
    const firstInput = checkedInputs[0]

    if (!firstInput) {
      return null
    }

    let prices = {}
    try {
      prices = JSON.parse(firstInput.dataset.prices)
    } catch (err) {
      console.error('Parsing prices for product parameters error: ', err)
      return null
    }

    // to int, because "JSON.parse" make "scope" values as int (for isEqual)
    const activeParams = Array.from(checkedInputs).map((input) => parseInt(input.value))

    // prettier-ignore
    const activePrice = Object.entries(prices).find(
      ([priceID, valuesObj]) => isEqual(sortBy(valuesObj.scope), sortBy(activeParams))
    )

    if (activePrice) {
      const [priceID, complectation] = activePrice

      const priceElement = document.querySelector('.catalog-item-detail__price')

      let measuring = priceElement.dataset.measuring
      measuring = (measuring) ? `/${measuring}` : ''

      priceElement.textContent = `${complectation.price} р${measuring}`

      const addButton = document.querySelector('*[data-add-url]')
      const addUrl = addButton.dataset.addUrl
      const oldProductId = addButton.dataset.product

      delete addButton.dataset[`amount-${oldProductId}`]

      const amountInput = document.querySelector('input[name="amount"]')
      const amount = amountInput.value || 1

      // TODO: min/max
      amountInput.dataset.product = priceID

      addButton.dataset.product = priceID
      addButton.dataset[`amount-${priceID}`] = amount
      addButton.href = `${addUrl}?product=${priceID}&amount-${priceID}=${amount}`
    }
  }
}

$(document).ready(function () {
  global.Parametres = new ParametresClass()

  $(document).on('change', 'input[id^="param-"]', (event) => {
    Parametres.activateRelatedParams(event.target)
  })
})
