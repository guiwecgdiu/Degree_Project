$(document).ready(function () {
    // add all event handlers here
    console.log("Adding event handlers");
    $("#username input").on("focus", focus_username);
    $("#username input").on("blur", blur_username);
    $("#username").on("change", check_username);
    $("#useremail").on("change", check_email);
    $("#useremail input").on("focus", focus_email);
    $("#userpassword input").on("focus", focus_pasword);
    $("#userpassword input").on("blur", blur_password);
    $("#userpassword").on("change", check__password);
    $("#userpassword2 input").on("focus", focus_password2);
    $("#userpassword2").on("change", check_password2);
    $("#changepassword input").on("focus", focus_changepasword);
    $("#changepassword").on("change", check_changepassword);
    $("#changepassword input").on("blur", blur_changepasword);

    console.log("function registered");

});
function focus_password2() {
    $("#userpassword2 span").removeClass();
    $("#userpassword2 span").html("")
}
function focus_email() {
    $("#useremail span").removeClass();
    $("#useremail span").html("")
}
function blur_changepasword() {
    $("#hintchangepassword").removeClass();
    $("#hintchangepassword").html("");
}
function focus_changepasword() {
    $("#changepassword span").removeClass();
    $("#changepassword span").html("")
    $("#hintchangepassword").removeClass();
    $("#hintchangepassword").html('<span>' + "length from 6 to 15" + '</span>');
    $("#hintchangepassword").addClass("success");
}

function check_changepassword() {
    var chosen_password = $(this).find("input");
    console.log(chosen_password.val().length);
    if (chosen_password.val().length <= 15 && chosen_password.val().length >= 6) {
        console.log("correct password");
        $("#checkchangepassword").removeClass();
        $("#checkchangepassword").addClass("success");

        $("#checkchangepassword").html('<span>' + "usable password" + '</span>');
    } else {
        console.log("wrong password");
        chosen_password.val("");
        // chosen_password.focus();
        window.setTimeout(function () {
            chosen_password.focus();
        }, 0);

        $("#checkchangepassword").html('<span>' + "Wrong format" + '</span>');
        $("#checkchangepassword").addClass("failure");
    }

}

function check_password2() {
    console.log("check password2");
    var first_password = $("#userpassword").find("input");
    var second_password = $(this).find("input");
    if (first_password.val() !== second_password.val()) {
        second_password.val("");
        // second_password.focus();
        window.setTimeout(function () {
            second_password.focus();
        }, 0);

        $("#checkpassword2").removeClass();
        $("#checkpassword2").html('<span>' + "different password" + '</span>');
        $("#checkpassword2").addClass("failure");
    }
    // else {
    //     $("#checkpassword2").removeClass();
    //     $("#checkpassword2").html('<span>' + "correct password" + '</span>');
    //     $("#checkpassword2").addClass("success");
    // }
}

function focus_pasword() {
    $("#userpassword span").removeClass();
    $("#userpassword span").html("")
            $("#checkpassword").removeClass();
            $("#checkpassword").html("")
    $("#hintpassword").removeClass();
    $("#hintpassword").html('<span>' + "length from 6 to 15" + '</span>');
    $("#hintpassword").addClass("success");
    // var pop = $('#userpassword input').contip({
    //
    //     align: 'bottom', //出现在元素底部
    //
    //     html: "length from 6 to 15"
    //
    //   });
    // pop.show();
}

function blur_password() {
    console.log("blur password");

    $("#hintpassword").removeClass();
    $("#hintpassword").html("");
}

function check__password() {
    var chosen_password = $(this).find("input");
    console.log(chosen_password.val().length);
    if (chosen_password.val().length <= 15 && chosen_password.val().length >= 6) {
        console.log("correct password");
        $("#checkpassword").removeClass();
        $("#checkpassword").addClass("success");

        $("#checkpassword").html('<span>' + "usable password" + '</span>');
    } else {
        console.log("wrong password");
        chosen_password.val("");
        // chosen_password.focus();
        window.setTimeout(function () {
            chosen_password.focus();
        }, 0);

        $("#checkpassword").html('<span>' + "Wrong format" + '</span>');
        $("#checkpassword").addClass("failure");
    }

}

