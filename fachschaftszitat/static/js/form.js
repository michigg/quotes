$("#quote-form").submit(function (event) {
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

function displaySuccessModal(data) {
    $('#successModal').modal();
    $("#successGif").attr("src", data.url)
}

function displayErrorModal(data) {
    $('#failModal').modal();
    $("#failGif").attr("src", data.responseJSON.url)
}