$( document ).ready(function() {


    $("#new_specialty").click(function (e) {
        e.preventDefault()
        var new_specialty = $("input[name='enter_specialty']").val()
        var url_loc = $(this).parent().attr("data-url")
        console.log(new_specialty)
        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:new_specitys_ajax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            new_specialty:new_specialty
        }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("thank you for submitting this specialty we will add it soon!!")
            }
              if(data.success == "already"){
                showFlashMessage("already submitted thanks!!")
            }

        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request")
            } else if (jqXHR.status == 401){
                alert("You must be logged in")
            } else {
                alert("There was an error with your request. Please try again.")
            }
        })
    })


    $("#your_specialty").click(function (e) {
        e.preventDefault()
        var your_specialtys = $("#your_specialtys").val()
        var url_loc = $(this).parent().attr("data-url")
        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:doctors_specitys_ajax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            your_specialtys:your_specialtys
        }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("specialty updated successfully !!")
            }

        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request")
            } else if (jqXHR.status == 401){
                alert("You must be logged in")
            } else {
                alert("There was an error with your request. Please try again.")
            }
        })
    })


    $("#all_specialtys").click(function (e) {
        e.preventDefault()
        var doc_specialty = $("#specialty_selected").val()
        var url_loc = $(this).parent().attr("data-url")
        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:doctor_specialty_selected_ajax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            doc_specialty:doc_specialty
        }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("specialty added successfully !!")
            }

        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request")
            } else if (jqXHR.status == 401){
                alert("You must be logged in")
            } else {
                alert("There was an error with your request. Please try again.")
            }
        })
    })


    $(".selected_clinic").click(function () {
        event.preventDefault()
        var doc_selected_clinic = $("#doctor_selected_clinic").val()
        var url_loc = $(this).parent().attr("data-url")

        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:doc_selected_clinic_ajax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            doc_selected_clinic : doc_selected_clinic,
            }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("Clinic added successfully")
            }
        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("Bad request")
            } else if (jqXHR.status == 401){
                alert("You must be logged in!")
            } else {
                alert("There was an error with your request. Please try again.")
            }
        })
    })



    $(".dokClinicName").click(function (e) {
        e.preventDefault()
        var clinic_name = $("#clinic_name").val()
        var url_loc = $(this).parent().attr("data-url")
        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:clinic_name_ajax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            clinic_name:clinic_name
        }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("Your clinic was updated successfully")
            }

        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request")
            } else if (jqXHR.status == 401){
                alert("You must be logged to finish this task")
            } else {
                alert("There was an error with your request. Please try again.")
            }
        })
    })



    $(".probackground").click(function () {
        $(this).parent().parent().next().children("td").children("div").show()
    })

    $("#probio").click(function () {
        $(this).siblings().show()
    })

    $(":button").click(function () {
        $(this).parent().siblings("td").next().children("div").show()
    })

   $(function () {
        $("#datepicker").datepicker({ dateFormat: 'dd-mm-yy' });

    });


    $("#cpiks").one('click', function (event) {
        event.preventDefault()
        var url_loc = $(this).attr("data-url")

        var request = $.ajax({
        method: "GET",
        // url: "{% url 'doctor:clinicPhotosAjax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",

        }
        })
        request.done(function (data) {
            if (data.doctors_clinics){
                $("#clinicPhotos").append(data.doctors_clinics)
            }else {
            }

        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request !!")
            } else if (jqXHR.status == 401){
                alert("You must be logged in to write a review!")
            } else {
                alert("There was an error with your request. Please try again.")
            }
        })

    })

    // Gets the span width of the filled-ratings span
    // this will be the same for each rating
    var star_rating_width = $('.fill-ratings span').width();
    // Sets the container of the ratings to span width
    // thus the percentages in mobile will never be wrong
    $('.star-ratings').width(star_rating_width);


    var star_rating_width_small_font = $('.fill-ratings-small span').width();
    // Sets the container of the ratings to span width
    // thus the percentages in mobile will never be wrong
    $('.star-ratings-small').width(star_rating_width_small_font);

});