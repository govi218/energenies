$(document).ready(function() {

    $('.update-btn').on('click', function() {
        console.log("updating")
        const device_id = $(this).attr('device_id');
        const name = $('#nameInput-' + device_id).val()
        const usage = $('#usageInput-' + device_id).val()

        req = $.ajax({
            url: '/update',
            type: 'POST',
            dataType: 'json',
            data: { id:device_id, name:name, usage:usage}
        });

        $('#device-section-' + device_id).fadeOut(250).fadeIn(250);

    });

    $('.delete-btn').on('click', function() {
        const device_id = $(this).attr('device_id');

        req = $.ajax({
            url: '/delete',
            type: 'POST',
            dataType: 'json',
            data: { id:device_id},
            succes: function(response) {
                if (response.redirect) {
                    window.location.href = response.redirect;
                }
            }
        }).done(function(response) {
            if (response.redirect) {
                window.location.href = response.redirect;
            }
        });

        $('#device-section-' + device_id).fadeOut(250).fadeIn(250);

    });


});