/* globals PSTCatalogFilter */
/* eslint indent: 0 */

'use strict'

function CatalogFilterFactory() {
  const animationEvents = 'webkitAnimationEnd oanimationend msAnimationEnd animationend'

  const filterPopupActiveClass = 'catalog-filter-popup_state_active'

  const catalogFilterVisible = 'catalog-filter_state_visible'
  const catalogFilterHidden = 'catalog-filter_state_hidden'

  let _isOpen = false

  const openCatalogFilter = (cb) => {
    $('.catalog-filter-popup').addClass(filterPopupActiveClass)

    const $catalogFilter = $('.catalog-filter')

    $catalogFilter.addClass(catalogFilterVisible).on(animationEvents, () => {
      $catalogFilter.off(animationEvents)
    })

    _isOpen = true
  }

  const closeCatalogFilter = () => {
    $('.catalog-filter-popup').removeClass(filterPopupActiveClass)

    const $catalogFilter = $('.catalog-filter')

    $catalogFilter.addClass(catalogFilterHidden).on(animationEvents, () => {
      $catalogFilter
        .css({ transform: '' })
        .removeClass([catalogFilterVisible, catalogFilterHidden].join(' '))
        .off(animationEvents)
    })

    _isOpen = false
  }

  return Object.freeze({
    get isOpen() {
      return _isOpen
    },
    openCatalogFilter,
    closeCatalogFilter,
  })
}

global.PSTCatalogFilter = new CatalogFilterFactory()

$(document).on('click', '.catalog-filter-popup__button', (event) => {
  event.stopPropagation()
  event.preventDefault()

  if (PSTCatalogFilter.isOpen) {
    PSTCatalogFilter.closeCatalogFilter()
  } else {
    PSTCatalogFilter.openCatalogFilter()
  }
})

$(document).on('click', (event) => {
  const $catalogFilter = $(event.target).closest('.catalog-filter, .catalog-filter-popup')

  if (!$catalogFilter.length && PSTCatalogFilter.isOpen) {
    PSTCatalogFilter.closeCatalogFilter()
  }
})
