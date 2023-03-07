import json


# LOL bisschen rumspielen. (Keine Sorge, das wird noch besser und schöner)
class VoiceMeeterController:
    def __init__(self, remote):
        self.remote = remote

    def control_strip(self, data):
        for strip_id in data:
            for action in data[strip_id]:
                value = data[strip_id][action]
                match action:
                    case "mono":
                        self.remote.strip[int(strip_id)].mono = value
                        break
                    case "solo":
                        self.remote.strip[int(strip_id)].solo = value

    def control_bus(self, data):
        print("LOL")

    def control_macrobutton(self, data):
        print("LOL")

    def control_recorder(self, data):
        print("LOL")

    def control_option(self, data):
        print("LOL")

    def control_patch(self, data):
        print("LOL")

    def control_command(self, data):
        print("LOL")

    def interpret_json(self, data: str) -> str:
        try:
            json_message = json.loads(data)
            for prim_key in json_message:
                match prim_key:
                    case "strip":
                        self.control_strip(json_message[prim_key])
                        break
                    case "bus":
                        self.control_bus(json_message[prim_key])
                        break
                    case "macrobutton":
                        self.control_macrobutton(json_message[prim_key])
                        break
                    case "recorder":
                        self.control_recorder(json_message[prim_key])
                        break
                    case "option":
                        self.control_option(json_message[prim_key])
                        break
                    case "patch":
                        self.control_patch(json_message[prim_key])
                        break
                    case "command":
                        self.control_command(json_message[prim_key])
                        break

        except ValueError:
            return "please provide valid JSON"
