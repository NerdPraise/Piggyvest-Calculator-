$("#btns").click(function() {
    event.preventDefault()
    let form_url = $("#form").attr("form-data-url")
    $.ajax({
        url: form_url,
        type: "POST",
        data: {
            "amount":$("#amount").val(),
            "start":$("#start").val(),
            "end": $("#end").val(),
        },
        success: function (data) {
            if (data.error) {
                $(".error-text").text(data.error)
            } else if (data.success) {
                $("#texta").text(data.success)
            }
        },
        
    })
})