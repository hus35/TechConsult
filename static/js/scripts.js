$(document).ready(function() {
    $('#contactForm').submit(function(e) {
        e.preventDefault();
        $.ajax({
            url: '/contact',
            type: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                $('#response').html('<div class="alert alert-success">' + response.message + '</div>');
                $('#contactForm')[0].reset();
            },
            error: function() {
                $('#response').html('<div class="alert alert-danger">حدث خطأ، حاول مرة أخرى.</div>');
            }
        });
    });
});
