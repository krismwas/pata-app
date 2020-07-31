$(document).ready(function () {

    $(":button").click(function () {
        $(this).hide()
    })


    $(".verify").click(function () {
        var patient_id = $(this).val()
        var url_loc = $(this).attr("data-url")

        var request = $.ajax({
            method: "POST",
            // url: "{% url 'doctor:patient_verification' %}",
            url: url_loc,
            data: {
                    // csrfmiddlewaretoken: "{{ csrf_token }}",
                    patient_id: patient_id
                    }

                    })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("successful patient verification !!")
            }

        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request!")
            }
            else if (jqXHR.status == 401){
                alert("You must be logged in to do this!")
            }
              else if (jqXHR.status == 404){
                alert("page not found!")
            }
            else {
                alert("There was an error with your request. Please try again.")
            }
        })
        })
    
})