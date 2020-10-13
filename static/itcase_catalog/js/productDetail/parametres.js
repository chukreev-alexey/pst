/* globals Parametres */

'use strict'

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

    if (firstDiv) {
      const checkedParam = firstDiv.querySelector('input[id^="param-"]:checked')
      if (checkedParam) {
        this.activateRelatedParams(checkedParam, 1)
      }
    }
  }

  activateRelatedParams(targetInput, slideSpeed) {
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

    const pricesList = Object.entries(prices)
    const relatedParams = new Set()
    pricesList.forEach(([priceID, valuesObj]) => {
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

      let needSetNewParam = false
      for (let input of inputs) {
        // prettier-ignore
        input.disabled = (targetInput.checked)
          ? !relatedParams.has(input.value.toString())
          : false

        if (input.disabled) {
          input.checked = false
          needSetNewParam = true
        }

        const paramItem = input.closest('.catalog-item-detail__param-item')
        if (paramItem) {
          paramItem.classList.toggle('catalog-item-detail__param-item_state_disabled', input.disabled)
        }
      }

      if (needSetNewParam) {
        const firstPrice = pricesList[0][1]
        firstPrice.scope.forEach((paramID) => {
          if (paramID.toString() !== targetInput.value.toString()) {
            $(`input[id="param-${paramID}"]`).click()
          }
        })
      }
    })

    this.showInfoForSelectedParams(targetInput, slideSpeed)
  }

  showInfoForSelectedParams(targetInput, slideSpeed) {
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
      const oldPriceElement = document.querySelector('.catalog-item__price-old')

      if (oldPriceElement) {
        if (parseInt(complectation.old_price)) {
          oldPriceElement.textContent = `${complectation.old_price} р${measuring}`
          oldPriceElement.style.display = ''
        } else {
          oldPriceElement.textContent = ''
          oldPriceElement.style.display = 'none'
        }
      }

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

      this.slideToActualImage(targetInput, priceID, slideSpeed)
    }
  }

  slideToActualImage(targetInput, priceID, slideSpeed) {
    const galleryBlock = document.querySelector('.catalog-item-gallery')
    if (galleryBlock) {
      const swiper = galleryBlock.swiper
      const iamge = document.querySelector(`img[data-price-pk="${priceID}"]`)
      if (iamge) {
        const slide = iamge.closest('*[data-swiper-slide-index]')
        const index = parseInt(slide.dataset.swiperSlideIndex) || 0
        swiper.slideToLoop(index, slideSpeed)
      }
    }
  }
}

global.Parametres = new ParametresClass()

$(document).on('change', 'input[id^="param-"]', (event) => {
  Parametres.activateRelatedParams(event.target)
})
