function init(){
    $("#runs").hide();
    $("#dates").show();
}

$(window).on('load', function() {
    init();
});

$(document).ready(function(){
  $("#dates-option").click(function(){
    $("#runs").hide();
    $("#dates").show();
  });

  $("#runs-option").click(function(){
    $("#dates").hide();
    $("#runs").show();
  });

  function create_error_li(text){
    var ul = document.getElementById("form-errors-additional");
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(text));
    ul.appendChild(li);
  }

  $("#add-form").on("submit", function(event){
    var ul = document.getElementById("form-errors-additional");
    ul.querySelectorAll('*').forEach(n => n.remove());

      if(
        (document.getElementById('id_valid_from_date').value && document.getElementById('id_valid_to_date').value ||
        (document.getElementById('id_run_from').value && document.getElementById('id_run_to').value) ||
        (document.getElementById('id_filename_from').value && document.getElementById('id_filename_to').value)
      )){
        return true;
      }
      
      
      var search_option = [...document.getElementsByName('search_option')].
        filter(n => n.checked)[0].value;

      console.log(search_option);

      if (search_option == 'dates'){
        if ( !document.getElementById("id_valid_from_date").value && 
                document.getElementById("id_valid_from_time").value) {
          create_error_li(
            "The date the configuration is valid from is required if the relevant time is specified.");
          event.preventDefault(); 
          return false;
        }
        if (!document.getElementById("id_valid_to_date").value && 
              document.getElementById("id_valid_to_time").value) {
          create_error_li(
            "The date the configuration is valid to is required if the relevant time is specified."
          );
          event.preventDefault(); 
          return false;
        }
        if( (document.getElementById("id_valid_from_date").value &&
              !document.getElementById("id_valid_to_date").value ) ||
            (document.getElementById("id_valid_to_date").value &&
              !document.getElementById("id_valid_from_date").value)) {
                create_error_li('If any of the validity dates is specified, then another one must be given too.');
                event.preventDefault(); 
                return false;
        }
      }

      else if (search_option == 'runs'){
        console.log('here');
        if ( 
          (!document.getElementById("id_run_from").value && document.getElementById("id_run_to").value) ||
          (document.getElementById("id_run_from").value && !document.getElementById("id_run_to").value)
        ){
          create_error_li(
            'If any of the run-id\'s is specified, another one must be provided too.'
          );
          event.preventDefault(); 
          return false;
        }
        if ( 
          (!document.getElementById("id_filename_from").value && document.getElementById("id_filename_to").value) ||
          (document.getElementById("id_filename_from").value && !document.getElementById("id_filename_to").value)
        ){
          create_error_li(
            'If any of the run filenames is specified, another one must be provided too.'
          );
          event.preventDefault(); 
          return false;
        }
      }
      create_error_li(
        'Either run id\'s, filenames or validation dates must be specified'
      );
      event.preventDefault(); 
      return false;
  });
});

