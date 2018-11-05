$("#quote-form").submit(function (event) {
    event.preventDefault();
    var form = $('#quote-form')
    var url = form.attr('action');
    console.log(url);
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
        dataType: 'html',
        data: form.serialize(),
        success: displaySuccessModal,
        error: displayErrorModal,
    })
});

function displaySuccessModal() {
    $('#successModal').modal();
    console.log('SUCCESS');
}

function displayErrorModal() {
    $('#failModal').modal();
    console.log('FAIL');
}