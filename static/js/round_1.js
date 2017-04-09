var submit_count=0;
var times = 8
$(document).ready(function(e) {
    $("#submit.click_option").click(function() {
        submit_count += 1;
        if (submit_count <= times) {
            check_answer();
            $('.tries_left h4').html('<b>'+String(times-submit_count)+'</b>');
        }
         else if (submit_count == (times+1)){
             $('#submit.click_option').attr('data-target','#aModal');
        };
    });
});

var check_answer = function () {
    submission = $('.answer_box #myInput').val()
    true_answer = $('#1.1994').attr("secanswer")
    submission = clean_data(submission)
    true_answer = clean_data(true_answer)
    if (submission == true_answer) {
        $('#submit.click_option').attr('data-target','#cModal');
    } else {
        $('#submit.click_option').attr('data-target','#wModal');
    }
};

var clean_data = function(data) {
    c_data = ""
    data = data.toLowerCase()
    for(var i=0; i<data.length; ++i) {
        code = data.charCodeAt(i);
        if((code >= 48 && code <= 57) || (code >= 97 && code <= 122))
            c_data += data[i];
    }
    return c_data;
};
