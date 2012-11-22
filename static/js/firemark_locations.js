function showCurrentLocation(data) {
    var mainContent = $('#MainContent');
    mainContent.removeClass();
    if (data.errno > 0) {
        mainContent.addClass('error');
        mainContent.html('<h2 class="title">Error ' + data.errno + '</h2>');
        mainContent.append('<p>' + data.error + '</p>');
        $('#ActionIndicator').html('Error loading current location...');
        $(document).bind('click', function() {
            $('#ActionIndicator').unbind('click');
            $('#ActionIndicator').fadeOut();
        });
        return;
    }
    mainContent.addClass('location current_location');
    mainContent.html('<h2 class="title">' + data.name + '</h2>');
    mainContent.append('<div class="bricks"></div>');
    var bricks = $('#MainContent .bricks');
    data.bricks.each(function(brick) {
        switch (brick.type) {
            case 'exit':
                bricks.append('<div class="brick exit" onclick="exitCurrentLocation(' + brick.content + ')">EXIT ' + brick.content + '</div>');
                break;
            case 'image':
                bricks.append('<img src="' + brick.content + '" class="brick img" alt=""/>');
                break;
            case 'text':
                bricks.append('<div class="brick text">' + brick.content + '</div>');
                break;
            default:
                console.log('Unknown brick type.');
        }
    });
    $('#ActionIndicator').fadeOut();
}
function exitCurrentLocation(exit) {
    $('#ActionIndicator').html('Changing location...');
    $('#ActionIndicator').fadeIn();
    $.post('getLocation.php', { "exit": exit }, function(data) {
        $('#ActionIndicator').stop();
        $('#ActionIndicator').fadeOut();
        showCurrentLocation(JSON.parse(data));
    });
}

