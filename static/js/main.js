/* globals SearchClass */

'use strict'

if (typeof SearchClass !== 'undefined') {
  global.ItcaseSearch = new SearchClass({
    quickSearchOpenClass: 'search-input',
    quickSearchPopupClass: 'search_type_quick',
    quickSearchVisibleClass: 'search_type_quick_state_visible',
    quickSearchHideClass: 'search_type_quick_state_hidden',
    clearButtonClass: 'search-input__clear',
  })
}

if (module.hot) {
  module.hot.accept()
}
