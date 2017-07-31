$(function () {
  function getCookie(name) {
    var cookieValue = null;
      if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
    return cookieValue;
  }

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
        // Only send the token to relative URLs i.e. locally.
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
      }
    }
  });


  $('#submitBtn').on('click', function () {
      var customerList = [];
      $('#customer-list tr').each(function () {
        $(this).find('td input:checked').each(function () {
          var checkedRow = $(this).closest('tr');
          customerList.push({
            'id': this.value,
            'full_name': $(checkedRow).find('td:eq(0)').text(),
            'email': $(checkedRow).find('td:eq(1)').text(),
            'company': $(checkedRow).find('td:eq(2)').text(),
            'city': $(checkedRow).find('td:eq(3)').text(),
            'country': $(checkedRow).find('td:eq(4)').text()
          });
        });
      });
      // check nothing selected
      // console.log(JSON.stringify(customerList));
      if (customerList.length) {
       $.ajax({
         type: "POST",
         url: "export/",  // the endpoint
         data: {customer_data: JSON.stringify(customerList)},
         success: function(data) {
           console.log("success");
           $('#customer-form')[0].reset();
         },
         error : function(xhr,errmsg,err) {
           console.log("An error");
         }
        });
      }
      else{
        console.log('nothing entered')
      }
  });
});
