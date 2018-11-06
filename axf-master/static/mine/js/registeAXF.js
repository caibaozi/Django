$(function () {
    $('.register').width(innerWidth)

    $('#account input').blur(function () {
        if ($(this).val() == '')return

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




    $('#password input').blur(function () {
        if ($(this).val() == '')return



        var reg = /^[\d]{6,12}$/
        if (reg.test($(this).val())) {


            $('#password i').html('')
            $('#password').removeClass('has-error')
                .addClass('has-success')
            $('#password span').removeClass('glyphicon-remove')
                .addClass('glyphicon-ok')
        }else {
            $('#password i').html('6-12位纯数字')
            $('#password').removeClass('has-success')
                .addClass('has-error')
            $('#password span').removeClass('glyphicon-ok')
                .addClass('glyphicon-remove')
        }
    })

     $('#passwd input').blur(function () {
        if ($(this).val() == '')return



        var reg = /^[\d]{6,12}$/
        if ($(this).val() == $('#password input').val()) {


            $('#passwd i').html('')
            $('#passwd').removeClass('has-error')
                .addClass('has-success')
            $('#passwd span').removeClass('glyphicon-remove')
                .addClass('glyphicon-ok')
        }else {
            $('#passwd i').html('两次密码不一样')
            $('#passwd').removeClass('has-success')
                .addClass('has-error')
            $('#passwd span').removeClass('glyphicon-ok')
                .addClass('glyphicon-remove')
        }
    })

     $('#phone input').blur(function () {
        if ($(this).val() == '')return



        var reg = /^1[3|5|6|7|8|9]\d{9}$/
        if (reg.test($(this).val())) {


            $('#phone i').html('')
            $('#phone').removeClass('has-error')
                .addClass('has-success')
            $('#phone span').removeClass('glyphicon-remove')
                .addClass('glyphicon-ok')
        }else {
            $('#phone i').html('请输入正确的11位手机号码')
            $('#phone').removeClass('has-success')
                .addClass('has-error')
            $('#passwd span').removeClass('glyphicon-ok')
                .addClass('glyphicon-remove')
        }
    })
})