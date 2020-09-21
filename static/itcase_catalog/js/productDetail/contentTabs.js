'use strict'

$(document).on('click', '*[data-product-tab-menu]', function changeActiceTab() {
  const baseClass = this.classList[0]
  const activeClass = `${baseClass}_state_active`
  document.querySelector(`.${activeClass}`).classList.remove(activeClass)
  this.classList.add(activeClass)

  const contentSelector = `*[data-product-tab-content="${this.dataset.productTabMenu}"]`
  const tabContent = document.querySelector(contentSelector)

  const contentBaseClass = tabContent.classList[0]
  const contentActiveClass = `${contentBaseClass}_state_active`
  document.querySelector(`.${contentActiveClass}`).classList.remove(contentActiveClass)
  tabContent.classList.add(contentActiveClass)

  $([document.documentElement, document.body]).animate(
    {
      scrollTop:
        $('.catalog-item-detail__tabs-list-item_state_active').offset().top -
        $('.header__wrapper').outerHeight() -
        12,
    },
    700
  )
})
