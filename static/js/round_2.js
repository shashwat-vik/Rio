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
            $('.que_options #'+ String(selected) +'.option').css('background','red');
            $('.que_options #'+ String(selected) +'.option').css('color','white');
        }
        $('.que_options #'+ answer +'.option').css('background','green');
        $('.que_options #'+ answer +'.option').css('color','white');
        lock_control = true;
    });
});
