(function() {
  var canvas = document.getElementById('canvas'),
      context = canvas.getContext('2d'),
      video = document.getElementById('video'),
      vendorUrl = window.URL || window.webkitURL;

  navigator.getMedia = navigator.getUserMedia ||
                       navigator.webKitGetUserMedia ||
                       navigator.mozGetUserMEdia ||
                       navigator.msGetUserMEdia;
  navigator.getMedia({
    video: true,
    audio: false
  }, function(stream){
    video.src = vendorUrl.createObjectURL(stream);
    video.play();
  }, function(error){
    // A ocurrido un error.
    // error.code
  });
})();
