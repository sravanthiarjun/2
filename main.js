$(document).ready(function() {
    $("#myModal").on("hidden.bs.modal", function() {
        $("#iframeYoutube").attr("src", "#");
    })
})

function changeVideo(video) {
    var iframe = document.getElementById("iframeYoutube");
    iframe.src = "https://www.youtube.com/embed/" + video;
    $("#myModal").modal("show");
}
