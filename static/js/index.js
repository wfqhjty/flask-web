$(function () {
    /**
     * Ajax用户登录
     */
    var url = getRootPath();
    $("#getuser").click(function () {
        data = {"username": $("#username").val()}
        $.ajax({
            url: url + "/user/getuser",
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json;charset=utf-8',
            data: JSON.stringify(data),
            timeout: 10000,
            success: function (data) {
                console.log(data)
                $("#content").text(data);
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert("查询失败");
            }
        });

    });
});