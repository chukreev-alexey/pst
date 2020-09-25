/*! For license information please see __main.js.LICENSE.txt */
!function(t){var e={};function r(n){if(e[n])return e[n].exports;var o=e[n]={i:n,l:!1,exports:{}};return t[n].call(o.exports,o,o.exports,r),o.l=!0,o.exports}r.m=t,r.c=e,r.d=function(t,e,n){r.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:n})},r.r=function(t){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},r.t=function(t,e){if(1&e&&(t=r(t)),8&e)return t;if(4&e&&"object"==typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(r.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var o in t)r.d(n,o,function(e){return t[e]}.bind(null,o));return n},r.n=function(t){var e=t&&t.__esModule?function(){return t.default}:function(){return t};return r.d(e,"a",e),e},r.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},r.p="/static/js/__build/",r(r.s=169)}([,,,,,,,,,,,,,,,,,function(t,e){var r=Array.isArray;t.exports=r},,,,,,,function(t,e,r){var n=r(116),o="object"==typeof self&&self&&self.Object===Object&&self,i=n||o||Function("return this")();t.exports=i},,,,,,function(t,e){var r;r=function(){return this}();try{r=r||new Function("return this")()}catch(t){"object"==typeof window&&(r=window)}t.exports=r},function(t,e,r){var n=r(196),o=r(199);t.exports=function(t,e){var r=o(t,e);return n(r)?r:void 0}},,,,,,,,,,,,,,,,,function(t,e,r){var n=r(49),o=r(51);t.exports=function(t){return"symbol"==typeof t||o(t)&&"[object Symbol]"==n(t)}},function(t,e,r){var n=r(50),o=r(181),i=r(182),a=n?n.toStringTag:void 0;t.exports=function(t){return null==t?void 0===t?"[object Undefined]":"[object Null]":a&&a in Object(t)?o(t):i(t)}},function(t,e,r){var n=r(24).Symbol;t.exports=n},function(t,e){t.exports=function(t){return null!=t&&"object"==typeof t}},,,,,function(t,e,r){var n=r(186),o=r(187),i=r(188),a=r(189),c=r(190);function s(t){var e=-1,r=null==t?0:t.length;for(this.clear();++e<r;){var n=t[e];this.set(n[0],n[1])}}s.prototype.clear=n,s.prototype.delete=o,s.prototype.get=i,s.prototype.has=a,s.prototype.set=c,t.exports=s},function(t,e,r){var n=r(77);t.exports=function(t,e){for(var r=t.length;r--;)if(n(t[r][0],e))return r;return-1}},function(t,e){t.exports=function(t){var e=typeof t;return null!=t&&("object"==e||"function"==e)}},function(t,e,r){var n=r(31)(Object,"create");t.exports=n},function(t,e,r){var n=r(208);t.exports=function(t,e){var r=t.__data__;return n(e)?r["string"==typeof e?"string":"hash"]:r.map}},function(t,e,r){var n=r(119),o=r(84);t.exports=function(t){return null!=t&&o(t.length)&&!n(t)}},function(t,e,r){var n=r(48);t.exports=function(t){if("string"==typeof t||n(t))return t;var e=t+"";return"0"==e&&1/t==-Infinity?"-0":e}},function(t,e){t.exports=function(t){return t}},,,,,,,,,,,,,,function(t,e){t.exports=function(t,e){return t===e||t!=t&&e!=e}},function(t,e,r){var n=r(31)(r(24),"Map");t.exports=n},function(t,e,r){var n=r(200),o=r(207),i=r(209),a=r(210),c=r(211);function s(t){var e=-1,r=null==t?0:t.length;for(this.clear();++e<r;){var n=t[e];this.set(n[0],n[1])}}s.prototype.clear=n,s.prototype.delete=o,s.prototype.get=i,s.prototype.has=a,s.prototype.set=c,t.exports=s},function(t,e,r){var n=r(212),o=r(51);t.exports=function t(e,r,i,a,c){return e===r||(null==e||null==r||!o(e)&&!o(r)?e!=e&&r!=r:n(e,r,i,a,t,c))}},function(t,e,r){var n=r(228),o=r(234),i=r(61);t.exports=function(t){return i(t)?n(t):o(t)}},function(t,e,r){var n=r(230),o=r(51),i=Object.prototype,a=i.hasOwnProperty,c=i.propertyIsEnumerable,s=n(function(){return arguments}())?n:function(t){return o(t)&&a.call(t,"callee")&&!c.call(t,"callee")};t.exports=s},function(t,e){var r=/^(?:0|[1-9]\d*)$/;t.exports=function(t,e){var n=typeof t;return!!(e=null==e?9007199254740991:e)&&("number"==n||"symbol"!=n&&r.test(t))&&t>-1&&t%1==0&&t<e}},function(t,e){t.exports=function(t){return"number"==typeof t&&t>-1&&t%1==0&&t<=9007199254740991}},function(t,e,r){var n=r(129),o=r(62);t.exports=function(t,e){for(var r=0,i=(e=n(e,t)).length;null!=t&&r<i;)t=t[o(e[r++])];return r&&r==i?t:void 0}},function(t,e,r){var n=r(17),o=r(48),i=/\.|\[(?:[^[\]]*|(["'])(?:(?!\1)[^\\]|\\.)*?\1)\]/,a=/^\w*$/;t.exports=function(t,e){if(n(t))return!1;var r=typeof t;return!("number"!=r&&"symbol"!=r&&"boolean"!=r&&null!=t&&!o(t))||(a.test(t)||!i.test(t)||null!=e&&t in Object(e))}},,,,,,,,,,,,,,,,,,,,,,,,,,,,,function(t,e,r){var n=r(257),o=r(259),i=r(269),a=r(277),c=i((function(t,e){if(null==t)return[];var r=e.length;return r>1&&a(t,e[0],e[1])?e=[]:r>2&&a(e[0],e[1],e[2])&&(e=[e[0]]),o(t,n(e,1),[])}));t.exports=c},function(t,e,r){(function(e){var r="object"==typeof e&&e&&e.Object===Object&&e;t.exports=r}).call(this,r(30))},function(t,e,r){var n=r(184),o=r(244),i=r(63),a=r(17),c=r(254);t.exports=function(t){return"function"==typeof t?t:null==t?i:"object"==typeof t?a(t)?o(t[0],t[1]):n(t):c(t)}},function(t,e,r){var n=r(56),o=r(191),i=r(192),a=r(193),c=r(194),s=r(195);function u(t){var e=this.__data__=new n(t);this.size=e.size}u.prototype.clear=o,u.prototype.delete=i,u.prototype.get=a,u.prototype.has=c,u.prototype.set=s,t.exports=u},function(t,e,r){var n=r(49),o=r(58);t.exports=function(t){if(!o(t))return!1;var e=n(t);return"[object Function]"==e||"[object GeneratorFunction]"==e||"[object AsyncFunction]"==e||"[object Proxy]"==e}},function(t,e){var r=Function.prototype.toString;t.exports=function(t){if(null!=t){try{return r.call(t)}catch(t){}try{return t+""}catch(t){}}return""}},function(t,e,r){var n=r(213),o=r(216),i=r(217);t.exports=function(t,e,r,a,c,s){var u=1&r,l=t.length,f=e.length;if(l!=f&&!(u&&f>l))return!1;var p=s.get(t),d=s.get(e);if(p&&d)return p==e&&d==t;var h=-1,v=!0,m=2&r?new n:void 0;for(s.set(t,e),s.set(e,t);++h<l;){var g=t[h],_=e[h];if(a)var y=u?a(_,g,h,e,t,s):a(g,_,h,t,e,s);if(void 0!==y){if(y)continue;v=!1;break}if(m){if(!o(e,(function(t,e){if(!i(m,e)&&(g===t||c(g,t,r,a,s)))return m.push(e)}))){v=!1;break}}else if(g!==_&&!c(g,_,r,a,s)){v=!1;break}}return s.delete(t),s.delete(e),v}},function(t,e){t.exports=function(t,e){for(var r=-1,n=e.length,o=t.length;++r<n;)t[o+r]=e[r];return t}},function(t,e,r){(function(t){var n=r(24),o=r(231),i=e&&!e.nodeType&&e,a=i&&"object"==typeof t&&t&&!t.nodeType&&t,c=a&&a.exports===i?n.Buffer:void 0,s=(c?c.isBuffer:void 0)||o;t.exports=s}).call(this,r(124)(t))},function(t,e){t.exports=function(t){return t.webpackPolyfill||(t.deprecate=function(){},t.paths=[],t.children||(t.children=[]),Object.defineProperty(t,"loaded",{enumerable:!0,get:function(){return t.l}}),Object.defineProperty(t,"id",{enumerable:!0,get:function(){return t.i}}),t.webpackPolyfill=1),t}},function(t,e,r){var n=r(232),o=r(126),i=r(233),a=i&&i.isTypedArray,c=a?o(a):n;t.exports=c},function(t,e){t.exports=function(t){return function(e){return t(e)}}},function(t,e,r){var n=r(58);t.exports=function(t){return t==t&&!n(t)}},function(t,e){t.exports=function(t,e){return function(r){return null!=r&&(r[t]===e&&(void 0!==e||t in Object(r)))}}},function(t,e,r){var n=r(17),o=r(86),i=r(246),a=r(249);t.exports=function(t,e){return n(t)?t:o(t,e)?[t]:i(a(t))}},function(t,e){t.exports=function(t,e){for(var r=-1,n=null==t?0:t.length,o=Array(n);++r<n;)o[r]=e(t[r],r,t);return o}},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,function(t,e,r){var n=r(180),o=r(183),i=r(117);t.exports=function(t,e){return t&&t.length?n(t,i(e,2),o):void 0}},function(t,e,r){var n=r(80);t.exports=function(t,e){return n(t,e)}},,function(t,e,r){r(170),r(172),t.exports=r(173)},function(t,e,r){"use strict";r(171)},function(t,e,r){"use strict";if("undefined"!=typeof SearchClass){document.querySelectorAll('input[name="search_input_text"]').forEach(t=>{new SearchClass({element:t})})}},function(t,e){$(document).on("click",".cart-order__delivery-method-item",(function(){const t=$(this),e=t.closest("form").find('input[name="address"]'),r=t.data("delivery");0===r?e.val("").closest(".cart-order__group").hide():e.closest(".cart-order__group").show();const n=document.querySelector(".cart-order__delivery-method-inner").offsetWidth-document.querySelector('[data-delivery="0"]').offsetWidth;$(".cart-order__delivery-method-state").css({left:1===r?n:"0"}).text(t.text()),$('input[name="delivery"]').val(r)}));const r=$('input[name="delivery"]').val();(r||0===r)&&$(`.cart-order__delivery-method-item[data-delivery="${r}"]`).click()},function(t,e,r){"use strict";(function(t){r(174),r(175),r(176),r(177),r(472),r(178),r(179),r(278),"undefined"!=typeof UserCartClass&&(t.UserCart=new UserCartClass({headerCartButton:"cart-button",headerCartButtonText:"cart-button__text-sum",headerCartButtonCount:"cart-button__text-count",emptyCartText:"Заказ",changeCartText:(t,e,r)=>{const n=document.querySelector("."+UserCart.props.headerCartButton),o=UserCart.getCartPriceText(e,"р");if(n.innerHTML.includes(UserCart.props.emptyCartText)){const e=n.querySelector(".cart-button__text");UserCart.replaceHeaderCartButtonEmptyText(e||n,t,o)}UserCart.cartCountBlock.length&&UserCart.cartCountBlock.text(t),UserCart.cartTextBlock.length&&UserCart.cartTextBlock.text(o),UserCart.orderSumTitleBlock.length&&UserCart.orderSumTitleBlock.text(o)},addToCartButton:".catalog-item__button, .search-result-list__item-button-add",productAmountInput:"cart-list__item-count-input",productAmountMinusButton:"cart-list__item-count-button_action_minus",productAmountPlusButton:"cart-list__item-count-button_action_plus",deleteFromCartButton:"cart-list__item-action-link",orderPaymentItem:"cart-order__payment-item",orderPaymentItemChecked:"cart-order__payment-item_state_checked",orderAgreeCheckbox:"cart-order__agree-checkbox",orderAgreeCheckboxChecked:"cart-order__agree_state_checked",priceFractionDigits:2,cartListContainer:"cart-list",cartListProductRow:"cart-list__item",cartListProductSum:"cart-list__item-cost-second",cartListOrderSum:"cart-list-sum__amount"}),UserCart.getCartPriceText=function(t,e){e=e?e.toUpperCase():this.getNumEnding(t,["рубль","рубля","рублей"]);const r=parseFloat(t),n=isFinite(r)&&Math.floor(r)===r?0:this.props.priceFractionDigits;return`${r.toLocaleString("ru-RU",{minimumFractionDigits:n,maximumFractionDigits:n})} ${e}`},UserCart.calculateOrderSum=function(){const{productAmountInput:t,cartListOrderSum:e}=this.props,r=$("."+e);if(!r.length)return null;let n=0;$("."+t).each((t,e)=>{const r=e.dataset.price.toString().replace(/\s/g,"");n+=e.value*parseFloat(r.replace(",","."))});const o=r.text().replace(/\r?\n|\r/g,"").trim().split(" ").filter(Boolean),i=o.length>1?o[1]||"":o[0]||"";if("р"===i.toLowerCase()||i.toLowerCase().startsWith("руб")){const t=isFinite(n)&&Math.floor(n)===n?0:this.props.priceFractionDigits,e={minimumFractionDigits:t,maximumFractionDigits:t};n=n.toLocaleString("ru-RU",e)}else n=n.toFixed(2);r.text(`${n} ${i}`)});const e=()=>{const t=$("input[data-price-min]"),e=$("input[data-price-max]"),r=ItcaseFilter.getCurrentFiltersFromUrl();if("price-max"in r&&e.val(r["price-max"]),"price-min"in r&&t.val(r["price-min"]),t.length&&e.length){const r=parseInt(t.val(),10)||0,n=parseInt(e.val(),10)||1e5;(!ItcaseFilter.rangeFirstMinVal||r<ItcaseFilter.rangeFirstMinVal)&&(ItcaseFilter.rangeFirstMinVal=parseInt(t.data("price-min"),10)||r),(!ItcaseFilter.rangeFirstMaxVal||n>ItcaseFilter.rangeFirstMaxVal)&&(ItcaseFilter.rangeFirstMaxVal=parseInt(e.data("price-max"),10)||n),$("*[data-range-slider]").ionRangeSlider({type:"double",min:ItcaseFilter.rangeFirstMinVal,max:ItcaseFilter.rangeFirstMaxVal,hide_min_max:!0,hide_from_to:!1,from:r,to:n,postfix:" р",onStart:r=>{t.val(r.from),e.val(r.to)},onChange:r=>{t.val(r.from),e.val(r.to)},onFinish:t=>{ItcaseFilter.sendCheckedFilters()}})}};"undefined"!=typeof ItcaseFilterClass&&(t.ItcaseFilter=new ItcaseFilterClass({dropPagination:!0,productListClass:"catalog-list",sortBlockClass:"catalog-sort",filterClearButtonClass:"catalog-filter__clear",sortItemClass:["catalog-sort__group-item","catalog-sort-dropdown__item"],contentRequestCB:e,prepareHtmlBeforeReplace:t=>{t.classList.contains("catalog-filter")&&PSTCatalogFilter.isOpen&&t.classList.add("catalog-filter_state_visible");if(t.classList.contains("catalog-group-page")&&PSTCatalogFilter.isOpen){const e=t.querySelector(".catalog-filter");e&&e.classList.add("catalog-filter_state_visible")}}})),$(document).ready(()=>{e()})}).call(this,r(30))},function(t,e,r){"use strict";$(document).on("click",".catalog-group__inner-nested-list-count",(function(t){t.stopPropagation(),t.preventDefault();this.parentElement.querySelectorAll('*[class*="_type_hidden"]').forEach(t=>{const e=Array.from(t.classList).find(t=>t.includes("_type_hidden"));t.classList.remove(e)}),this.remove()}))},function(t,e,r){"use strict";$(document).on("click","*[data-sort-dropdown]",(function(t){t.stopPropagation(),t.preventDefault();const e=this.classList[0]+"_state_open",r=!this.classList.contains(e);this.classList.toggle(e,r)})),$(document).on("click",".catalog-sort-dropdown__item",(function(t){const e=this.closest("*[data-sort-dropdown]");if(!e)return t;e.click();const r=e.querySelector(".catalog-sort-dropdown__current");if(!r)return t;r.textContent=this.textContent})),$(document).on("click",t=>{const e=document.querySelector("*[data-sort-dropdown]");if(e&&!t.target.closest("*[data-sort-dropdown]")){const t=e.classList[0]+"_state_open";e.classList.contains(t)&&e.classList.remove(t)}})},function(t,e,r){"use strict";(function(t){t.PSTCatalogFilter=new function(){const t="webkitAnimationEnd oanimationend msAnimationEnd animationend",e="catalog-filter-popup_state_active",r="catalog-filter_state_visible",n="catalog-filter_state_hidden";let o=!1;return Object.freeze({get isOpen(){return o},openCatalogFilter:n=>{$(".catalog-filter-popup").addClass(e);const i=$(".catalog-filter");i.addClass(r).on(t,()=>{i.off(t)}),o=!0},closeCatalogFilter:()=>{$(".catalog-filter-popup").removeClass(e);const i=$(".catalog-filter");i.addClass(n).on(t,()=>{i.css({transform:""}).removeClass([r,n].join(" ")).off(t)}),o=!1}})},$(document).on("click",".catalog-filter-popup__button",t=>{t.stopPropagation(),t.preventDefault(),PSTCatalogFilter.isOpen?PSTCatalogFilter.closeCatalogFilter():PSTCatalogFilter.openCatalogFilter()}),$(document).on("click",t=>{!$(t.target).closest(".catalog-filter, .catalog-filter-popup").length&&PSTCatalogFilter.isOpen&&PSTCatalogFilter.closeCatalogFilter()})}).call(this,r(30))},function(t,e,r){"use strict";document.querySelector(".catalog-item-gallery")&&new Swiper(".catalog-item-gallery",{wrapperClass:"catalog-item-gallery__wrapper",slidesPerView:1,slideClass:"catalog-item-gallery__image",slideActiveClass:"catalog-item-gallery__image-active",loop:!0,navigation:{nextEl:".catalog-item-gallery__arrow_type_next",prevEl:".catalog-item-gallery__arrow_type_prev"},pagination:{el:".swiper-pagination",clickable:!0}})},function(t,e,r){"use strict";$(document).on("click","*[data-product-tab-menu]",(function(){const t=this.classList[0]+"_state_active";document.querySelector("."+t).classList.remove(t),this.classList.add(t);const e=`*[data-product-tab-content="${this.dataset.productTabMenu}"]`,r=document.querySelector(e),n=r.classList[0]+"_state_active";document.querySelector("."+n).classList.remove(n),r.classList.add(n),$([document.documentElement,document.body]).animate({scrollTop:$(".catalog-item-detail__tabs-list-item_state_active").offset().top-$(".header__wrapper").outerHeight()-12},700)}))},function(t,e,r){"use strict";r.r(e),function(t){var e=r(166),n=r.n(e),o=r(167),i=r.n(o),a=r(115),c=r.n(a);t.Parametres=new class{constructor(){this.priorityList=new Set,this.groupBloks=document.querySelectorAll("*[data-group-pk]");const t=this.groupBloks[0];if(t){if(t.querySelectorAll('input[id^="param-"]').length>1)this.priorityList.add(t.dataset.groupPk);else{const t=n()(this.groupBloks,t=>t.querySelectorAll('input[id^="param-"]').length);this.priorityList.add(t.dataset.groupPk)}}if(this.groupBloks.forEach((t,e)=>{this.priorityList.add(t.dataset.groupPk)}),t){const e=t.querySelector('input[id^="param-"]:checked');e&&this.activateRelatedParams(e,1)}}activateRelatedParams(t,e){const r=t.closest("*[data-group-pk]").dataset.groupPk,n=Array.from(this.groupBloks),o=Array.from(this.priorityList),i=o.findIndex(t=>t==r);let a={};try{a=JSON.parse(t.dataset.prices)}catch(t){return console.error("Parsing prices for product parameters error: ",t),null}const c=Object.entries(a),s=new Set;c.forEach(([e,r])=>{r.scope.forEach(e=>{const r=e.toString();r!==t.value.toString()&&s.add(r)})}),o.forEach((e,r)=>{if(i>=r)return null;const o=n.find(t=>t.dataset.groupPk===e).querySelectorAll('input[id^="param-"]');let a=!1;for(let e of o){e.disabled=!!t.checked&&!s.has(e.value.toString()),e.disabled&&(e.checked=!1,a=!0);const r=e.closest(".catalog-item-detail__param-item");r&&r.classList.toggle("catalog-item-detail__param-item_state_disabled",e.disabled)}if(a){c[0][1].scope.forEach(e=>{e.toString()!==t.value.toString()&&$(`input[id="param-${e}"]`).click()})}}),this.showInfoForSelectedParams(t,e)}showInfoForSelectedParams(t,e){const r=document.querySelectorAll('input[id^="param-"]:checked'),n=r[0];if(!n)return null;let o={};try{o=JSON.parse(n.dataset.prices)}catch(t){return console.error("Parsing prices for product parameters error: ",t),null}const a=Array.from(r).map(t=>parseInt(t.value)),s=Object.entries(o).find(([t,e])=>i()(c()(e.scope),c()(a)));if(s){const[r,n]=s,o=document.querySelector(".catalog-item-detail__price");let i=o.dataset.measuring;i=i?"/"+i:"",o.textContent=`${n.price} р${i}`;const a=document.querySelector("*[data-add-url]"),c=a.dataset.addUrl,u=a.dataset.product;delete a.dataset["amount-"+u];const l=document.querySelector('input[name="amount"]'),f=l.value||1;l.dataset.product=r,a.dataset.product=r,a.dataset["amount-"+r]=f,a.href=`${c}?product=${r}&amount-${r}=${f}`,this.slideToActualImage(t,r,e)}}slideToActualImage(t,e,r){const n=document.querySelector(".catalog-item-gallery");if(n){const t=n.swiper,o=document.querySelector(`img[data-price-pk="${e}"]`);if(o){const e=o.closest("*[data-swiper-slide-index]"),n=parseInt(e.dataset.swiperSlideIndex)||0;t.slideToLoop(n,r)}}}},$(document).on("change",'input[id^="param-"]',t=>{Parametres.activateRelatedParams(t.target)})}.call(this,r(30))},function(t,e,r){var n=r(48);t.exports=function(t,e,r){for(var o=-1,i=t.length;++o<i;){var a=t[o],c=e(a);if(null!=c&&(void 0===s?c==c&&!n(c):r(c,s)))var s=c,u=a}return u}},function(t,e,r){var n=r(50),o=Object.prototype,i=o.hasOwnProperty,a=o.toString,c=n?n.toStringTag:void 0;t.exports=function(t){var e=i.call(t,c),r=t[c];try{t[c]=void 0;var n=!0}catch(t){}var o=a.call(t);return n&&(e?t[c]=r:delete t[c]),o}},function(t,e){var r=Object.prototype.toString;t.exports=function(t){return r.call(t)}},function(t,e){t.exports=function(t,e){return t>e}},function(t,e,r){var n=r(185),o=r(243),i=r(128);t.exports=function(t){var e=o(t);return 1==e.length&&e[0][2]?i(e[0][0],e[0][1]):function(r){return r===t||n(r,t,e)}}},function(t,e,r){var n=r(118),o=r(80);t.exports=function(t,e,r,i){var a=r.length,c=a,s=!i;if(null==t)return!c;for(t=Object(t);a--;){var u=r[a];if(s&&u[2]?u[1]!==t[u[0]]:!(u[0]in t))return!1}for(;++a<c;){var l=(u=r[a])[0],f=t[l],p=u[1];if(s&&u[2]){if(void 0===f&&!(l in t))return!1}else{var d=new n;if(i)var h=i(f,p,l,t,e,d);if(!(void 0===h?o(p,f,3,i,d):h))return!1}}return!0}},function(t,e){t.exports=function(){this.__data__=[],this.size=0}},function(t,e,r){var n=r(57),o=Array.prototype.splice;t.exports=function(t){var e=this.__data__,r=n(e,t);return!(r<0)&&(r==e.length-1?e.pop():o.call(e,r,1),--this.size,!0)}},function(t,e,r){var n=r(57);t.exports=function(t){var e=this.__data__,r=n(e,t);return r<0?void 0:e[r][1]}},function(t,e,r){var n=r(57);t.exports=function(t){return n(this.__data__,t)>-1}},function(t,e,r){var n=r(57);t.exports=function(t,e){var r=this.__data__,o=n(r,t);return o<0?(++this.size,r.push([t,e])):r[o][1]=e,this}},function(t,e,r){var n=r(56);t.exports=function(){this.__data__=new n,this.size=0}},function(t,e){t.exports=function(t){var e=this.__data__,r=e.delete(t);return this.size=e.size,r}},function(t,e){t.exports=function(t){return this.__data__.get(t)}},function(t,e){t.exports=function(t){return this.__data__.has(t)}},function(t,e,r){var n=r(56),o=r(78),i=r(79);t.exports=function(t,e){var r=this.__data__;if(r instanceof n){var a=r.__data__;if(!o||a.length<199)return a.push([t,e]),this.size=++r.size,this;r=this.__data__=new i(a)}return r.set(t,e),this.size=r.size,this}},function(t,e,r){var n=r(119),o=r(197),i=r(58),a=r(120),c=/^\[object .+?Constructor\]$/,s=Function.prototype,u=Object.prototype,l=s.toString,f=u.hasOwnProperty,p=RegExp("^"+l.call(f).replace(/[\\^$.*+?()[\]{}|]/g,"\\$&").replace(/hasOwnProperty|(function).*?(?=\\\()| for .+?(?=\\\])/g,"$1.*?")+"$");t.exports=function(t){return!(!i(t)||o(t))&&(n(t)?p:c).test(a(t))}},function(t,e,r){var n,o=r(198),i=(n=/[^.]+$/.exec(o&&o.keys&&o.keys.IE_PROTO||""))?"Symbol(src)_1."+n:"";t.exports=function(t){return!!i&&i in t}},function(t,e,r){var n=r(24)["__core-js_shared__"];t.exports=n},function(t,e){t.exports=function(t,e){return null==t?void 0:t[e]}},function(t,e,r){var n=r(201),o=r(56),i=r(78);t.exports=function(){this.size=0,this.__data__={hash:new n,map:new(i||o),string:new n}}},function(t,e,r){var n=r(202),o=r(203),i=r(204),a=r(205),c=r(206);function s(t){var e=-1,r=null==t?0:t.length;for(this.clear();++e<r;){var n=t[e];this.set(n[0],n[1])}}s.prototype.clear=n,s.prototype.delete=o,s.prototype.get=i,s.prototype.has=a,s.prototype.set=c,t.exports=s},function(t,e,r){var n=r(59);t.exports=function(){this.__data__=n?n(null):{},this.size=0}},function(t,e){t.exports=function(t){var e=this.has(t)&&delete this.__data__[t];return this.size-=e?1:0,e}},function(t,e,r){var n=r(59),o=Object.prototype.hasOwnProperty;t.exports=function(t){var e=this.__data__;if(n){var r=e[t];return"__lodash_hash_undefined__"===r?void 0:r}return o.call(e,t)?e[t]:void 0}},function(t,e,r){var n=r(59),o=Object.prototype.hasOwnProperty;t.exports=function(t){var e=this.__data__;return n?void 0!==e[t]:o.call(e,t)}},function(t,e,r){var n=r(59);t.exports=function(t,e){var r=this.__data__;return this.size+=this.has(t)?0:1,r[t]=n&&void 0===e?"__lodash_hash_undefined__":e,this}},function(t,e,r){var n=r(60);t.exports=function(t){var e=n(this,t).delete(t);return this.size-=e?1:0,e}},function(t,e){t.exports=function(t){var e=typeof t;return"string"==e||"number"==e||"symbol"==e||"boolean"==e?"__proto__"!==t:null===t}},function(t,e,r){var n=r(60);t.exports=function(t){return n(this,t).get(t)}},function(t,e,r){var n=r(60);t.exports=function(t){return n(this,t).has(t)}},function(t,e,r){var n=r(60);t.exports=function(t,e){var r=n(this,t),o=r.size;return r.set(t,e),this.size+=r.size==o?0:1,this}},function(t,e,r){var n=r(118),o=r(121),i=r(218),a=r(222),c=r(238),s=r(17),u=r(123),l=r(125),f="[object Arguments]",p="[object Array]",d="[object Object]",h=Object.prototype.hasOwnProperty;t.exports=function(t,e,r,v,m,g){var _=s(t),y=s(e),x=_?p:c(t),b=y?p:c(e),w=(x=x==f?d:x)==d,j=(b=b==f?d:b)==d,C=x==b;if(C&&u(t)){if(!u(e))return!1;_=!0,w=!1}if(C&&!w)return g||(g=new n),_||l(t)?o(t,e,r,v,m,g):i(t,e,x,r,v,m,g);if(!(1&r)){var S=w&&h.call(t,"__wrapped__"),$=j&&h.call(e,"__wrapped__");if(S||$){var k=S?t.value():t,O=$?e.value():e;return g||(g=new n),m(k,O,r,v,g)}}return!!C&&(g||(g=new n),a(t,e,r,v,m,g))}},function(t,e,r){var n=r(79),o=r(214),i=r(215);function a(t){var e=-1,r=null==t?0:t.length;for(this.__data__=new n;++e<r;)this.add(t[e])}a.prototype.add=a.prototype.push=o,a.prototype.has=i,t.exports=a},function(t,e){t.exports=function(t){return this.__data__.set(t,"__lodash_hash_undefined__"),this}},function(t,e){t.exports=function(t){return this.__data__.has(t)}},function(t,e){t.exports=function(t,e){for(var r=-1,n=null==t?0:t.length;++r<n;)if(e(t[r],r,t))return!0;return!1}},function(t,e){t.exports=function(t,e){return t.has(e)}},function(t,e,r){var n=r(50),o=r(219),i=r(77),a=r(121),c=r(220),s=r(221),u=n?n.prototype:void 0,l=u?u.valueOf:void 0;t.exports=function(t,e,r,n,u,f,p){switch(r){case"[object DataView]":if(t.byteLength!=e.byteLength||t.byteOffset!=e.byteOffset)return!1;t=t.buffer,e=e.buffer;case"[object ArrayBuffer]":return!(t.byteLength!=e.byteLength||!f(new o(t),new o(e)));case"[object Boolean]":case"[object Date]":case"[object Number]":return i(+t,+e);case"[object Error]":return t.name==e.name&&t.message==e.message;case"[object RegExp]":case"[object String]":return t==e+"";case"[object Map]":var d=c;case"[object Set]":var h=1&n;if(d||(d=s),t.size!=e.size&&!h)return!1;var v=p.get(t);if(v)return v==e;n|=2,p.set(t,e);var m=a(d(t),d(e),n,u,f,p);return p.delete(t),m;case"[object Symbol]":if(l)return l.call(t)==l.call(e)}return!1}},function(t,e,r){var n=r(24).Uint8Array;t.exports=n},function(t,e){t.exports=function(t){var e=-1,r=Array(t.size);return t.forEach((function(t,n){r[++e]=[n,t]})),r}},function(t,e){t.exports=function(t){var e=-1,r=Array(t.size);return t.forEach((function(t){r[++e]=t})),r}},function(t,e,r){var n=r(223),o=Object.prototype.hasOwnProperty;t.exports=function(t,e,r,i,a,c){var s=1&r,u=n(t),l=u.length;if(l!=n(e).length&&!s)return!1;for(var f=l;f--;){var p=u[f];if(!(s?p in e:o.call(e,p)))return!1}var d=c.get(t),h=c.get(e);if(d&&h)return d==e&&h==t;var v=!0;c.set(t,e),c.set(e,t);for(var m=s;++f<l;){var g=t[p=u[f]],_=e[p];if(i)var y=s?i(_,g,p,e,t,c):i(g,_,p,t,e,c);if(!(void 0===y?g===_||a(g,_,r,i,c):y)){v=!1;break}m||(m="constructor"==p)}if(v&&!m){var x=t.constructor,b=e.constructor;x==b||!("constructor"in t)||!("constructor"in e)||"function"==typeof x&&x instanceof x&&"function"==typeof b&&b instanceof b||(v=!1)}return c.delete(t),c.delete(e),v}},function(t,e,r){var n=r(224),o=r(225),i=r(81);t.exports=function(t){return n(t,i,o)}},function(t,e,r){var n=r(122),o=r(17);t.exports=function(t,e,r){var i=e(t);return o(t)?i:n(i,r(t))}},function(t,e,r){var n=r(226),o=r(227),i=Object.prototype.propertyIsEnumerable,a=Object.getOwnPropertySymbols,c=a?function(t){return null==t?[]:(t=Object(t),n(a(t),(function(e){return i.call(t,e)})))}:o;t.exports=c},function(t,e){t.exports=function(t,e){for(var r=-1,n=null==t?0:t.length,o=0,i=[];++r<n;){var a=t[r];e(a,r,t)&&(i[o++]=a)}return i}},function(t,e){t.exports=function(){return[]}},function(t,e,r){var n=r(229),o=r(82),i=r(17),a=r(123),c=r(83),s=r(125),u=Object.prototype.hasOwnProperty;t.exports=function(t,e){var r=i(t),l=!r&&o(t),f=!r&&!l&&a(t),p=!r&&!l&&!f&&s(t),d=r||l||f||p,h=d?n(t.length,String):[],v=h.length;for(var m in t)!e&&!u.call(t,m)||d&&("length"==m||f&&("offset"==m||"parent"==m)||p&&("buffer"==m||"byteLength"==m||"byteOffset"==m)||c(m,v))||h.push(m);return h}},function(t,e){t.exports=function(t,e){for(var r=-1,n=Array(t);++r<t;)n[r]=e(r);return n}},function(t,e,r){var n=r(49),o=r(51);t.exports=function(t){return o(t)&&"[object Arguments]"==n(t)}},function(t,e){t.exports=function(){return!1}},function(t,e,r){var n=r(49),o=r(84),i=r(51),a={};a["[object Float32Array]"]=a["[object Float64Array]"]=a["[object Int8Array]"]=a["[object Int16Array]"]=a["[object Int32Array]"]=a["[object Uint8Array]"]=a["[object Uint8ClampedArray]"]=a["[object Uint16Array]"]=a["[object Uint32Array]"]=!0,a["[object Arguments]"]=a["[object Array]"]=a["[object ArrayBuffer]"]=a["[object Boolean]"]=a["[object DataView]"]=a["[object Date]"]=a["[object Error]"]=a["[object Function]"]=a["[object Map]"]=a["[object Number]"]=a["[object Object]"]=a["[object RegExp]"]=a["[object Set]"]=a["[object String]"]=a["[object WeakMap]"]=!1,t.exports=function(t){return i(t)&&o(t.length)&&!!a[n(t)]}},function(t,e,r){(function(t){var n=r(116),o=e&&!e.nodeType&&e,i=o&&"object"==typeof t&&t&&!t.nodeType&&t,a=i&&i.exports===o&&n.process,c=function(){try{var t=i&&i.require&&i.require("util").types;return t||a&&a.binding&&a.binding("util")}catch(t){}}();t.exports=c}).call(this,r(124)(t))},function(t,e,r){var n=r(235),o=r(236),i=Object.prototype.hasOwnProperty;t.exports=function(t){if(!n(t))return o(t);var e=[];for(var r in Object(t))i.call(t,r)&&"constructor"!=r&&e.push(r);return e}},function(t,e){var r=Object.prototype;t.exports=function(t){var e=t&&t.constructor;return t===("function"==typeof e&&e.prototype||r)}},function(t,e,r){var n=r(237)(Object.keys,Object);t.exports=n},function(t,e){t.exports=function(t,e){return function(r){return t(e(r))}}},function(t,e,r){var n=r(239),o=r(78),i=r(240),a=r(241),c=r(242),s=r(49),u=r(120),l="[object Map]",f="[object Promise]",p="[object Set]",d="[object WeakMap]",h="[object DataView]",v=u(n),m=u(o),g=u(i),_=u(a),y=u(c),x=s;(n&&x(new n(new ArrayBuffer(1)))!=h||o&&x(new o)!=l||i&&x(i.resolve())!=f||a&&x(new a)!=p||c&&x(new c)!=d)&&(x=function(t){var e=s(t),r="[object Object]"==e?t.constructor:void 0,n=r?u(r):"";if(n)switch(n){case v:return h;case m:return l;case g:return f;case _:return p;case y:return d}return e}),t.exports=x},function(t,e,r){var n=r(31)(r(24),"DataView");t.exports=n},function(t,e,r){var n=r(31)(r(24),"Promise");t.exports=n},function(t,e,r){var n=r(31)(r(24),"Set");t.exports=n},function(t,e,r){var n=r(31)(r(24),"WeakMap");t.exports=n},function(t,e,r){var n=r(127),o=r(81);t.exports=function(t){for(var e=o(t),r=e.length;r--;){var i=e[r],a=t[i];e[r]=[i,a,n(a)]}return e}},function(t,e,r){var n=r(80),o=r(245),i=r(251),a=r(86),c=r(127),s=r(128),u=r(62);t.exports=function(t,e){return a(t)&&c(e)?s(u(t),e):function(r){var a=o(r,t);return void 0===a&&a===e?i(r,t):n(e,a,3)}}},function(t,e,r){var n=r(85);t.exports=function(t,e,r){var o=null==t?void 0:n(t,e);return void 0===o?r:o}},function(t,e,r){var n=r(247),o=/[^.[\]]+|\[(?:(-?\d+(?:\.\d+)?)|(["'])((?:(?!\2)[^\\]|\\.)*?)\2)\]|(?=(?:\.|\[\])(?:\.|\[\]|$))/g,i=/\\(\\)?/g,a=n((function(t){var e=[];return 46===t.charCodeAt(0)&&e.push(""),t.replace(o,(function(t,r,n,o){e.push(n?o.replace(i,"$1"):r||t)})),e}));t.exports=a},function(t,e,r){var n=r(248);t.exports=function(t){var e=n(t,(function(t){return 500===r.size&&r.clear(),t})),r=e.cache;return e}},function(t,e,r){var n=r(79);function o(t,e){if("function"!=typeof t||null!=e&&"function"!=typeof e)throw new TypeError("Expected a function");var r=function(){var n=arguments,o=e?e.apply(this,n):n[0],i=r.cache;if(i.has(o))return i.get(o);var a=t.apply(this,n);return r.cache=i.set(o,a)||i,a};return r.cache=new(o.Cache||n),r}o.Cache=n,t.exports=o},function(t,e,r){var n=r(250);t.exports=function(t){return null==t?"":n(t)}},function(t,e,r){var n=r(50),o=r(130),i=r(17),a=r(48),c=n?n.prototype:void 0,s=c?c.toString:void 0;t.exports=function t(e){if("string"==typeof e)return e;if(i(e))return o(e,t)+"";if(a(e))return s?s.call(e):"";var r=e+"";return"0"==r&&1/e==-Infinity?"-0":r}},function(t,e,r){var n=r(252),o=r(253);t.exports=function(t,e){return null!=t&&o(t,e,n)}},function(t,e){t.exports=function(t,e){return null!=t&&e in Object(t)}},function(t,e,r){var n=r(129),o=r(82),i=r(17),a=r(83),c=r(84),s=r(62);t.exports=function(t,e,r){for(var u=-1,l=(e=n(e,t)).length,f=!1;++u<l;){var p=s(e[u]);if(!(f=null!=t&&r(t,p)))break;t=t[p]}return f||++u!=l?f:!!(l=null==t?0:t.length)&&c(l)&&a(p,l)&&(i(t)||o(t))}},function(t,e,r){var n=r(255),o=r(256),i=r(86),a=r(62);t.exports=function(t){return i(t)?n(a(t)):o(t)}},function(t,e){t.exports=function(t){return function(e){return null==e?void 0:e[t]}}},function(t,e,r){var n=r(85);t.exports=function(t){return function(e){return n(e,t)}}},function(t,e,r){var n=r(122),o=r(258);t.exports=function t(e,r,i,a,c){var s=-1,u=e.length;for(i||(i=o),c||(c=[]);++s<u;){var l=e[s];r>0&&i(l)?r>1?t(l,r-1,i,a,c):n(c,l):a||(c[c.length]=l)}return c}},function(t,e,r){var n=r(50),o=r(82),i=r(17),a=n?n.isConcatSpreadable:void 0;t.exports=function(t){return i(t)||o(t)||!!(a&&t&&t[a])}},function(t,e,r){var n=r(130),o=r(85),i=r(117),a=r(260),c=r(266),s=r(126),u=r(267),l=r(63),f=r(17);t.exports=function(t,e,r){e=e.length?n(e,(function(t){return f(t)?function(e){return o(e,1===t.length?t[0]:t)}:t})):[l];var p=-1;e=n(e,s(i));var d=a(t,(function(t,r,o){return{criteria:n(e,(function(e){return e(t)})),index:++p,value:t}}));return c(d,(function(t,e){return u(t,e,r)}))}},function(t,e,r){var n=r(261),o=r(61);t.exports=function(t,e){var r=-1,i=o(t)?Array(t.length):[];return n(t,(function(t,n,o){i[++r]=e(t,n,o)})),i}},function(t,e,r){var n=r(262),o=r(265)(n);t.exports=o},function(t,e,r){var n=r(263),o=r(81);t.exports=function(t,e){return t&&n(t,e,o)}},function(t,e,r){var n=r(264)();t.exports=n},function(t,e){t.exports=function(t){return function(e,r,n){for(var o=-1,i=Object(e),a=n(e),c=a.length;c--;){var s=a[t?c:++o];if(!1===r(i[s],s,i))break}return e}}},function(t,e,r){var n=r(61);t.exports=function(t,e){return function(r,o){if(null==r)return r;if(!n(r))return t(r,o);for(var i=r.length,a=e?i:-1,c=Object(r);(e?a--:++a<i)&&!1!==o(c[a],a,c););return r}}},function(t,e){t.exports=function(t,e){var r=t.length;for(t.sort(e);r--;)t[r]=t[r].value;return t}},function(t,e,r){var n=r(268);t.exports=function(t,e,r){for(var o=-1,i=t.criteria,a=e.criteria,c=i.length,s=r.length;++o<c;){var u=n(i[o],a[o]);if(u)return o>=s?u:u*("desc"==r[o]?-1:1)}return t.index-e.index}},function(t,e,r){var n=r(48);t.exports=function(t,e){if(t!==e){var r=void 0!==t,o=null===t,i=t==t,a=n(t),c=void 0!==e,s=null===e,u=e==e,l=n(e);if(!s&&!l&&!a&&t>e||a&&c&&u&&!s&&!l||o&&c&&u||!r&&u||!i)return 1;if(!o&&!a&&!l&&t<e||l&&r&&i&&!o&&!a||s&&r&&i||!c&&i||!u)return-1}return 0}},function(t,e,r){var n=r(63),o=r(270),i=r(272);t.exports=function(t,e){return i(o(t,e,n),t+"")}},function(t,e,r){var n=r(271),o=Math.max;t.exports=function(t,e,r){return e=o(void 0===e?t.length-1:e,0),function(){for(var i=arguments,a=-1,c=o(i.length-e,0),s=Array(c);++a<c;)s[a]=i[e+a];a=-1;for(var u=Array(e+1);++a<e;)u[a]=i[a];return u[e]=r(s),n(t,this,u)}}},function(t,e){t.exports=function(t,e,r){switch(r.length){case 0:return t.call(e);case 1:return t.call(e,r[0]);case 2:return t.call(e,r[0],r[1]);case 3:return t.call(e,r[0],r[1],r[2])}return t.apply(e,r)}},function(t,e,r){var n=r(273),o=r(276)(n);t.exports=o},function(t,e,r){var n=r(274),o=r(275),i=r(63),a=o?function(t,e){return o(t,"toString",{configurable:!0,enumerable:!1,value:n(e),writable:!0})}:i;t.exports=a},function(t,e){t.exports=function(t){return function(){return t}}},function(t,e,r){var n=r(31),o=function(){try{var t=n(Object,"defineProperty");return t({},"",{}),t}catch(t){}}();t.exports=o},function(t,e){var r=Date.now;t.exports=function(t){var e=0,n=0;return function(){var o=r(),i=16-(o-n);if(n=o,i>0){if(++e>=800)return arguments[0]}else e=0;return t.apply(void 0,arguments)}}},function(t,e,r){var n=r(77),o=r(61),i=r(83),a=r(58);t.exports=function(t,e,r){if(!a(r))return!1;var c=typeof e;return!!("number"==c?o(r)&&i(e,r.length):"string"==c&&e in r)&&n(r[e],t)}},function(t,e,r){"use strict";$(document).on("click",".catalog-item-detail__count-button_action_plus",(function(t){UserCart.onAmountButtonClick(t,1)})),$(document).on("click",".catalog-item-detail__count-button_action_minus",(function(t){UserCart.onAmountButtonClick(t,-1)})),$(document).on("input",".catalog-item-detail__count-input",(function(t){const e=parseInt(this.value);if(""!==this.value&&(isNaN(this.value)||isNaN(e)))return this.value=this.dataset.prevValue||1,t;this.value=""!==this.value?e:"",this.dataset.prevValue=this.value})),$(document).on("change",".catalog-item-detail__count-input",(function(t){let e=parseInt(this.value);const r=parseInt(this.dataset.min||this.min||1)||1,n=parseInt(this.dataset.max||this.max)||null;if(isNaN(this.value)||isNaN(e))return this.value=this.dataset.prevValue||r,t;e<r&&(e=r),null!==n&&e>n&&(e=n),this.value=e,this.dataset.prevValue=this.value;const o=this.dataset.product,i=document.querySelector(`*[data-add-url][data-product="${o}"]`),a=i.dataset.addUrl;i.dataset["amount-"+o]=this.value,i.href=`${a}?product=${o}&amount-${o}=${this.value}`}))},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,function(t,e,r){"use strict";r.r(e);var n=!1;if("undefined"!=typeof window){var o={get passive(){n=!0}};window.addEventListener("testPassive",null,o),window.removeEventListener("testPassive",null,o)}var i="undefined"!=typeof window&&window.navigator&&window.navigator.platform&&(/iP(ad|hone|od)/.test(window.navigator.platform)||"MacIntel"===window.navigator.platform&&window.navigator.maxTouchPoints>1),a=[],c=!1,s=-1,u=void 0,l=void 0,f=function(t){return a.some((function(e){return!(!e.options.allowTouchMove||!e.options.allowTouchMove(t))}))},p=function(t){var e=t||window.event;return!!f(e.target)||(e.touches.length>1||(e.preventDefault&&e.preventDefault(),!1))},d=function(){void 0!==l&&(document.body.style.paddingRight=l,l=void 0),void 0!==u&&(document.body.style.overflow=u,u=void 0)},h=function(t,e){if(t){if(!a.some((function(e){return e.targetElement===t}))){var r={targetElement:t,options:e||{}};a=[].concat(function(t){if(Array.isArray(t)){for(var e=0,r=Array(t.length);e<t.length;e++)r[e]=t[e];return r}return Array.from(t)}(a),[r]),i?(t.ontouchstart=function(t){1===t.targetTouches.length&&(s=t.targetTouches[0].clientY)},t.ontouchmove=function(e){1===e.targetTouches.length&&function(t,e){var r=t.targetTouches[0].clientY-s;!f(t.target)&&(e&&0===e.scrollTop&&r>0||function(t){return!!t&&t.scrollHeight-t.scrollTop<=t.clientHeight}(e)&&r<0?p(t):t.stopPropagation())}(e,t)},c||(document.addEventListener("touchmove",p,n?{passive:!1}:void 0),c=!0)):function(t){if(void 0===l){var e=!!t&&!0===t.reserveScrollBarGap,r=window.innerWidth-document.documentElement.clientWidth;e&&r>0&&(l=document.body.style.paddingRight,document.body.style.paddingRight=r+"px")}void 0===u&&(u=document.body.style.overflow,document.body.style.overflow="hidden")}(e)}}else console.error("disableBodyScroll unsuccessful - targetElement must be provided when calling disableBodyScroll on IOS devices.")};const v=new class{constructor(){this.$menu=$(".catalog-menu-popup"),this.timerShow=null,this.timerHide=null,this.animationEvents="webkitAnimationEnd oanimationend msAnimationEnd animationend",this.showClass="catalog-menu-popup_state_visible",this.hideClass="catalog-menu-popup_state_hidden",this.state={open:this.$menu.hasClass(this.showClass),locked:!1},this.show=this.show.bind(this),this.hide=this.hide.bind(this),this.toggle=this.toggle.bind(this)}show(){clearTimeout(this.timerHide),clearTimeout(this.timerShow),this.state.locked=!0,h(document.querySelector(".catalog-menu-popup")),this.$menu.css({height:$(window).height()-$(".header__wrapper").height()}).scrollTop(0),this.$menu.hasClass(this.showClass)&&this.$menu.hasClass(this.hideClass)&&this.$menu.removeClass([this.hideClass,this.showClass].join(" ")).off(this.animationEvents),this.timerShow=setTimeout(()=>{this.$menu.addClass(this.showClass),this.state.open=!0,this.state.locked=!1},0)}hide(t=200){clearTimeout(this.timerHide),clearTimeout(this.timerShow),this.state.locked=!0,this.state.open&&(this.timerHide=setTimeout(()=>{this.$menu.addClass(this.hideClass).on(this.animationEvents,()=>{var t;(t=document.querySelector(".catalog-menu-popup"))?(a=a.filter((function(e){return e.targetElement!==t})),i?(t.ontouchstart=null,t.ontouchmove=null,c&&0===a.length&&(document.removeEventListener("touchmove",p,n?{passive:!1}:void 0),c=!1)):a.length||d()):console.error("enableBodyScroll unsuccessful - targetElement must be provided when calling enableBodyScroll on IOS devices."),this.$menu.removeClass([this.hideClass,this.showClass].join(" ")).removeAttr("style").off(this.animationEvents),this.state.open=!1,this.state.locked=!1})},t))}toggle(){if(this.state.locked)return!1;this.state.open?this.hide():this.show()}},m=$(".catalog-menu__item_type_popup"),g=$(".catalog-group__close");m.length&&(m.on("mouseenter",()=>v.show()).on("mouseleave",()=>v.hide()),g.on("click",()=>v.hide(0)),v.$menu.on("mouseenter",()=>{clearTimeout(v.timerHide),v.state.locked=!1}).on("mouseleave",()=>v.hide()));const _=$(".header__catalog");_.length&&_.on("click",()=>v.toggle())}]);