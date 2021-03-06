import json

hmi_data = [
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

obu_data = [
    {
        "version": 1,
        "timestamp_ms": 1234567,
        "id": 1,
        "lat": 123,
        "lon": 1234,
        "type": "BUS",
        "role": "PUBLIC_TRANSPORT",
        "heading": 30,
        "speed": 130,
        "events": [
            {
                "orig_sta_id": 100,
                "seq_num": 300,
                "term_flag": False,
                "cause_code": "ACCIDENT",
                "sub_cause_code": 13,
                "ttc_ms": 321,
                "lat": 111,
                "lon": 112
            },
            {
                "orig_sta_id": 1001,
                "seq_num": 3001,
                "term_flag": True,
                "cause_code": "SLOW_VEHICLE",
                "sub_cause_code": 131,
                "ttc_ms": 3211,
                "lat": 1111,
                "lon": 1121
            }
        ]
    },
    {
        "version": 2,
        "timestamp_ms": 7654321,
        "id": 2,
        "lat": 321,
        "lon": 4321,
        "type": "MOPED",
        "role": "TAXI",
        "heading": 60,
        "speed": 100,
        "events": [
            {
                "orig_sta_id": 1001,
                "seq_num": 3001,
                "term_flag": False,
                "cause_code": "POST_CRASH",
                "sub_cause_code": 131,
                "ttc_ms": 3211,
                "lat": 1111,
                "lon": 1112
            },
            {
                "orig_sta_id": 10011,
                "seq_num": 30011,
                "term_flag": False,
                "cause_code": "WRONG_WAY_DRIVING",
                "sub_cause_code": 1311,
                "ttc_ms": 32111,
                "lat": 11111,
                "lon": 11211
            }
        ]
    }
]


with open("hmi_data_file.json", "w") as write_file:
    json.dump(hmi_data, write_file)

with open("obu_data_file.json", "w") as write_file:
    json.dump(obu_data, write_file)
