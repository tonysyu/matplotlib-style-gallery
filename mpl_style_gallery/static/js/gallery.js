/*jslint browser:true */
/*global $, jQuery, alert*/

function mplStyleGallery(table) {
    'use strict';

    var ESCAPE_KEY = 27,
        imageDatabase = {};

    $(document).ready(function () {
        // Replace anchor targets with lighbox display

        var $lightbox = $('#lightbox');

        // Click on any lightbox-viewable to open lightbox window.
        $('a.lightbox-viewable').click(function (event) {

            var imageHref = $(this).attr('href');  // clicked link target

            // Prevent default (hyperlink) action
            event.preventDefault();

            // Set lightbox image source to the clicked image.
            $('#content img').attr('src', imageHref);

            $lightbox.show();

        });

        // Press ESCAPE to hide the lightbox window.
        $(document).keyup(function (event) {
            if (event.keyCode == ESCAPE_KEY) {
                $lightbox.hide();
            }
        });

    });
};
