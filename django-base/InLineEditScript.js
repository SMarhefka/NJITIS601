// JavaScript source code
/*
    $(document).ready(function () {
        $(document).on("dblclick", ".editable", function () {
            var value = $(this).text();
            var data_type = $(this).data("type");
            var input_type = "text";
            if (data_type == "created_at") {
                input_type = "datetime-local";
            }
            var input = "<input type='" + input_type + "' class='input-data' value='" + value + "' class='form-control'>";
            $(this).html(input);
            $(this).removeClass("editable")
        });

        $(document).on("blur", ".input-data", function () {
            var value = $(this).val();
            var td = $(this).parent("td");
            $(this).remove();
            td.html(value);
            td.addClass("editable");
            var type = td.data("type");
            // Send the information to the server
            sendToServer(td.data("id"), value, type);
        });
        $(document).on("keypress", ".input-data", function (e) {
            var key = e.which;
            if (key == 13) {
                var value = $(this).val();
                var td = $(this).parent("td");
                $(this).remove();
                td.html(value);
                td.addClass("editable");
                var type = td.data("type");
                // prevent page from refreshing
                e.preventDefault();
                sendToServer(td.data("id"), value, type);
            }
        });

        // Function to send our data to the server
        function sendToServer(id, value, type) {
            console.log(id);
            console.log(value);
            console.log(type);
            $.ajax({
                url: '/upload',
                type: "POST",
                data: { id: id, type: type, value: value },
            })
                .done(function (response) {
                    console.log(response);
                })
                .fail(function () {
                    console.log("Error Occured");
                });

        }
    });
    */
