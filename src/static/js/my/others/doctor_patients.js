
$( document ).ready(function() {
    $(":button").click(function () {
        $(this).parent().parent().hide()
    }),

    $(".unverify").click(function () {
        var patient_id = $(this).val()
        var url_loc = $(this).attr("data-url")
        var request = $.ajax({
            method: "POST",
            // url: "{% url 'doctor:patient_unverification_ajax' %}",
            url: url_loc,
            data: {
                    patient_id: patient_id
                    }
                    })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("successful not your patient anymore!!")
            }
        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request!")
            } else if (jqXHR.status == 401){
                alert("You must be logged in to do this!")
            } else {
                alert("There was an error with your request. Please try again.")
            }
    })
    })
});
