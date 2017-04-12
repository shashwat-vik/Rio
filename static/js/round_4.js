var submit_count=0;
var times = 1
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
        bar.stop();
        $('.my_tick')[0].pause();
    });
    $('.box-icon').on('click', function () {
        if (!timer_started) {
            $('.box-icon .header_element').html('')
            $('#timer.timer_container').removeAttr('hidden')
            bar.text.style.fontFamily = '"Raleway", Helvetica, sans-serif';
            bar.text.style.fontSize = '2rem';
            bar.animate(1.0, {}, function() {
                $('#tModal').modal('show');
                $('.my_tick')[0].pause();
            });
            timer_started = true;
            $('.my_tick')[0].play();
        }
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

var timer_started = false;
var bar = new ProgressBar.Circle(timer, {
  color: '#fff',

  strokeWidth: 4,
  text: {
    autoStyleContainer: false
  },
  duration: 10000,
  // Set default step function for all animate calls
  step: function(state, circle) {
    var value = Math.round(circle.value() * 10);
    if (value === 0) {
      circle.setText('');
    } else {
      circle.setText(value);
    }
  }
});
