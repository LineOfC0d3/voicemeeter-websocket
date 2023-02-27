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

### External Packages
[Python Wrapper for Voicemeeter API](https://github.com/onyx-and-iris/voicemeeter-api-python)

### Development
Developed with Python 3.11
