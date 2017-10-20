from channels import route
from NewsHub.consumers import ws_connect, ws_disconnect, ws_receive, \
    world_join, world_leave, news_publish

websocket_routing = [
    route("websocket.connect", ws_connect),
    route("websocket.disconnect", ws_disconnect),
    route("websocket.receive", ws_receive),
]

custom_routing = [
    route("NewsHub.receive", world_join, command="^join$"),
    route("NewsHub.receive", world_leave, command="^leave$"),
    route("NewsHub.receive", news_publish, command="^send$"),
]
