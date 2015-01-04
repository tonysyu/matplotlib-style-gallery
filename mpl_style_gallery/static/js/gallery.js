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
        var ESCAPE_KEY = 27,
            lightboxFacade;

        // Press ESCAPE to hide the lightbox window.
        $(document).keyup(function (event) {
            if (event.keyCode === ESCAPE_KEY) {
                $el.hide();
            }
        });

        // The public interface for lighbox.
        lightboxFacade = {

            // Replace anchor targets with lightbox display.
            display : function (event) {

                var imageHref = $(this).attr('href');  // clicked link target

                // Prevent default (hyperlink) action
                event.preventDefault();

                // Set lightbox image source to the clicked image.
                $el.children('img').attr('src', imageHref);

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
