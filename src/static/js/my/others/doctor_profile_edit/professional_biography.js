$(document).ready(function () {
    $(".p_bg").click(function (e) {
        e.preventDefault()
        var probio = $("textarea[name='professinal_biography']").val()
        var url_loc = $(this).parent().attr("data-url")
        $(this).parent().parent().hide()
        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:professinal_bio' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            probio:probio,
        }
        })
        request.done(function (data) {
             if(data.success){
                showFlashMessage("Your professional biography has been updated successfully")
            }

        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request")
            }
            else if (jqXHR.status == 401){
                alert("You must be logged in to edit your professional biography")
            }
            else if (jqXHR.status == 404){
                alert("Not found")
            }
            else {
                alert("There was an error with your request. Please try again.")
            }
        })
    })

})