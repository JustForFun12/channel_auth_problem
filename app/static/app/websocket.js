var path = window.location.pathname;
path = path.split('/');
room = path[path.length - 1];

if (room == "") {
    room = 'anonymous'
}

// ================== CREATING A WEB SOCKET ====================
// Note: it is said that a good practice is to great websocket in the end

// ws = new WebSocket('ws://127.0.0.1:8000/ws/wsc/')
ws = new WebSocket(`ws://127.0.0.1:8000/ws/wsc/${room}`)



ws.onopen = function() {
    console.log('we are connected')
    // ws.send('hello G')
}

ws.onmessage = function(event) {
    console.log('message received')
    console.log(event);

    msg = event['data'] + '\n'
    $('#display_board').append(msg);

}

ws.onclose = function(event) {
    console.log('connection closed')
}





//  ============== SENDING DATA WHEN SUBMIT TO FORM ===========
$('#post-form').on('submit', function(event) {
    event.preventDefault();
    
    let val = $('#msg').val();
    ws.send(val);
    $('#msg').val('');        // resetting inbox
    $('#msg').focus();        // focusing back of input box
});




























// ====================== HANDLING THE CSRF_TOKEN HERE ========================================

$(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});
