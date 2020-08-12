/* eslint-disable */

(function ($) {
  'use strict';

  window.chainedfk = function () {
    return {
      fireEvent: function (element, event) {
        var rtn;
        if (document.createEventObject) {
          // dispatch for IE
          var evt = document.createEventObject();
          rtn = element.fireEvent('on' + event, evt);
        } else {
          // dispatch for firefox + others
          var evt = document.createEvent('HTMLEvents');
          evt.initEvent(event, true, true); // event type,bubbling,cancelable
          rtn = !element.dispatchEvent(evt);
        }

        return rtn;
      },

      init: function (chainfieldId, url, id, init_value, empty_label, auto_choose) {
        var $chainfield = $(chainfieldId);


        if (!$chainfield.hasClass('chained')) {
          var val = $chainfield.val();
          this.fill_field(val, init_value, id, url, empty_label, auto_choose);
        }

        $chainfield.change(function (event) {
          var fieldForFilled = document.querySelector(
            '*[data-chainfield="{name}"]'.replace('{name}', this.name)
          );

          if (fieldForFilled) {
            var elem_id = '#' + fieldForFilled.id;
            var start_value = fieldForFilled.value;
            var this_val = this.value;
            chainedfk.fill_field(this_val, start_value, elem_id, url, empty_label, auto_choose);
          }
        });

        if (typeof(dismissAddAnotherPopup) !== 'undefined') {
          var oldDismissAddAnotherPopup = dismissAddAnotherPopup;
          dismissAddAnotherPopup = function (win, newId, newRepr) {
            oldDismissAddAnotherPopup(win, newId, newRepr);
            if (windowname_to_id(win.name) === chainfieldId) {
              $(chainfieldId).change();
            }
          }
        }
      },

      dismissRelatedLookupPopup: function (win, chosenId) {
        var name = windowname_to_id(win.name);
        var elem = document.getElementById(name);

        if (elem.className.indexOf('vManyToManyRawIdAdminField') !== -1 && elem.value) {
          elem.value += ',' + chosenId;
        } else {
          elem.value = chosenId;
        }
        fireEvent(elem, 'change');
        win.close();
      },

      fill_field: function (val, init_value, elem_id, url, empty_label, auto_choose) {
        var $selectField = $(elem_id);
        var options = [];

        url = url + '/' + val + '/';

        var emptyOption =  document.createElement('option');
        emptyOption.value = '';
        emptyOption.innerHTML = empty_label;

        if (!val || val === '') {
          emptyOption.selected = true;
          $selectField.html(emptyOption);
          return;
        }

        $.getJSON(url, function (j) {
          auto_choose = j.length === 1 && auto_choose;

          if (auto_choose === 'true' || auto_choose === 'True') {
            auto_choose = true;
          } else if (auto_choose === 'false' || auto_choose === 'False') {
            auto_choose = false;
          }

          // Append empty label as the first option
          if (!(init_value || auto_choose)) {
            emptyOption.selected = true;
          }

          options.push(emptyOption);

          // Append each option to the select
          $.each(j, function (index, optionData) {
            var option = document.createElement('option');
            option.value = optionData.value;
            option.innerHTML = optionData.display;

            if (auto_choose || (init_value && optionData.value === init_value)) {
              option.selected = true;
            }

            options.push(option);
          });

          $selectField.html(options);
          if (init_value) {
            $selectField.val(init_value);
          }

          var width = $selectField.outerWidth();
          if (navigator.appVersion.indexOf('MSIE') !== -1) {
            $selectField.width(width + 'px');
          }
        });
      }
    }
  }();
}(jQuery || django.jQuery));
