from mycroft import MycroftSkill, intent_file_handler


class DeviceController(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('controller.device.intent')
    def handle_controller_device(self, message):
        self.speak_dialog('controller.device')


def create_skill():
    return DeviceController()

