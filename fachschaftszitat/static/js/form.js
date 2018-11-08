/**
 * setup JQuery's AJAX methods to setup CSRF token in the request before sending it off.
 * http://stackoverflow.com/questions/5100539/django-csrf-check-failing-with-an-ajax-post-request
 */

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
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

$("#quote-form").submit(function (event) {
    event.preventDefault();
    var form = $('#quote-form');
    var url = form.attr('action');
    $.ajax({
        url: url,
        type: 'post',
        dataType: 'json',
        data: form.serialize(),
        success: displaySuccessModal,
        error: displayErrorModal,
    })
});
$("#author-form").submit(function (event) {
    event.preventDefault();
    var form = $('#author-form');
    var url = form.attr('action');
    $.ajax({
        url: url,
        type: 'post',
        dataType: 'json',
        data: form.serialize(),
        success: displaySuccessModal,
        error: displayErrorModal,
    })
});

function updateQuotes() {
    var url = '/api/quote';
    $.ajax({
        url: url,
        type: 'get',
        dataType: 'json',
        success: resetAuthorOptions,
        error: displayErrorModal,
    })
}

function updateAuthors() {
    var url = '/api/author';
    $.ajax({
        url: url,
        type: 'get',
        dataType: 'json',
        success: resetAuthorOptions,
        error: displayErrorModal,
    })
}

function resetAuthorOptions(data) {
    let options = '<option value="" selected>---------</option>';
    console.log(data);
    for (var author of data) {
        options += '<option value="' + author.id + '">' + author.name + '</option>';
    }
    console.log(options);
    $('.author-select-box').each(function (index) {
        console.log($(this).val());
        var selected = $(this).val();
        $(this).empty().append(options);
        $(this).val(selected);
    })
}

function displaySuccessModal(data) {
    updateAuthors();
    $('#successModal').modal();
    $("#successGif").attr("src", data.url)
}

function displayErrorModal(data) {
    $('#failModal').modal();
    $("#failGif").attr("src", data.responseJSON.url)
}