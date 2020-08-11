'use strict'

$(document).on('click', '*[data-sort-dropdown]', function () {
  const baseClass = this.classList[0]
  const openClass = `${baseClass}_state_open`
  const isNeedOpen = !this.classList.contains(openClass)

  this.classList.toggle(openClass, isNeedOpen)
})

$(document).on('click', '.catalog-sort-dropdown__item', function (event) {
  const dropdownBlock = this.closest('*[data-sort-dropdown]')
  if (!dropdownBlock) return event

  dropdownBlock.click()

  const currentSort = dropdownBlock.querySelector('.catalog-sort-dropdown__current')
  if (!currentSort) return event

  currentSort.textContent = this.textContent
})
