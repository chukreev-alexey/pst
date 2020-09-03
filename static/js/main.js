/* globals SearchClass */

'use strict'

if (typeof SearchClass !== 'undefined') {
  const searchInputs = document.querySelectorAll('input[name="search_input_text"]')
  searchInputs.forEach((input) => {
    // global.ItcaseSearch = new SearchClass({
    new SearchClass({
      element: input,
      quickSearchOnOpenClass: 'search-input',
      quickSearchPopupClass: 'search_type_quick',
      quickSearchVisibleClass: 'search_type_quick_state_visible',
      quickSearchHiddenClass: 'search_type_quick_state_hidden',
      clearValueButtonClass: 'search-input__clear',
    })
  })
}

if (module.hot) {
  module.hot.accept()
}
