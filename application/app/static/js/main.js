$(document).ready(function() {

    // Update a device
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

    // Delete a device
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
    });


    // display additional device info
    $('.info-btn').on('click', function() {
        const device_id = $(this).attr('device_id');
        var infoSection = document.getElementById("device-info-" + device_id)
        if (infoSection.style.display == 'none') {
            infoSection.style.display = 'inline';
        } else {
            infoSection.style.display = 'none'
        }     
    });



});