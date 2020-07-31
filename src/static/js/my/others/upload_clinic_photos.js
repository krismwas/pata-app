$(document).ready(function () {

    $(".delt").click(function () {
        var pic_id = $(this).val()
        var url_loc = $(this).attr("data-url")
        // console.log(pic_id)
        $(this).parent().parent().hide()
        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:delclinicpic' %}",
        url: url_loc,
        data: {
                // csrfmiddlewaretoken: "{{ csrf_token }}",
                pic_id: pic_id
                }

                })
        request.done(function (data) {
            showFlashMessage("Picture deleted")


        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request !!")
            } else if (jqXHR.status == 401){
                alert("You must be logged in to do this!")
            } else {
                alert("There was an error with your request. Please try again.")
            }
        })

    })

})