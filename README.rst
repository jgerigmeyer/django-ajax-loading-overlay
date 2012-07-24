jQuery Ajax Loading Overlay plugin package for Django
=====================================================

django-ajax-loading-overy uses Javascript to add/remove a loading overlay to a target element during Ajax calls. It can be called on any element that should receive the loading overlay, and accepts options for class selectors and loading overlay text.

Dependencies
------------

- jQuery library (http://jquery.com/)

Installation
------------

In your Django project settings, add "ajax_loading_overlay" to your INSTALLED_APPS.

Usage
-----

Linking the JS::

    <script src="{{ STATIC_URL }}ajax_loading_overlay/jquery.ajax-loading-overlay.js"></script>

Calling the plugin::

    $('#target').loadingOverlay();

Removing the loading overlay (usually upon success of the Ajax call)::

    $('#target').loadingOverlay('remove');

Options can be passed to override the default loading class ('loading'), overlay class ('overlay'), loading text('loading...'), and/or function to return loading text padding-top::

    $('#target').loadingOverlay({
        loadingClass: 'myLoadingClass',
        overlayClass: 'myOverlayClass',
        loadingText: 'Loading. Please Wait.',
        paddingTop: function (target) {
            return ((target.outerHeight() - parseInt(target.css('line-height'), 10)) / 2).toString() + 'px';
        }
    });

If `loadingClass` or `overlayClass` options are passed when initializing the loading overlay, the same options must be passed when removing that overlay::

    $('#target').loadingOverlay('remove', {
        loadingClass: 'myLoadingClass',
        overlayClass: 'myOverlayClass'
    });