from channels import include


# Display text of the received message
def message_handler(message):
    print(message['text'])


channel_routing = [
    include("NewsHub.routing.websocket_routing", path=r"^/news/stream"),
    include("NewsHub.routing.custom_routing"),
]
