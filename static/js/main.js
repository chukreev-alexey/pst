/* globals SearchClass */

'use strict'

if (typeof SearchClass !== 'undefined') {
  global.ItcaseSearch = new SearchClass()
}

if (module.hot) {
  module.hot.accept()
}
