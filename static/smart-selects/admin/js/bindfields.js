/* eslint-disable */

(function ($) {
  'use strict';

  function initItem(item) {
    var chainfield = '#id_' + item.dataset.chainfield;
    var url = item.dataset.url;
    var id = '#' + item.id;
    var value = JSON.parse(item.dataset.value);
    var auto_choose = item.dataset.auto_choose;

    if (item.classList.contains('chained-fk')) {
      var empty_label = item.dataset.empty_label;
      chainedfk.init(chainfield, url, id, value, empty_label, auto_choose);
    } else if (item.classList.contains('chained')) {
      chainedm2m.init(chainfield, url, id, value, auto_choose);
    } else if (item.classList.contains('filtered')) {
      // For the ManyToMany using horizontal=True added after the page load
      // using javascript.
      id = id.replace('_from', ''); // we need to remove the _from part
      chainedm2m.init(chainfield, url, id, value, auto_choose);
    }
  }

  $(window).on('load', function () {
    $('.chained').each(function (index, item) {
      initItem(item);
    });
  });

  $(document).ready(function () {
    $('.chained-fk').each(function (index, item) {
      initItem(item);
    });
  });

  function initFormset(chained) {
    var baseChainfield = chained.dataset.chainfield;

    if (baseChainfield.indexOf('__prefix__') + 1) {
      // If we have several inlines with the same name, they will get an index,
      // so we need to ignore that and get the last numeric value in the id
      var re = /\d+/g;
      var prefix;
      var match;
      while ((match = re.exec(chained.id)) !== null) {
        prefix = match[0];
      }
      chained.dataset.chainfield = baseChainfield.replace('__prefix__', prefix);
    }

    if (baseChainfield.indexOf('-empty-') + 1) {
      var re = /\d+/ig;
      var match = re.exec(chained.id);
      if (match) {
        chained.dataset.chainfield = baseChainfield.replace('empty', match[0]);
      }
    }

    initItem(chained);
  }

  $(document).on('formset:added', function (event, $row, formsetName) {
    // Fired every time a new inline formset is created

    // For the ForeingKey
    var $chainedFK = $row.find('.chained-fk');
    $chainedFK.each(function (index, chained) {
      initFormset(chained);
    });

    // For the ManyToMany
    var $chainedM2M = $row.find('.chained');
    $chainedM2M.each(function (index, chained) {
      initFormset(chained);
    });

    // For the ManyToMany using horizontal=True added after the page load
    // using javascript.
    var $filteredM2M = $row.find('.filtered');
    $filteredM2M.each(function (index, filtered) {
      if (filtered.hasAttribute('data-chainfield')) {
        initFormset(filtered);
      }
    });
  });
}(jQuery || django.jQuery));
