$(function () {
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws"
    var ws_path = ws_scheme + "://" + window.location.host + "/news/stream"
    console.log("Connecting to " + ws_path)
    var socket = new ReconnectingWebSocket(ws_path)

    var json_data=""

    socket.onopen = function () {
        console.log("Connected to chat socket")
        $.getJSON("static/json/newsfeed.json", function (jsonData) {
            json_data = jsonData
        })
    }
    socket.onclose = function () {
        console.log("Disconnected from chat socket")
    }

    // Processing responses from the server
    socket.onmessage = function (message) {
        // Decode JSON
        console.log("Got websocket message " + message.data)
        var data = JSON.parse(message.data)
        // Handle errors
        if (data.error) {
            alert(data.error)
            return
        }
        // Handle joining
        if (data.join) {
            console.log("Joining world " + data.join)
            var worlddiv = $(
                "<div class='world' id='world-" + data.join + "'>" +
                "<div class='pane-header'><h2 class='text-center'>" + data.title + "- News" +
                " Feed</h2></div>" +
                "<div class='news'></div>" +
                "</div>"
            )
            $("#news-feed").append(worlddiv)


            // Handle leaving
        } else if (data.leave) {
            console.log("Leaving world " + data.leave)
            $("#world-" + data.leave).remove()

        } else if (data.News) {
            var newsdiv = $("#world-" + data.world + " .news")

            // Message
            var news_text = "<div class='news-item row'>" +
                "<div class='feed-item-text col-xs-10 col-sm-10 col-md-10" +
                " col-lg-10 col-xl-10'>" +
                "<span class='feed-time'>" + data.Time + "&nbsp;</span>" + data.News + "</div>" +
                "<div class='feed-item-click col-xs-1 col-sm-1 col-md-1" +
                " col-lg-1-xl-1'>" +
                "<a href='''>" +
                "<svg width='16px' height='11px' viewBox='0 0 16 11'" +
                " version='1.1' xmlns='http://www.w3.org/2000/svg'" +
                " xmlns:xlink='http://www.w3.org/1999/xlink'>" +
                "<!-- Generator: Sketch 47.1 (45422) -" +
                " http://www.bohemiancoding.com/sketch -->" +
                " <desc>Created with Sketch.</desc>" +
                "<defs></defs>" +
                "<g id='Page-1' stroke='none' stroke-width='1' fill='none'" +
                " fill-rule='evenodd'>" +
                "<g id='News-Feed-Open' transform='translate(-987.000000," +
                " -51.000000) fill-rule='nonzero' fill='#0000FF'>" +
                "<g id='Feed-List" +
                " transform='translate(762.000000, 44.000000)'>" +
                "<g id='Feed-Item'> <g id='Feed-text'" +
                " transform='translate(7.000000, 5.000000)>' +" +
                "<g id='Link' transform='translate(218.000000, 2.000000)'>" +
                "<g id='link'> <g id='Octicons'> <g id='link'>" +
                "<path d='M3.2,6.4 L4.26666667,6.4 L4.26666667,7.46666667" +
                " L3.2,7.46666667 C1.6,7.46666667 0,5.664 0,3.73333333" +
                " C0,1.80266667 1.65333333,0 3.2,0 L7.46666667,0" +
                " C9.01333333,0 10.6666667,1.80266667 10.6666667,3.73333333" +
                " C10.6666667,5.23733333 9.696,6.63466667 8.53333333,7.2" +
                " L8.53333333,5.96266667 C9.152,5.48266667 9.6,4.608" +
                " 9.6,3.73333333 C9.6,2.368 8.512,1.06666667" +
                " 7.46666667,1.06666667 L3.2,1.06666667" +
                " C2.15466667,1.06666667 1.06666667,2.368" +
                " 1.06666667,3.73333333 C1.06666667,5.09866667" +
                " 2.13333333,6.4 3.2,6.4 Z M12.8,3.2 L11.7333333,3.2" +
                " L11.7333333,4.26666667 L12.8,4.26666667" +
                " C13.8666667,4.26666667 14.9333333,5.568" +
                " 14.9333333,6.93333333 C14.9333333,8.29866667" +
                " 13.8453333,9.6 12.8,9.6 L8.53333333,9.6 C7.488,9.6" +
                " 6.4,8.29866667 6.4,6.93333333 C6.4,6.048 6.848,5.184" +
                " 7.46666667,4.704 L7.46666667,3.46666667 C6.304,4.032" +
                " 5.33333333,5.42933333 5.33333333,6.93333333" +
                " C5.33333333,8.864 6.98666667,10.6666667" +
                " 8.53333333,10.6666667 L12.8,10.6666667" +
                " C14.3466667,10.6666667 16,8.864 16,6.93333333" +
                " C16,5.00266667 14.4,3.2 12.8,3.2 Z id='Shape'></path>" +
                "</g> </g> </g> </g> </g> </g> </g> </g> </g> </svg>" +
                "</a> </div> </div>"


            newsdiv.prepend(news_text);
            // newsdiv.scrollTop(0);
        } else {
            console.log("Cannot handle feed!")
        }

    }

    // if joined the room or not
    function inWorld(worldId) {
        return $("#world-" + worldId).length > 0
    }

    // Room join/leave
    $("li.world-link").click(function () {
        worldId = $(this).attr("data-world-id")
        if (inWorld(worldId)) {
            // Leave world
            $(this).removeClass("joined")
            socket.send(JSON.stringify({
                "command": "leave",
                "world": worldId,
            }))
        } else {
            // Join world
            $(this).addClass("joined")
            socket.send(JSON.stringify({
                "command": "join",
                "world": worldId,
            }))
        }
    })


    $(".pane-header").click(function () {
        worldId = $(this).parent().attribute("id")
        $('#' + worldId + " .news").toggle()
    })


    // #####################################
    // #####################################
    // Publish news every 2 second
    // #####################################
    // #####################################

    function publishNews() {

        random_number = Math.floor(Math.random() * 21) + 1
        world_number = Math.floor(Math.random() * 4) + 1

        socket.send(JSON.stringify({
            "command": "send",
            "world": world_number,
            "News": json_data[random_number].News,
            "Time": json_data[random_number].Time,
        }))

    }

    window.setInterval(publishNews, 2000)

})