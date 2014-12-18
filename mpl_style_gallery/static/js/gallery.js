/*jslint browser:true */
/*global $, jQuery, alert*/

function mplStyleGallery(table) {
    'use strict';

    var ESCAPE_KEY = 27,
        imageDatabase = {};

    function createImageDatabase(table) {
        // Transform gallery table to an image database
        //
        // The image database returns image urls when indexed as:
        //
        //    imageDatabase[<style-name>][<type-name>]

        var row = [],
            style = '',
            row = [],
            cell = {},
            imageDatabase = {};

        for (var iRow = 0; iRow < table.length; iRow++) {
            style = table[iRow][0];
            row = table[iRow][1];

            imageDatabase[style] = {}
            for (var iCell = 0; iCell < row.length; iCell++) {
                cell = row[iCell];
                imageDatabase[style][cell.type] = cell.url;
            }
        }

        return imageDatabase;
    }

    imageDatabase = createImageDatabase(table)

    $(document).ready(function () {
        // Replace anchor targets with lighbox display

        var $lightbox = $('#lightbox');

        // Click on any lightbox-viewable to open lightbox window.
        $('a.lightbox-viewable').click(function (event) {

            var $anchor = $(this),                  // clicked anchor
                imageHref = $anchor.attr('href'),  // clicked link target
                imageUrls = {},
                $thumbnailDiv = $('#lightbox-thumbnails'),
                clickedImg = $anchor.children('img')[0],
                style = clickedImg.getAttribute('data-style');

            // Prevent default (hyperlink) action
            event.preventDefault();

            // Set lightbox image source to the clicked image.
            $('#content img').attr('src', imageHref);

            // All image URLs for the selected style.
            imageUrls = imageDatabase[style]

            for (var type in imageUrls) {
                console.log(imageUrls[type])
            }

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
