$("#quote-form").submit(function (event) {
    event.preventDefault();
    var form = $('#quote-form');
    var url = form.attr('action');
    $.post(url, form.serialize(), function (data) {
            console.log(data);
        },
        'json' // I expect a JSON response
    );
});

$("#author-form").submit(function (event) {
    event.preventDefault();
    var form = $('#author-form');
    var url = form.attr('action');
    console.log(url);
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
    console.log('SUCCESS');
    console.log(data);
    $("#successGif").attr("src", data.url)
}

function displayErrorModal(data) {
    $('#failModal').modal();
    console.log('FAIL');
    console.log(data.responseJSON);
    $("#failGif").attr("src", data.responseJSON.url)
}