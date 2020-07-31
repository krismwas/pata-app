$(document).ready(function () {

       $("#btnUsername").click(function () {
        event.preventDefault()
        var username = $("input[name='username']").val()
        var url_loc = $(this).parent().attr("data-url")


        $(this).parent().parent().hide()

        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:doc_username_ajax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            username : username,
            }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("username updated successfully !!")
            }
        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request")
            } else if (jqXHR.status == 401){
                alert("You must be logged in to write a review!")
            }
            else if (jqXHR.status == 404){
                alert("Not found !!")
            }
            else {
                alert("There was an error with your request. Please try again.")
            }
        })
    })


  $(".btnFirstName").click(function () {
        event.preventDefault()
        var fname = $("input[name='fname']").val()
        var url_loc = $(this).parent().attr("data-url")

        $(this).parent().parent().hide()

        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:first_name_ajax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            fname: fname,
            }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("first name updated successfully")
            }
        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request")
            } else if (jqXHR.status == 401){
                alert("You must be logged in to write a review!")
            }
            else if (jqXHR.status == 404){
                alert("Not found !!")
            }
            else {
                alert("There was an error with your request. Please try again.")
            }
        })
    })


     $(".btnSecondName").click(function () {
        event.preventDefault()
        var sname = $("input[name='sname']").val()
        var url_loc = $(this).parent().attr("data-url")
        $(this).parent().parent().hide()

        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:second_name_ajax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            sname : sname,
            }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("second name updated successfully !!")
            }
        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request")
            } else if (jqXHR.status == 401){
                alert("You must be logged in to write a review!")
            }
            else if (jqXHR.status == 404){
                alert("Not found !!")
            }
            else {
                alert("There was an error with your request. Please try again.")
            }
        })
    })


    $(".btnLastName").click(function () {
        event.preventDefault()
        var lname = $("input[name='lname']").val()
        var url_loc = $(this).parent().attr("data-url")

        $(this).parent().parent().hide()

        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:last_name_ajax' %}",
        url:url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            lname : lname,
            }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("last name updated successfully !!")
            }
        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request")
            } else if (jqXHR.status == 401){
                alert("You must be logged in to write a review!")
            }
            else if (jqXHR.status == 404){
                alert("Not found !!")
            }
            else {
                alert("There was an error with your request. Please try again.")
            }
        })
    })



    $("#mobile_no").click(function () {
        event.preventDefault()
        var mobile_no = $("input[name='mobile']").val()
        var url_loc = $(this).parent().attr("data-url")

        $(this).parent().parent().hide()

        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:patient_mobile_no_ajax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            mobile_no : mobile_no,
            }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("mobile number updated successfully !!")
            }
        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request")
            } else if (jqXHR.status == 401){
                alert("You must be logged in to write a review!")
            }
            else if (jqXHR.status == 404){
                alert("Not found !!")
            }
            else {
                alert("There was an error with your request. Please try again.")
            }
        })
    })



    $(".btnEmail").click(function () {
        event.preventDefault()
        var email = $("input[name='email']").val()
        var url_loc = $(this).parent().attr("data-url")

        $(this).parent().parent().hide()

        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:email_ajax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            email : email,
            }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("email updated successfully !!")
            }
        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request")
            } else if (jqXHR.status == 401){
                alert("You must be logged in to write a review!")
            }
            else if (jqXHR.status == 404){
                alert("Not found !!")
            }
            else {
                alert("There was an error with your request. Please try again.")
            }
        })
    })


    $(".btnDOB").click(function () {
        event.preventDefault()
        var dob = $("input[name='dob']").val()
        var url_loc = $(this).parent().attr("data-url")

        $(this).parent().parent().hide()

        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:dob_ajax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            dob : dob,
            }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("Date of birth updated successfully !!")
            }
        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request")
            }
            else if (jqXHR.status == 401){
                alert("You must be logged in to write a review!")
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