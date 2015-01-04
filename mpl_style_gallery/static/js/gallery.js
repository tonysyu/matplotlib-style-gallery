/*jslint browser:true */
/*global $, Spinner*/

(function mplStyleGallery() {
    'use strict';

    function createLightbox($el) {
        var ESCAPE_KEY = 27,
            lightboxFacade;

        // Press ESCAPE to hide the lightbox window.
        $(document).keyup(function (event) {
            if (event.keyCode === ESCAPE_KEY) {
                $el.hide();
            }
        });

        lightboxFacade = {
            display : function (event) {
                // Replace anchor targets with lightbox display

                var imageHref = $(this).attr('href');  // clicked link target

                // Prevent default (hyperlink) action
                event.preventDefault();

                // Set lightbox image source to the clicked image.
                $('#lightbox img').attr('src', imageHref);

                $el.show();
            }
        };
        return lightboxFacade;
    }

    $(document).ready(function () {

        var lightbox = createLightbox($('#lightbox'));

        $('input').click(function (event) {
            $(this).after(new Spinner({}).spin().el);
        });

        // click on any lightbox-viewable to open lightbox window.
        $('a.lightbox-viewable').click(lightbox.display);

    });
}());
