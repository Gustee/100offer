//注册按钮
    //应聘者
$("#signup-button-applicant").click(function () {
        var username = $("#username").val();
        var mailaddress = $("#mailaddress").val();
        var password = $("#password").val();
        var password2 = $("#password2").val;
        if (password == password2) {
            $(".error-red-text").text("两次密码输入不同").show();
            return;
        }
        console.log($('#username').val())
        if (username.length < 5 || password.length < 6) {
            console.log("账号或密码格式不对");
            $(".error-red-text").text("账号或密码格式不对").show();
        } else {
            $.ajax({
                url: "/signup/",
                type: "POST",

                data: {
                    "type": "applicant",
                    "username": $("#username").val(),
                    "password": $("#password").val(),
                    "mailaddress": $("#mailaddress").val(),
                    "csrfmiddlewaretoken": $('[name=csrfmiddlewaretoken]').val()
                },
                success: function (data) {
                    console.log(data);
                    var returndata = JSON.parse(data);
                    console.log(returndata.msg);

                    if (returndata.msg == 1) {
                        console.log("邮箱已被使用");
                        $(".error-red-text").text("邮箱已被使用").show();
                    }
                }
            })
        }
    });
    //hr
$("#signup-button-hr").click(function () {
    var username = $("#username").val();
    var mailaddress = $("#mailaddress").val();
    var password = $("#password").val();
    var password2 = $("#password2").val;
    if (password == password2) {
        $(".error-red-text").text("两次密码输入不同").show();
        return;
    }
    console.log($('#username').val())
    var companyname = $("#companyname").val();
    var job = $("#job").val();
    var phone = $("#phone").val();
    if (username.length < 5 || password.length < 6) {
        console.log("账号或密码格式不对");
        $(".error-red-text").text("账号或密码格式不对").show();
    } else {
        $.ajax({
            url: "/signup/",
            type: "POST",

            data: {
                "type": "hr",
                "username": $("#username").val(),
                "password": $("#password").val(),
                "mailaddress": $("#mailaddress").val(),
                "companyname": companyname,
                "job": job,
                "phone": phone,
                "csrfmiddlewaretoken": $('[name=csrfmiddlewaretoken]').val()
            },
            success: function (data) {
                console.log(data);
                var returndata = JSON.parse(data);
                console.log(returndata.msg);

                if (returndata.msg == 1) {
                    console.log("邮箱已被使用");
                    $(".error-red-text").text("邮箱已被使用").show();
                }
            }
        })
    }
});

$("#signup-1").click(function(){console.log(11)});

$("#signup-2").click(function(){
    console.log("加载注册脚本");
    jQuery.getScript("/static/js/user-signup.js")
});