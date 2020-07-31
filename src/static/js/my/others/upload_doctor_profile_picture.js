$(document).ready(function () {

    $(".delt").click(function () {
        // var pic_id = $(this).val()
        // console.log(pic_id)
        $(this).parent().parent().hide()
        var url_loc = $(this).parent().attr("data-url")
        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:profile_pic_delete_ajax' %}",
        url: url_loc,
        data: {
                // csrfmiddlewaretoken: "{{ csrf_token }}",

            }

            })
        request.done(function (data) {
            showFlashMessage("Profile picture deleted")
          // $("#"+"instance.clinic_photo.id").hide()


            })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 404){
                alert("Page not found!")
            } else if (jqXHR.status == 401){
                alert("You must be logged in to do this!")
            } else {
                alert("There was an error with your request. Please try again.")
            }
            })

        })

})