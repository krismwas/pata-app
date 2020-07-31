$(document).ready(function () {
    $(".no").click(function () {
        var review_id = $(this).val()
        var url_loc = $(this).attr("data-url")
        console.log(review_id)
        var request = $.ajax({
            method: "POST",
            // url: "{% url 'doctor:no_ajax' %}",
            url: url_loc,
            data: {
                    // csrfmiddlewaretoken: "{{ csrf_token }}",
                    review_id: review_id,
                    }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("ok removed")
            }
            if(data.success == "doesnotexists"){
                showFlashMessage("thanks you for reviewing")
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

    $(".abuse").click(function () {
        var review_id = $(this).val()
        var url_loc = $(this).attr("data-url")
        var request = $.ajax({
            method: "POST",
            // url: "{% url 'doctor:report_abuse_ajax' %}",
            url: url_loc,
            data: {
                    // csrfmiddlewaretoken: "{{ csrf_token }}",
                    review_id: review_id,
                    }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("thank you for reporting this. let us look at it")
            }
             if(data.success == "already_submitted"){
                showFlashMessage("please note we are looking at it")
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

    $(".helpful").click(function () {
        var review_id = $(this).val()
        var url_loc = $(this).attr("data-url")
        console.log(review_id)
        var request = $.ajax({
            method: "POST",
            // url: "{% url 'doctor:helpful_count_ajax' %}",
            url: url_loc,
            data: {
                    // csrfmiddlewaretoken: "{{ csrf_token }}",
                    review_id: review_id,
                    }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("thank you for reviewing")
            }
            if(data.success == "already"){
                showFlashMessage("already reviewed")
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

    $(".review input[type='submit']").click(function (event) {
        event.preventDefault()
       // var reviewmessage = $(this).val()
        var reviewmessage = $(".review textarea[name='reviewtxt']").val()
        var url_loc = $(this).parent().attr("data-url")
        var doc_id = $(this).parent().attr("doc_id")
        var request = $.ajax({
            method: "POST",
            // url: "{% url 'doctor:ajax_review_msg' %}",
            url: url_loc,
            data: {
                // csrfmiddlewaretoken: "{{ csrf_token }}",
                // doctor_id: "{{ object.id }}",
                doctor_id:doc_id,
                msgrvw:reviewmessage,
            }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("Your review has been submitted successfully!!")
            }
            if(data.docSelf){
              showFlashMessage("Sorry you cannot review yourself")
            }

        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request")
            } else if (jqXHR.status == 401){
                alert("You must be logged in to write a review!")
            } else {
                alert("There was an error with your request. Please try again.")
            }
        })

    })

    $(".rating input[type='radio']").click(function () {
        var inputValue = $(this).val()
        var url_loc = $(this).parent().parent().attr("data-url")
        var doc_id = $(this).parent().parent().attr("doc_id")
        var request = $.ajax({
            method: "POST",
            // url: "{% url 'doctor:ajax_rating' %}",
            url: url_loc,
            data: {
                // csrfmiddlewaretoken: "{{ csrf_token }}",
                // doctor_id: "{{ object.id }}",
                doctor_id: doc_id,
                rating_vaue: inputValue,
            }
        })
        request.done(function (data) {
            if(data.success){
                showFlashMessage("thank you for rating!!")
            }

        })
        request.fail(function (jqXHR, textStatus) {
            if (jqXHR.status == 400){
                alert("bad request!")
            } else if (jqXHR.status == 401){
                alert("You must be logged in to rate!")
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


    //this is for small medium and large devices
    // Gets the span width of the filled-ratings span
    // this will be the same for each rating
    var star_rating_width = $('.fill-ratings_sm_md_lg span').width();
    // Sets the container of the ratings to span width
    // thus the percentages in mobile will never be wrong
    $('.star-ratings_sm_md_lg').width(star_rating_width);


    var star_rating_width_small_font = $('.fill-ratings-small span').width();
    // Sets the container of the ratings to span width
    // thus the percentages in mobile will never be wrong
    $('.star-ratings-small').width(star_rating_width_small_font);

})