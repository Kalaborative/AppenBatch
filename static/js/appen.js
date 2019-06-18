$(document).ready(function() {
  $("#updateBtn").click(function() {
      $("#doneBtn").hide();
      $("#statusAnimation").html('<img src="static/img/flask.svg">');
      $("#updateStatus").html('Great! Your results are updating. Please wait for the button to appear to close this modal. This will take about 5 minutes.');
      var bar1 = new ldBar("#progressBar");
      var bar2 = document.getElementById('progressBar').ldBar;
      bar1.set(0);
      $.ajax({
        type: 'get',
        url: '/api-update-1'
      }).done(function(res) {
        bar1.set(res['progress']);
        $.ajax({
          type: 'get',
          url: '/api-update-2'
        }).done(function(res) {
          bar1.set(res['progress']);
          $.ajax({
            type: 'get',
            url: '/api-update-3'
          }).done(function (res) {
            bar1.set(res['progress']);
            $.ajax({
              type: 'get',
              url: '/api-update-4'
            }).done(function (res) {
              bar1.set(res['progress']);
              $.ajax({
                type: 'get',
                url: '/api-update-5'
              }).done(function (res) {
                bar1.set(res['progress']);
                $.ajax({
                  type: 'get',
                  url: '/api-update-6'
                }).done(function(res) {
                  console.log(res);
                  if (res['maj_tr_hasBatch']) {
                    $("#majorTransWorkAvailable").html("YES");
                  } else {
                    $("#majorTransWorkAvailable").html("NO");
                  }
                  $("#majorTransWorkNum").html(res['maj_tr_numBatch']);

                  if (res['maj_qa_hasBatch']) {
                    $("#majorQAWorkAvailable").html("YES");
                  } else {
                    $("#majorQAWorkAvailable").html("NO");
                  }
                  $("#majorQAWorkNum").html(res['maj_qa_numBatch']);

                  if (res['min_tr_hasBatch']) {
                    $("#minorTransWorkAvailable").html("YES");
                  } else {
                    $("#minorTransWorkAvailable").html("NO");
                  }
                  $("#minorTransWorkNum").html(res['min_tr_numBatch']);

                  if (res['min_qa_hasBatch']) {
                    $("#minorQAWorkAvailable").html("YES");
                  } else {
                    $("#minorQAWorkAvailable").html("NO");
                  }
                  $("#minorQAWorkNum").html(res['min_qa_numBatch']);

                  let d = new Date().toLocaleString();
                  let last_updated = "Last updated on " + d;

                  $(".updateDate").html(last_updated);

                  $("#statusAnimation").html('<img src="static/img/party.svg">');
                  $("#doneBtn").show();
                  $("#updateStatus").html("Congrats! The data has been updated. Please click the button below to exit this modal.");
                  bar1.set(100);
                })
              })
            })
          })
        })
      }).fail(function(){
        $("#statusAnimation").html('<img src="static/img/heartbeat.svg">');
        $("#doneBtn").show();
        $("#updateStatus").html("There's been an error. Sorry! Please try again.");
      });
  });  
}); 
