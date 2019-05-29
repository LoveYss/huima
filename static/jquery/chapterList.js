$(function () {
    $('.add-list').on('click', function () {
        // var obj = $(this).parent().next().next();
        var obj = $(this).parent().next();
        // obj.css({'display':'block'});
        obj.show();
    });
    var divInner = $('#cha-scrollBar-list');
    var num = 0, flag = true;
    var warpWidth = parseInt($('.cha-scrollBar').css('width'));

    $('#l-sec-btnLeft').on('click', function () {
        if (flag) {
            num -= 174;
            if ((divInner.children().length-1)*174+parseInt(divInner.css('marginLeft'))-parseInt(divInner.css('width'))<0) {
                num += 174;
                return;
            }
            flag = false;
            divInner.animate({
                marginLeft: num + 'px'
            }, function () {
                flag = true
            })
        }
    });
    $('#l-sec-btnRight').on('click', function () {
        if (flag) {
            num += 174;
            if (num === 174) {
                num -= 174;

                return;
            }
            flag = false;
            divInner.animate({
                marginLeft: num + 'px'
            }, function () {
                flag = true
            })
        }
    });
});