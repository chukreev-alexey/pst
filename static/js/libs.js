/* eslint no-unused-vars: off, import/no-webpack-loader-syntax: off */

'use strict'

import $ from 'expose-loader?exposes[]=$&exposes[]=jQuery!jquery'
import Cookies from 'expose-loader?exposes=Cookies!js-cookie'
import Swiper from 'swiper/bundle'

global.Swiper = Swiper

require('ion-rangeslider')

// Before libs call before common
$(document).on('validator_start_initialize', 'form', function () {
  $.extend($.validator.messages, { require_from_group: null })
})

if (module.hot) {
  module.hot.accept()
}
