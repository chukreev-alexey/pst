'use strict'

// Click on catalog group button(on main page) for showing hidden categories. (like "+ 12 категорий")
$(document).on('click', '.catalog-group__inner-nested-list-count', function (event) {
  event.stopPropagation()
  event.preventDefault()

  const hiddenCategories = this.parentElement.querySelectorAll('*[class*="_type_hidden"]')
  hiddenCategories.forEach((element) => {
    const hiddenClass = Array.from(element.classList).find((cls) => cls.includes('_type_hidden'))
    element.classList.remove(hiddenClass)
  })

  this.remove()
})
