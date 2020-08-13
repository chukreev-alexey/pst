'use strict'

$(document).on('click', '*[data-sort-dropdown]', function (event) {
  event.stopPropagation()
  event.preventDefault()

  const baseClass = this.classList[0]
  const openClass = `${baseClass}_state_open`
  const isNeedOpen = !this.classList.contains(openClass)

  this.classList.toggle(openClass, isNeedOpen)
})

$(document).on('click', '.catalog-sort-dropdown__item', function (event) {
  // "stopPropagation" and "preventDefault" call in itcase-common
  const dropdownBlock = this.closest('*[data-sort-dropdown]')
  if (!dropdownBlock) return event

  dropdownBlock.click()

  const currentSort = dropdownBlock.querySelector('.catalog-sort-dropdown__current')
  if (!currentSort) return event

  currentSort.textContent = this.textContent
})

$(document).on('click', (event) => {
  const sortDropdown = document.querySelector('*[data-sort-dropdown]')
  if (sortDropdown && !event.target.closest('*[data-sort-dropdown]')) {
    const openClass = `${sortDropdown.classList[0]}_state_open`
    if (sortDropdown.classList.contains(openClass)) {
      sortDropdown.classList.remove(openClass)
    }
  }
})
