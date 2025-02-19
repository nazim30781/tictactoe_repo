html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="">
            <input type="text" id="row" autocomplete="off"/>
            <input type="text" id="column" autocomplete="off"/>
            <button onclick="sendMessage(event)" type="button">Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            document.cookie = "start=0"
            var ws = new WebSocket("ws://localhost:8000/v1/game/3/room");
            var cookie = document.cookie

            data = {
                "cookie": cookie,
            };

            setTimeout(() => { ws.send(JSON.stringify(data)); }, 1000);

            ws.onmessage = function(event) {
                data = JSON.parse(event.data)
                console.log(data)
                if ("start" in data) {
                    document.cookie = `cell_value=${data["cell_value"]}`
                }

                if ("finish" in data) {
                    document.cookie = `win_value=${data["win_value"]}`
                }

                if ("move" in data) {
                    console.log(data)
                }
            };

            function sendMessage(event) {
                console.log("test")
                var row = document.getElementById("row").value
                var column = document.getElementById("column").value

                indexes_data = {
                    "cookie": document.cookie,
                    "row": row,
                    "column": column,
                };

                ws.send(JSON.stringify(indexes_data))
            }
        </script>
    </body>
</html>
"""
