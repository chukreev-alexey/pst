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

  // if (this.checked) {
  /* getProductParametrsData() */
  //   {
  //     parametrID: this.name.replace('product_parametr-', ''),
  //     productParametrID: this.value,
  //   }
  // }
})

/*
// { parametrID, productParametrID }
const getProductParametrsData = () => {
  const checkedParams = document.querySelectorAll('input[id^="product_parametr-"]:checked')
  Array.from(checkedParams).forEach((input) => {
    const parametrID = input.name.replace('product_parametr-', '')
    const productParametrID = input.value
  })

  const requestProps = {
    method: 'POST',
    body: JSON.stringify({ parametr: 1, productParametr: 1 }),
    credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json; charset=UTF-8',
      'X-Requested-With': 'XMLHttpRequest',
      'X-CSRFToken': document.querySelector('*[name="csrfmiddlewaretoken"]')?.value,
    },
  }

  fetch('/', requestProps)
    .then((response) => {
      if (response.status === 204) {
        // The server has successfully fulfilled the request and that there is
        // no additional content to send in the response payload body.
        return response.text()
      }

      if (response.status >= 200 && response.status < 300) {
        // Success response. Get JSON.
        return response.json()
      }

      // Something wrong. Lets throw error.
      const error = new Error(response.statusText)
      error.response = response
      throw error
    })
    .then((json) => {
      console.info('==== response ====')
      console.log('json: ', json)
    })
    .catch((err) => console.error('Product parametrs request error: ', err))
}
*/
