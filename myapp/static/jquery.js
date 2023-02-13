function prepS2(clicked_id){
      $.ajax({
        url: "levelFunc",
        method: 'GET', // or another (GET), whatever you need
        data:{
            id: clicked_id
        },
        success: success,
        error: error
    });

      function success(response){
        //frame = document.getElementById('mat_frame');
        //frame.setAttribute('src', response.response);
        document.getElementById("mat_frame").src= response.response;

      }

      function error(){
        alert('error');
      }
}