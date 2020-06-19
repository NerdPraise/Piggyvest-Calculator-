$("#btns").click(function() { 
    event.preventDefault()
    let form_url = $("#form").attr("form-data-url")
    
    $.ajax({
        url: form_url,
        type: "POST",
        data: {
            "amount":$("#amount").val(),
            "plan":$("#plan").val(),
            "end": $("#end").val(),
        },
        success: function (data) {
            if (data.error) {
                $("#texta").text(data.error)
            } else if (data.success) {
                $("#texta").text(data.success)
            }
        },
        
    })
})

$(".export").click(function() {
    event.preventDefault()
    data = $("#texta").val()
    var doc = new jsPDF()

    doc.text(data, 10, 10)
    doc.save('a4.pdf')
})



$.post(url, function(data)
    {
        location.replace(url);
    });