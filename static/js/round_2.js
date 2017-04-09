$(document).ready(function () {
    $('.que_options .option').on('click', function () {
        for(var i=1; i<=4; ++i) {
            $('.que_options #'+String(i)+'.option').removeClass('selected');
            $('.que_options #'+String(i)+'.option').removeClass('border_effect');
        }
        $(this).toggleClass('selected');
        $(this).toggleClass('border_effect');
    });
});
