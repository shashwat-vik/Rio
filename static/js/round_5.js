var que_idx = 1;
$(document).ready(function () {
    for(var i=1; i<=5; ++i)
        que_caretaker(i);
    $('.glyphicon-plus-sign').on('click', function () {
        if (que_idx <= 5) {
            $('#'+String(que_idx)+'.rapid_fire').removeClass('hidden');
        }
        que_idx += 1
    });

    $('.box-icon').on('click', function () {
        if (!timer_started) {
            $('#timer.timer_container').removeAttr('hidden')
            bar.text.style.fontFamily = '"Raleway", Helvetica, sans-serif';
            bar.text.style.fontSize = '2rem';
            bar.animate(1.0, {}, function() {
                $('#tModal').modal('show');
                $('.my_tick')[0].pause();
            });
            timer_started = true;
            $('.glyphicon-plus-sign').click();
            $('.my_tick')[0].play();
        }
    });
});

var que_caretaker = function(q) {
    var que = String(q);
    $('#'+q+'.rapid_fire .option').on('click', function() { create_answer_highlighter(q); });
    $('#'+q+'.rapid_fire #1.option').on('click', function() { create_option_highlighter(q, 1); });
    $('#'+q+'.rapid_fire #2.option').on('click', function() { create_option_highlighter(q, 2); });
};

var create_option_highlighter = function(q, o) {
    var que = String(q);
    var opt = String(o);
    var answer = $('#'+que+'.rapid_fire .1994').attr('secanswer');
    if (answer == opt) {
        $('#'+que+'.rapid_fire #'+ opt +'.option').css('background','#33CC00');
        $('#'+que+'.rapid_fire #'+ opt +'.option').css('color','white');
    } else {
        $('#'+que+'.rapid_fire #'+ opt +'.option').css('background','#CC0000');
        $('#'+que+'.rapid_fire #'+ opt +'.option').css('color','white');
    }
};
var create_answer_highlighter = function(q) {
    var que = String(q);
    var answer = $('#'+q+'.rapid_fire .1994').attr('secanswer');
    $('#'+q+'.rapid_fire #'+ answer +'.option').css('background','#33CC00');
    $('#'+q+'.rapid_fire #'+ answer +'.option').css('color','white');
};


var timer_started = false;
var bar = new ProgressBar.Circle(timer, {
  color: '#fff',

  strokeWidth: 4,
  text: {
    autoStyleContainer: false
  },
  duration: 30000,
  // Set default step function for all animate calls
  step: function(state, circle) {
    var value = Math.round(circle.value() * 30);
    if (value === 0) {
      circle.setText('');
    } else {
      circle.setText(value);
    }
  }
});
