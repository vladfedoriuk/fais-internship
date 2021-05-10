function init(){
    $("#runs").hide();
    $("#dates").show();
}

$( window ).on('load', function() {
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
});

