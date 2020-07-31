$(document).ready(function () {
    $("#professional_education").click(function (e) {
        e.preventDefault()

        var edu = $("textarea[name='edu']").val()
        var url_loc = $(this).parent().attr("data-url")

        $(this).parent().parent().hide()
        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:professional_education_ajax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            edu:edu,
        }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("education updated successfully")
            }

        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request !!")
            } else if (jqXHR.status == 401){
                alert("You must be logged to finish this task")
            }
             else if (jqXHR.status == 404){
                alert("Not found")
            }
            else {
                alert("There was an error with your request. Please try again.")
            }
        })
    })


     $("#p_membership").click(function (e) {
        e.preventDefault()

        var pmembership = $("textarea[name='pmembership']").val()
        var url_loc = $(this).parent().attr("data-url")

        $(this).parent().parent().hide()
        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:professional_membership_ajax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            pmembership:pmembership,
        }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("professional membership updated successfully")
            }

        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request !!")
            } else if (jqXHR.status == 401){
                alert("You must be logged to finish this task")
            }
             else if (jqXHR.status == 404){
                alert("Not found")
            }
            else {
                alert("There was an error with your request. Please try again.")
            }
        })
    })



    $("#board_certification").click(function (e) {
        e.preventDefault()

        var bcertification = $("textarea[name='bcertification']").val()
        var url_loc = $(this).parent().attr("data-url")

        $(this).parent().parent().hide()
        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:bcertifications_ajax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            bcertification:bcertification,
        }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("board certification updated successfully")
            }

        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request !!")
            } else if (jqXHR.status == 401){
                alert("You must be logged to finish this task")
            }
             else if (jqXHR.status == 404){
                alert("Not found")
            }

            else {
                alert("There was an error with your request. Please try again.")
            }
        })
    })



    $("#professinal_awards").click(function (e) {
        e.preventDefault()

        var pawards = $("textarea[name='pawards']").val()
        var url_loc = $(this).parent().attr("data-url")

        $(this).parent().parent().hide()
        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:professional_award_ajax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            pawards:pawards,
        }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("proffessional award updated successfully")
            }

        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request !!")
            } else if (jqXHR.status == 401){
                alert("You must be logged to finish this task")
            }
            else if (jqXHR.status == 404){
                alert("Not found !!")
            }
            else {
                alert("There was an error with your request. Please try again.")
            }
        })
    })

})