$(document).ready(function () {

    $("#cancel_selection").hide();
    $("#stop_recording").hide();


    $("#new_btn").click(function () {
        mode = ticked_mode()
        if (do_png) {
            eel.save_png(mode)
            return
        }

        if (region_selected) {
            start_record(mode)
            $("#stop_recording").show();
            $("#cancel_selection").hide();
            $("#new_btn").toggleClass("disabled")
            return
        }

        get_preview_image(mode)
        $("#cancel_selection").show();
        $("#preview_img").show();
        $(this).children("p").text("Start")
        $(this).children("i").toggleClass("play")
        toggle_menu(menu_items.slice(1))
    });

    $("#stop_recording").click(function () {
        eel.stop_record()
        $("#stop_recording").hide();
        $("#new_btn").toggleClass("disabled")
    });

    $("#cancel_selection").click(function () {
        region_selected = false
        $(this).hide()
        $("#new_btn").children("p").text("New")
        $("#new_btn").children("i").toggleClass("play")
        $("#img_segment").removeClass("ui segment")
        $("#preview_img").hide();
        toggle_menu(menu_items.slice(1))
    });

    $("#modus_items > .item").click(function () {
        $("#modus_items").children("div").each(function () {
            if ($(this).children("i").hasClass("check icon")) {
                $(this).children("i").toggleClass("check icon")
            };
        });
        $(this).children("i").toggleClass("check icon")
    });

    $("#delay_items> .item").click(function () {
        var clicked_item = $(this).attr('id')
        $("#delay_items").children("div").each(function () {
            if ($(this).attr('id') != clicked_item) {
                if ($(this).children("i").hasClass("check icon")) {
                    $(this).children("i").toggleClass("check icon")
                    delay_id = "0_Sec"
                };
            }
        });
        $(this).children("i").toggleClass("check icon")
        delay_id = $(this).attr('id')
    });

    $("#option_items > .item").click(function () {
        $("#option_items").children("div").each(function () {
            if ($(this).children("i").hasClass("check icon")) {
                $(this).children("i").toggleClass("check icon")
                do_png = false
            };
        });
        $(this).children("i").toggleClass("check icon")
        if ($(this).attr('id') == "png_opt") {
            do_png = true
        }
    });

}); // End document.ready

region_selected = false
var delay_id = ""
var do_png = false

var delay_dict = {
    "0_sec": 0,
    "1_sec": 1000,
    "2_sec": 2000,
    "3_sec": 3000,
    "4_sec": 4000,
    "5_sec": 5000
};

var menu_items = [
    "#new_btn",
    "#mode_menu",
    "#delay_menu",
    "#option_menu",
]

function selected_region() {
    region_selected = true
}


function ticked_mode() {
    $("#modus_items").children("div").each(function () {
        if ($(this).children("i").hasClass("check icon")) {
            select_id = this.id
        };
    });
    return select_id;
}

function ticked_delay() {
    var select_delay = "0_sec"
    $("#delay_items").children("div").each(function () {
        if ($(this).children("i").hasClass("check icon")) {
            select_delay = this.id
            console.log("Test")
        };
    });
    return select_delay;
}

function get_preview_image(mode) {
    eel.get_preview(mode)

}

function set_modal(modal_option) {
    $('#window_modal')
        .modal(modal_option)
        ;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


async function start_record() {
    var delay = delay_dict[delay_id];
    await sleep(delay);
    eel.start_record();
}


function toggle_menu(items) {
    items.forEach(function (item) {
        $(item).toggleClass("disabled");
    });
}
