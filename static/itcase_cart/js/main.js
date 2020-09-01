$(document).on('click', '.cart-order__delivery-method-item', function () {
  const self = $(this)
  const $form = self.closest('form')
  const $address = $form.find('input[name="address"]')

  // 0 - 'Самовывоз'
  // 1 - 'Доставка'
  const delivery = self.data('delivery')

  if (delivery === 0) {
    $address.val('').closest('.cart-order__group').hide()
  } else {
    $address.closest('.cart-order__group').show()
  }

  // Move swicher
  const swidthPosition =
    document.querySelector('.cart-order__delivery-method-inner').offsetWidth -
    document.querySelector('[data-delivery="0"]').offsetWidth

  $('.cart-order__delivery-method-state')
    .css({ left: delivery === 1 ? swidthPosition : '0' })
    .text(self.text())

  $('input[name="delivery"]').val(delivery)
})

// $(document).ready(() => {})
const delivery = $('input[name="delivery"]').val()
if (delivery || delivery === 0) {
  $(`.cart-order__delivery-method-item[data-delivery="${delivery}"]`).click()
}
