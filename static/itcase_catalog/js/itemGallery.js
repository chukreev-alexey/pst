/* globals Swiper */

'use strict'

if (document.querySelector('.catalog-item-gallery')) {
  new Swiper('.catalog-item-gallery', {
    wrapperClass: 'catalog-item-gallery__wrapper',
    slidesPerView: 1,
    slideClass: 'catalog-item-gallery__image',
    slideActiveClass: 'catalog-item-gallery__image-active',
    loop: true,
    navigation: {
      nextEl: '.catalog-item-gallery__arrow_type_next',
      prevEl: '.catalog-item-gallery__arrow_type_prev',
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
  })
}
