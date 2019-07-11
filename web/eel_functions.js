$(document).ready(function () {

});

eel.expose(show_ok_modal);
function show_ok_modal() {
    $('#ok_modal')
        .modal("show")
        ;

    $('#wait_modal')
        .modal("hide")
        ;

    $("#cancel_selection").show();
}

eel.expose(show_wait_modal);
function show_wait_modal() {
    $('#wait_modal')
        .modal("setting", "closable", false)
        .modal("show")
        ;
}

eel.expose(set_image);
function set_image(img) {
    selected_region()
    var prev_img = "data:image/jpg;base64," + img.slice(2, -1)
    $("#img_segment").addClass("ui segment")
    $("#preview_img").attr("src", prev_img)
}

eel.expose(set_modal_eel);
function set_modal_eel(modal_option) {
    set_modal(modal_option);
}