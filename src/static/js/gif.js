/**
 * setup JQuery's AJAX methods to setup CSRF token in the request before sending it off.
 * http://stackoverflow.com/questions/5100539/django-csrf-check-failing-with-an-ajax-post-request
 */
// CONFIG
const GIFS_ENDPOINT = '/api/gif/';
const GIFS_FORMULAR = $("#gif-form");

let gifs_source = document.getElementById("gifs-template").innerHTML;
let gifs_template = Handlebars.compile(gifs_source);

/* jshint esversion: 6 */

/**
 * Cookie setting for django
 *
 * @param name  cookie name
 * @returns {*}
 */
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            let cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

GIFS_FORMULAR.submit(function (event) {
    event.preventDefault();
    var url = GIFS_FORMULAR.attr('action');
    $.ajax({
        url: url,
        type: 'post',
        dataType: 'json',
        data: GIFS_FORMULAR.serialize(),
        success: gifSuccessProcess,
        error: displayErrorModal,
    })
});

function clearGIFFormular() {
    GIFS_FORMULAR[0].reset();
}

function gifSuccessProcess(data) {
    updateGifs();
    displaySuccessModal(data);
    clearGIFFormular();
}

ready(function () {
    console.log("Ready");
    updateGifs();
});

function updateGifs() {
    $.ajax({
        url: GIFS_ENDPOINT,
        type: 'get',
        dataType: 'json',
        success: resetGifs,
        error: displayErrorModal,
    })
}

function resetGifs(data) {
    let gifs = $('#gifs-wrapper');
    let html = '';
    for (const context of data) {
        html += gifs_template(context);
    }
    gifs.empty();
    gifs.append(html)
}

function confirm_gif_delete() {
    return confirm("Möchtest du das GIF wirklich löschen?");
}

function resetGifAndDisplaySuccess() {
    updateGifs();
    displaySuccessModal();
}


function deleteGif(url) {
    const is_confirmed = confirm_gif_delete();
    if (is_confirmed) {
        console.log(url);
        $.ajax({
            url: url,
            type: 'delete',
            dataType: 'json',
            data: {},
            success: resetGifAndDisplaySuccess,
            error: displayErrorModal,
        })
    }
}
