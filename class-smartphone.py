# Smartphone class representing a mobile phone
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage} GB")
        print(f"Battery Life: {self.battery_life} hours")

    def make_call(self, number):
        print(f"Calling {number}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

# Inheritance layer: Let's create a specific type of Smartphone: "SmartphoneWithCamera"
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, storage, battery_life, camera_resolution):
        super().__init__(brand, model, storage, battery_life)
        self.camera_resolution = camera_resolution

    def take_photo(self):
        print(f"Taking a photo with {self.camera_resolution} MP camera")

# Create a smartphone object
phone = SmartphoneWithCamera("Apple", "iPhone 14", 128, 20, 12)
phone.display_info()
phone.make_call("123-456-7890")
phone.take_photo()

