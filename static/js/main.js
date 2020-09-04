'use strict'

if (typeof SearchClass !== 'undefined') {
  const searchInputs = document.querySelectorAll('input[name="search_input_text"]')
  searchInputs.forEach((input) => {
    new SearchClass({
      element: input
    })
  })
}

if (module.hot) {
  module.hot.accept()
}
