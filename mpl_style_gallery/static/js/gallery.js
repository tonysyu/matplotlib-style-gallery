/*jslint browser:true */
/*global $, jQuery, alert*/

(function mplStyleGallery() {
    'use strict';

    var ESCAPE_KEY = 27;

    $(document).ready(function () {

        var $lightbox = $('#lightbox');

        // Click on any lightbox-viewable to open lightbox window.
        $('a.lightbox-viewable').click(function (event) {

            // Prevent default (hyperlink) action
            event.preventDefault();

            // Get clicked link target
            var image_href = $(this).attr("href");

            $('#content img').attr('src', image_href);
            $lightbox.show();

        });

        // Press ESCAPE to hide the lightbox window.
        $(document).keyup(function (event) {
            if (event.keyCode == ESCAPE_KEY) {
                $lightbox.hide();
            }
        });

    });
}());
