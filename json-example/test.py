import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

data = [
    {
        "low_beam_headlight_on": True,
        "high_beam_headlight_on": True,
        "left_turn_signal_on": True,
        "right_turn_signal_on": True,
        "daytime_running_lights_on": True,
        "reverse_light_on": True,
        "fog_light_on": True,
        "parking_light_on": True,
        "light_bar_activated": True,
        "siren_activated": True
    },
    {
        "low_beam_headlight_on": False,
        "high_beam_headlight_on": False,
        "left_turn_signal_on": False,
        "right_turn_signal_on": False,
        "daytime_running_lights_on": False,
        "reverse_light_on": False,
        "fog_light_on": False,
        "parking_light_on": False,
        "light_bar_activated": False,
        "siren_activated": False
    }
]


with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)