function check_email() {
    console.log("check email");
    var regex = /^([a-zA-Z0-9])+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$/;

    var chosen_email = $(this).find("input");
    if (!regex.test(chosen_email.val())) {
        console.log("wrong format");
        chosen_email.val("");
        // chosen_email.focus();
        window.setTimeout(function () {
            chosen_email.focus();
        }, 0);

        $("#checkemail").html('<span>' + "Wrong format" + '</span>');
        $("#checkemail").addClass("failure");
    } else {
        $("#checkemail").removeClass();
        $("#checkemail").html("");
        console.log("true format");
        $.post('/checkemail', {
            'email': chosen_email.val() //field value being sent to the server
        }).done(function (response) {
            var server_code = response['emailreturnvalue'];
            if (server_code == 0) { // success: Username does not exist in the database
                $("#checkemail").html('<span>' + "Usable email" + '</span>');
                $("#checkemail").addClass("success");
            } else { // failure: Username already exists in the database
                chosen_email.val("");
                // chosen_user.focus();
                window.setTimeout(function () {
                    // chosen_user.focus();
                }, 0);

                $("#checkemail").html('<span>' + "This email is used by others" + '</span>');
                $("#checkemail").addClass("failure");
            }
        }).fail(function () {
            $("#checkemail").html('<span>Error contacting server</span>');
            $("#checkemail").addClass("failure");
        });
    }
}

function focus_username() {
    $("#username span").removeClass();
    $("#username span").html("")
    $("#checkuser").removeClass();
    $("#checkuser").html("")
    console.log("focus_username called");
    // var chosen_user = $(this).find("input");
    $("#hintuser").removeClass();
    $("#hintuser").html('<span>' + "String length from 3 to 10" + '</span>');
    $("#hintuser").addClass("success");
}

function blur_username() {
    console.log("blur_username called");
    // var chosen_user = $(this).find("input");
    $("#hintuser").removeClass();
    $("#hintuser").html("");
}

function check_username() {
    blur_username()
    // get the source element
    console.log("check_username called");
    var chosen_user = $(this).find("input");
    console.log("User chose: " + chosen_user.val());
    $("#checkuser").removeClass();
    $("#checkuser").html('<img src="static/style/icon/loading.gif")>');
    var regex = /^[A-Za-z0-9\u4e00-\u9fa5]{3,10}$/;
    if (!regex.test(chosen_user.val())) {
        console.log("wrong format");
        chosen_user.val("");
        // chosen_user.focus();
        window.setTimeout(function () {
            chosen_user.focus();
        }, 0);

        $("#checkuser").html('<span>' + "Wrong format" + '</span>');
        $("#checkuser").addClass("failure");
    } else {
        console.log("true format");
        $.post('/checkuser', {
            'username': chosen_user.val() //field value being sent to the server
        }).done(function (response) {
            var server_code = response['returnvalue'];
            if (server_code == 0) { // success: Username does not exist in the database
                $("#checkuser").html('<span>' + "Usable name" + '</span>');
                $("#checkuser").addClass("success");
            } else { // failure: Username already exists in the database
                chosen_user.val("");
                // chosen_user.focus();
                window.setTimeout(function () {
                    // chosen_user.focus();
                }, 0);

                $("#checkuser").html('<span>' + "This name is used by others" + '</span>');
                $("#checkuser").addClass("failure");
            }
        }).fail(function () {
            $("#checkuser").html('<span>Error contacting server</span>');
            $("#checkuser").addClass("failure");
        });
    }
    // ajax code
    // end of ajax code
    console.log("finished check_username");
}