/* eslint no-unused-vars: off, import/no-webpack-loader-syntax: off */

'use strict'

import $ from 'expose-loader?exposes[]=$&exposes[]=jQuery!./vendor/jquery'
import Cookies from 'expose-loader?exposes=Cookies!./vendor/js.cookie'
import Swiper from 'expose-loader?exposes=Swiper!./vendor/swiper'

require('./vendor/ion.rangeSlider.min.js')

// Before libs call before common
$(document).on('validator_start_initialize', 'form', function () {
  $.extend($.validator.messages, { require_from_group: null })
})

if (module.hot) {
  module.hot.accept()
}
