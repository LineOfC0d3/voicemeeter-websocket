# voicemeeter-websocket
A Websocket API for VoiceMeeter.

**This project is _WIP_**

### Basic idea
This API will make it possible to control any version of [VoiceMeeter](https://vb-audio.com/Voicemeeter/) over a Websocket Connection.
Websockets allows the API to make callbacks when values change.

With this API VoiceMeeter could be controlled from any applications that supports Websocket-Connections (i.e. [Bitfocus Companion](https://github.com/bitfocus/companion)).
This also makes it possible to control VoiceMeeter instances on other PCs with VoiceMeeter installed and this API running.

### Requirements
Any Version of VoiceMeeter [Standard](https://vb-audio.com/Voicemeeter/)/[Banana](https://vb-audio.com/Voicemeeter/banana.htm)/[Potato](https://vb-audio.com/Voicemeeter/potato.htm)

[Python](https://www.python.org/downloads/)

#### External Packages
[Python Wrapper for Voicemeeter API](https://github.com/onyx-and-iris/voicemeeter-api-python)

[Websockets](https://github.com/aaugustin/websockets)

### JSON Configuration
The full JSON structure the websocket is capable of understanding or sending. Just sending or expecting parts will work.

Plase keep in mind that some features are only available in certain VoiceMeeter Editions (e.g. Gainlayers are only available on VoiceMeeter Potato)

(For value limitations see [VoiceMeeter Remote API documentation](https://download.vb-audio.com/Download_CABLE/VoicemeeterRemoteAPI.pdf))


```jsonc
{
  "strip":
  {
    "0":
    {
      "mono": true,
      "solo": true,
      "mute": true,
      "gain": 0.0,
      "gain_layer":
      {
        "0": 0.0,
        //...
      },
      "comp": 0.0,
      "gate": 0.0,
      "audibility": 0,
      "limit": 0,
      "a1": true,
      "a2": true,
      "a3": true,
      "a4": true,
      "a5": true,
      "b1": true,
      "b2": true,
      "b3": true,
      "label": "test",
      "mc": true,
      "k": 1,
      "bass": 0.0,
      "mid": 0.0,
			"fx_1": 0,
			"fx_2": 0,
      "pan_x": 0.0,
      "pan_y": 0.0,
      "color_x": 0.0,
      "color_y": 0.0,
      "fx_x": 0.0,
      "fx_y": 0.0,
			"post_reverb": true,
			"post_delay": true,
			"post_fx_1": true,
			"post_fx_2": true,
      "denoiser": 0, //not supported by wrapper
			"fade_to":
			{
				"target": 0,
				"time_ms": 1000
			},
      "fade_by":
			{
				"relative_change": 5,
				"time_ms": 1000
			},
			"app":
			{
				"spotify":
				{
					"gain": 0,
					"mute": true
				}
			},
      "levels":
      {
        "pre_fader": 0,
        "post_fader": 0,
        "post_mute": 0
      },
      "eq_virtual":
      {
        "treble": 0.0,
        "reverb": 0,
        "delay": 0,
      },
      "eq_physical": //not supported by wrapper
      {
        "active": true,
        "memory_slot": "A",
        "0": //channel index
        {
          "0": //cell index
          {
            "active": true,
            "type": 1,
            "frequency": 20000,
            "gain": 0.0,
            "quality": 50,
          }
          //...
        }
        //...
      },
      "device":
      {
        "name": "", //read only
        "sr": "", //read only
        "wdm": "Microphone", //write only
        "ks": "Microphone", //write only
        "mme": "Microphone", //write only
        "asio": "Microphone", //write only
      }
    }
    //...
  },
  "bus":
  {
    "0":
    {
      "mono": true,
      "eq": true,
      "eq_memory": "A",
      "mute": true,
      "sel": true,
      "gain": 0.0,
      "label": "testLabel",
      "return_reverb": 0.0,
      "return_delay": 0.0,
      "return_fx1": 0.0,
      "return_fx2": 0.0,
      "monitor": false,
      "fade_to":
	    {
	    	"target": 0,
	    	"time_ms": 1000
	    },
      "fade_by":
	    {
	    	"relative_change": 5,
	    	"time_ms": 1000
	    },
      "mode": "normal",
      "device":
      {
        "name": "", //read only
        "sr": "", //read only
        "wdm": "Microphone", //write only
        "ks": "Microphone", //write only
        "mme": "Microphone", //write only
        "asio": "Microphone", //write only
      }
    },
    //...
  },
  "macrobutton":
  {
    "0":
    {
      "state": true,
      "stateonly": true,
      "trigger": true,
    }
    //...
  },
  "recorder":
  {
    "command": "play", //commands like "play", "stop", "pause", "record", "ff", "rew"
    "load": "<filepath>", //write only
    "loop": true,
    "a1": true,
    "a2": true,
    "a3": true,
    "a4": true,
    "a5": true,
    "b1": true,
    "b2": true,
    "b3": true,
  },
  "option":
  {
    "sample_rate": 48000,
    "asio_sr": true,
    "monitor_on_sel": true,
    "buffer":
    {
      "mme": 512,
      "wdm": 512,
      "ks": 512,
      "asio": 512
    },
    "delay":
    {
      "0": 0, //bus index
      //...
    }
  },
  "patch":
  {
    "post_fx_insert": true,
    "post_fader_composite": true,
    "asio":
    {
      "0": 0 //valid range determined by connected device
      //... from 0 to 10
    },
    "a2":
    {
      "0": 0 //valid range determined by connected device
      //... from 0 to 8
    },
    "a3":
    {
      "0": 0 //valid range determined by connected device
      //... from 0 to 8
    },
    "a4":
    {
      "0": 0 //valid range determined by connected device
      //... from 0 to 8
    },
    "a5":
    {
      "0": 0 //valid range determined by connected device
      //... from 0 to 8
    },
    "composite":
    {
      "0": 0 //valid range depending on version
      //... from 0 to 8
    },
    "insert":
    {
      "0": true
      //... from 0 to number of channels depending on version
    }
  },
  "command": "" //commands like "show", "shutdown", "restart" and "reset" are available
}
```
TODO: allow toggle for boolean values

### Development
Developed with Python 3.11
