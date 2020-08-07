'use strict'

class CatalogPopupMenu {
  constructor() {
    this.$menu = $('.catalog-menu-popup')

    this.timerShow = null
    this.timerHide = null

    this.animationEvents = 'webkitAnimationEnd oanimationend msAnimationEnd animationend'

    this.showClass = 'catalog-menu-popup_state_visible'
    this.hideClass = 'catalog-menu-popup_state_hidden'

    this.state = {
      open: this.$menu.hasClass(this.showClass),
      locked: false,
    }

    this.show = this.show.bind(this)
    this.hide = this.hide.bind(this)
  }

  show() {
    clearTimeout(this.timerHide)
    clearTimeout(this.timerShow)

    this.state.locked = true

    if (this.$menu.hasClass(this.showClass) && this.$menu.hasClass(this.hideClass)) {
      this.$menu.removeClass([this.hideClass, this.showClass].join(' ')).off(this.animationEvents)
    }

    this.timerShow = setTimeout(() => {
      this.$menu.addClass(this.showClass)
      this.state.open = true
      this.state.locked = false
    }, 0)
  }

  hide() {
    clearTimeout(this.timerHide)
    clearTimeout(this.timerShow)

    this.state.locked = true

    if (this.state.open) {
      this.timerHide = setTimeout(() => {
        this.$menu.addClass(this.hideClass).on(this.animationEvents, () => {
          this.$menu
            .removeClass([this.hideClass, this.showClass].join(' '))
            .off(this.animationEvents)

          this.state.open = false
          this.state.locked = false
        })
      }, 200)
    }
  }

  toggle() {
    if (this.state.locked) {
      return false
    }

    if (this.state.open) {
      this.hide()
    } else {
      this.show()
    }
  }
}

const $menuPopup = $('.catalog-menu__item_type_popup')

if ($menuPopup.length) {
  const menu = new CatalogPopupMenu()

  $menuPopup.on('mouseenter', menu.show).on('mouseleave', menu.hide)

  menu.$menu
    .on('mouseenter', () => {
      clearTimeout(menu.timerHide)
    })
    .on('mouseleave', menu.hide)
}