'use strict'

import fs from 'fs'
import modules from './gulpfile.modules.js'

const PROJECT_NAME = JSON.parse(fs.readFileSync('./package.json', 'utf8')).name

const PROJECT_TYPE = 'site'
const SETTINGS = { projectType: PROJECT_TYPE }

if (PROJECT_TYPE === 'site') {
  SETTINGS.projectName = PROJECT_NAME
  SETTINGS.concatRedefineCSSDirs = ['./../']
} else if (PROJECT_TYPE === 'module') {
  SETTINGS.projectName = PROJECT_NAME.replace('-', '_')
}

export default {
  SETTINGS: SETTINGS,
  reactModules: modules.reactModules,
  jsModules: modules.jsModules,
  jsAdditionalFiles: modules.jsAdditionalFiles,
  emailTemplates: modules.emailTemplates,
}
