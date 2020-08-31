$(document).on('click', '.cart-order__delivery-method-item', function () {
  const self = $(this)
  const $form = self.closest('form')
  const $address = $form.find('input[name="address"]')
  const $groupTitle = $address.closest('.cart-order__group').find('.cart-order__group-title')

  console.warn('==== delivery ====')
  console.log('self: ', self)
  console.log('form: ', $form)
  console.log('address: ', $address)
  console.log('groupTitle: ', $groupTitle)

  // 0 - 'Самовывоз'
  // 1 - 'Доставка'
  const delivery = self.data('delivery')

  console.log('delivery: ', delivery)

  if (delivery === 0) {
    $address.val('').closest('.cart-order__group').hide()
  } else {
    $address.closest('.cart-order__group').show()
  }

  // Move swicher
  $('.cart-order__delivery-method-state')
    .css({ left: delivery === 1 ? '118px' : '0' })
    .text(self.text())

  $('input[name="delivery"]').val(delivery)
})

// $(document).ready(() => {})
const delivery = $('input[name="delivery"]').val()
if (delivery || delivery === 0) {
  $(`.cart-order__delivery-method-item[data-delivery="${delivery}"]`).click()
}
