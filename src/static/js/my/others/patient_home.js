
$(document).ready(function () {
    $("#patient_username").click(function (e) {
        e.preventDefault()

        var username = $("input[name='username']").val()
        var url_loc = $(this).parent().attr("data-url")
        $(this).parent().parent().hide()
        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:patient_username_ajax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            username:username,
        }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("username updated successfully !!")
            }

        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request !!")
            }
            else if (jqXHR.status == 401){
                alert("You must be logged to finish this task")
            }
            else if (jqXHR.status == 404){
                alert("page not found !!")
            }
            else {
                alert("There was an error with your request. Please try again.")
            }
            })
    })

    $("#btnemail").click(function (e) {
        e.preventDefault()

        var email = $("input[name='email']").val()
        var url_loc = $(this).parent().attr("data-url")
        console.log(email)
        $(this).parent().parent().hide()
        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:patient_email_ajax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            email:email,
        }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("email updated successfully !!")
            }

        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request !!")
            }
            else if (jqXHR.status == 401){
                alert("You must be logged to finish this task")
            }
            else if (jqXHR.status == 404){
                alert("page not found !!")
            }
            else {
                alert("There was an error with your request. Please try again.")
            }
        })
        })

     $("#btnfirst_name").click(function (e) {
        e.preventDefault()

        var first_name = $("input[name='first_name']").val()
        var url_loc = $(this).parent().attr("data-url")
        // console.log("momomommomomom")
        $(this).parent().parent().hide()
        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:patient_fname_ajax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            first_name:first_name,
        }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("first name updated successfully !!")
            }

        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request !!")
            }
            else if (jqXHR.status == 401){
                alert("You must be logged to finish this task")
            }
            else if (jqXHR.status == 404){
                alert("page not found !!")
            }
            else {
                alert("There was an error with your request. Please try again.")
            }
        })
        })

     $("#last_name").click(function (e) {
        e.preventDefault()

        var last_name = $("input[name='last_name']").val()
        var url_loc = $(this).parent().attr("data-url")
        $(this).parent().parent().hide()
        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:patient_lname_ajax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            last_name:last_name,
        }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("last name updated successfully !!")
            }

        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request !!")
            }
            else if (jqXHR.status == 401){
                alert("You must be logged to finish this task")
            }
            else if (jqXHR.status == 404){
                alert("page not found !!")
            }
            else {
                alert("There was an error with your request. Please try again.")
            }
        })
        })



    $(function () {
            $("#datepicker").datepicker({ dateFormat: 'dd-mm-yy' });
               // $("#datepicker").datepicker({ minDate: (new Date(1910, 1 - 1)), maxDate: (new Date(2005, 1 - 1)), dateFormat: 'dd-mm-yy' });
               //        $("#datepicker").datepicker({ minDate: 0, maxDate: 7 },{ dateFormat: 'dd-mm-yy' });

        });
    $(".probackground").click(function () {
        $(this).parent().parent().next().children("td").children("div").show()
        })


    $("#mobileno").click(function (e) {
        e.preventDefault()

        var mobile_no = $("input[name='mobile_no']").val()
        var url_loc = $(this).parent().attr("data-url")
        $(this).parent().parent().hide()
        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:patient_mobile_no_ajax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            mobile_no:mobile_no,
        }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("mobile number updated successfully !!")
            }

        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request !!")
            }
            else if (jqXHR.status == 401){
                alert("You must be logged to finish this task")
            }
            else if (jqXHR.status == 404){
                alert("page not found !!")
            }
            else {
                alert("There was an error with your request. Please try again.")
            }
        })
    })



    $("#patient_dob").click(function (e) {
        e.preventDefault()

        var dob = $("input[name='dob']").val()
        var url_loc = $(this).parent().attr("data-url")
        $(this).parent().parent().hide()
        var request = $.ajax({
        method: "POST",
        // url: "{% url 'doctor:patient_dob_ajax' %}",
        url: url_loc,
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            dob:dob,
        }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("date of birth updated successfully !!")
            }

        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request !!")
            }
            else if (jqXHR.status == 401){
                alert("You must be logged to finish this task")
            }
            else if (jqXHR.status == 404){
                alert("page not found !!")
            }
            else {
                alert("There was an error with your request. Please try again.")
            }
        })
    })
})










