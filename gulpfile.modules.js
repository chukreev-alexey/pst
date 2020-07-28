'use strict'

const reactModules = {}
const jsModules = {}
const jsAdditionalFiles = []
const emailTemplates = [
  './templates/emails/**/*',
  './templates/entry/emails/**/*',
]

export default {
  reactModules: reactModules,
  jsModules: jsModules,
  jsAdditionalFiles: jsAdditionalFiles,
  emailTemplates: emailTemplates,
}
