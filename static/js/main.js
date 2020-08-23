/* globals SearchClass */

'use strict'

if (typeof SearchClass !== 'undefined') {
  global.ItcaseSearch = new SearchClass({
    quickSearchOpenClass: 'search__wrapper',
    quickSearchPopupClass: 'search_type_quick',
    quickSearchVisibleClass: 'search_type_quick_state_visible',
    quickSearchHideClass: 'search_type_quick_state_hidden',
  })
}

if (module.hot) {
  module.hot.accept()
}
