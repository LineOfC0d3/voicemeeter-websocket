using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

///responses according to VoiceMeeterRemote.h
namespace VoiceMeeterWebsocket.VoiceMeeterWrapper.Enums
{
    public enum LoginResponse
    {
        OK = 0,
        OkVoicemeeterNotRunning = 1,
        NoClient = -1,
        AlreadyLoggedIn = -2,
    }
}
