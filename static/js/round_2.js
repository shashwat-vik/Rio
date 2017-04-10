var lock_control = false;
$(document).ready(function () {
    $('.que_options .option').on('click', function () {
        if (!lock_control) {
            for(var i=1; i<=4; ++i) {
                $('.que_options #'+String(i)+'.option').removeClass('selected');
                $('.que_options #'+String(i)+'.option').removeClass('border_effect');
            }
            $(this).toggleClass('selected');
            $(this).toggleClass('border_effect');
        };
    });
    $('.lock').on('click', function () {
        var selected = null;
        for(var i=1; i<=4; ++i) {
            if ($('.que_options #'+String(i)+'.option').hasClass('selected')) {
                selected = i;
            }
            $('.que_options #'+String(i)+'.option').removeClass('selected');
            $('.que_options #'+String(i)+'.option').removeClass('border_effect');
        }
        answer = $('#1.1994').attr("secanswer")
        if (selected != answer*1) {
            $('.que_options #'+ String(selected) +'.option').css('background','#CC0000');
            $('.que_options #'+ String(selected) +'.option').css('color','white');
        }
        $('.que_options #'+ answer +'.option').css('background','#33CC00');
        $('.que_options #'+ answer +'.option').css('color','white');
        lock_control = true;
        bar.stop();
    });
    $('.box-icon').on('click', function () {
        if (!timer_started) {
            $('.box-icon .header_element').html('')
            $('#timer.timer_container').removeAttr('hidden')
            bar.text.style.fontFamily = '"Raleway", Helvetica, sans-serif';
            bar.text.style.fontSize = '2rem';
            bar.animate(1.0, {}, function() {
                $('#tModal').modal('show');
            });
            timer_started = true;
        }
    });
});

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
