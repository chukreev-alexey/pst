/* globals Swiper */

'use strict'

if (document.querySelector('.catalog-item-gallery')) {
  new Swiper('.catalog-item-gallery', {
    wrapperClass: 'catalog-item-gallery__wrapper',
    slidesPerView: 1,
    slideClass: 'catalog-item-gallery__image',
    slideActiveClass: 'catalog-item-gallery__image-active',
    loop: true,
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
  })
}
