$(function () {
    $('.register').width(innerWidth)

    $('#account input').blur(function () {
        var reg = /^[A-Za-z0-9]+$/
        if (reg.test($(this).val())) {
            $('#account i').html('')
            $('#account').removeClass('has-error')
                .addClass('has-success')
            $('#account span').removeClass('glyphicon-remove')
                .addClass('glyphicon-ok')
        }else {
            $('#account i').html('账号由数字，字母下划线组成')
            $('#account').removeClass('has-success')
                .addClass('has-error')
            $('#account span').removeClass('glyphicon-ok')
                .addClass('glyphicon-remove')
        }
    })
})