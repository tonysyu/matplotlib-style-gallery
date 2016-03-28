/*jslint browser:true */
/*global $, Spinner*/

(function mplStyleGallery() {
    'use strict';

    /**
     * Create simple lightbox for viewing images.
     *
     * @param {JQuery} Target lightbox div containing single `img` element.
     */
    function createLightbox($el) {
        var SELECTED = null,
            KEY_ESCAPE = 27,
            KEY_LEFT_ARROW = 37,
            KEY_UP_ARROW = 38,
            KEY_RIGHT_ARROW = 39,
            KEY_DOWN_ARROW = 40,
            ARROW_KEYS = [KEY_LEFT_ARROW, KEY_UP_ARROW,
                          KEY_RIGHT_ARROW, KEY_DOWN_ARROW];

        function getElementAtIndex(iRow, iCol) {
            return $("[data-icol='" + iCol + "'][data-irow='" + iRow + "']");
        }

        function isArrowKey(keyCode) {
            return ARROW_KEYS.indexOf(keyCode) !== -1;
        }

        function displayImage($elImage) {
            SELECTED = {
                iCol: parseInt($elImage.attr('data-icol'), 10),
                iRow: parseInt($elImage.attr('data-irow'), 10),
            };

            // Update displayed plot info.
            $('#plot-script').text($elImage.attr('data-script'));
            $('#plot-style').text($elImage.attr('data-style'));

            // Update displayed image.
            $el.children('img').attr('src', $elImage.attr('href'));
        }

        function incrementAndWrap(value, increment, max) {
            var newValue = (value + increment) % max;
            if (newValue < 0) {
                newValue += max;
            }
            return newValue;
        }

        // Update lightbox impage based on arrow-keys.
        function updateLightboxImage(keyCode) {
            // Subtract 1 to remove header row and column.
            var table = document.getElementById("gallery"),
                nRows = table.rows.length - 1,
                nCols = table.rows[0].cells.length - 1;

            if (keyCode === KEY_LEFT_ARROW) {
                SELECTED.iCol = incrementAndWrap(SELECTED.iCol, -1, nCols);
            } else if (keyCode === KEY_RIGHT_ARROW) {
                SELECTED.iCol = incrementAndWrap(SELECTED.iCol, 1, nCols);
            }else  if (keyCode === KEY_DOWN_ARROW) {
                SELECTED.iRow = incrementAndWrap(SELECTED.iRow, 1, nRows);
            } else if (keyCode === KEY_UP_ARROW) {
                SELECTED.iRow = incrementAndWrap(SELECTED.iRow, -1, nRows);
            }

            var $elImage = getElementAtIndex(SELECTED.iRow, SELECTED.iCol);
            displayImage($elImage);
        }

        $(document).keydown(function (event) {
            if (SELECTED !== null && isArrowKey(event.keyCode)) {
                event.preventDefault(); // Prevent default (scroll) action
            }
        });

        $(document).keyup(function (event) {
            // Press ESCAPE to hide the lightbox window.
            if (event.keyCode === KEY_ESCAPE) {
                SELECTED = null;
                $el.hide();
            } else if (SELECTED !== null && isArrowKey(event.keyCode)) {
                updateLightboxImage(event.keyCode);
            }
        });

        // The public interface for lighbox.
        var lightboxFacade = {

            // Replace anchor targets with lightbox display.
            display : function (event) {

                // Prevent default (hyperlink) action
                event.preventDefault();
                displayImage($(this));
                $el.show();
            }
        };
        return lightboxFacade;
    }

    $(document).ready(function () {
        var lightbox = createLightbox($('#lightbox'));

        // Stylesheet input fires spinner since there's a noticeable delay.
        $('input').click(function (event) {
            $(this).after(new Spinner({}).spin().el);
        });

        // Click on any lightbox-viewable to open lightbox window.
        $('a.lightbox-viewable').click(lightbox.display);

    });
}());
