'use strict'

const reactModules = {}
const jsModules = {}
const jsAdditionalFiles = ['./static/itcase_cart/js/main.js', './static/itcase_catalog/js/main.js']
const emailTemplates = [
  './templates/emails/**/*',
  './templates/itcase_cart/emails/**/*',
  './templates/itcase_entry/emails/**/*',
]

export default {
  reactModules: reactModules,
  jsModules: jsModules,
  jsAdditionalFiles: jsAdditionalFiles,
  emailTemplates: emailTemplates,
}
