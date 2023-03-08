import json


# LOL bisschen rumspielen. (Keine Sorge, das wird noch besser und schöner)
class VoiceMeeterController:
    def __init__(self, remote):
        self.remote = remote

    def control_strip(self, data) -> int:
        executed_actions = 0
        simple_attributes = {"mono", "solo", "mute", "gain", "comp", "gate", "audibility", "limit",
                             "A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "label", "mc",
                             "reverb", "delay", "fx1", "fx2", "pan_x", "pan_y", "color_x", "color_y",
                             "fx_x", "fx_y", "postreverb", "postdelay", "postfx1", "postfx2"}
        for key in data:
            strip_id = int(key)
            for action in data[key]:
                active_strip = self.remote.strip[strip_id]
                if action in simple_attributes:
                    setattr(active_strip, action, data[key][action])
                    executed_actions += 1
                else:
                    match action:
                        case "gain_layer":
                            for target in data[key][action]:
                                bus_id = int(target)
                                value = data[key][action][target]
                                active_strip.gainlayer[bus_id].gain = value
                                executed_actions += 1
                        case "fade_to":
                            amount = data[key][action]["target"]
                            time = data[key][action]["time_ms"]
                            active_strip.fadeto(amount, time)
                            executed_actions += 1
                        case "fade_by":
                            amount = data[key][action]["relative_change"]
                            time = data[key][action]["time_ms"]
                            active_strip.fadeto(amount, time)
                            executed_actions += 1
                        case "app":
                            for application in data[key][action]:
                                gain = data[key][action][application]["gain"]
                                if gain is not None:
                                    active_strip.appgain(application, gain)
                                    executed_actions += 1
                                mute = data[key][action][application]["mute"]
                                if mute is not None:
                                    active_strip.appmute(application, mute)
                                    executed_actions += 1
                        # case "levels":
                        #    for level_setting in data[key][action]:
                        #        setattr(active_strip.levels, level_setting, data[key][action][level_setting])
                        #        executed_actions += 1
                        case "eq_virtual":
                            for eq_setting in data[key][action]:
                                setattr(active_strip, eq_setting, data[key][action][eq_setting])
                                executed_actions += 1
                        case "eq_physical":
                            # TODO: implement manually or wait for wrapper to update
                            print("eq_physical not implemented")
                        case "device":
                            for device_setting in data[key][action]:
                                if device_setting not in ("name", "sr"):
                                    setattr(active_strip.device, device_setting, data[key][action][device_setting])
                                    executed_actions += 1
        return executed_actions

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
                    case "bus":
                        self.control_bus(json_message[prim_key])
                    case "macrobutton":
                        self.control_macrobutton(json_message[prim_key])
                    case "recorder":
                        self.control_recorder(json_message[prim_key])
                    case "option":
                        self.control_option(json_message[prim_key])
                    case "patch":
                        self.control_patch(json_message[prim_key])
                    case "command":
                        self.control_command(json_message[prim_key])

        except ValueError:
            return "please provide valid JSON"
