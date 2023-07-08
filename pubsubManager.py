from pubsub import pub


# from pubsub import pub

# def callback(message):
#     print(f"Received message: {message}")

# pub.subscribe(callback, 'test_topic')
# pub.sendMessage('test_topic', message='Hello')

# # If you see "Received message: Hello" printed, it indicates that the `pubsub` package is functioning correctly.

class PubSubManager:
    pub_dict = {}

    @classmethod
    def subscribe(cls, signal_name, callback):
        if signal_name not in cls.pub_dict:
            pub_object = pub
            cls.pub_dict[signal_name] = pub_object
        else:
            pub_object = cls.pub_dict[signal_name]
        pub_object.subscribe(callback, signal_name)

    @classmethod
    def send_message(cls, signal_name, **kwargs):
        if signal_name in cls.pub_dict:
            pub_object = cls.pub_dict[signal_name]
            pub_object.sendMessage(signal_name, **kwargs)
        else:
            print(f"No subscribers found for signal: {signal_name}")

if __name__ == "__main__":
    # Example usage
    def callback1(message):
        print(f"Callback 1 received message: {message}")

    def callback2(message):
        print(f"Callback 2 received message: {message}")

    PubSubManager.subscribe("signal1", callback1)
    PubSubManager.send_message("signal1", message =  "Hello subscribers!")
