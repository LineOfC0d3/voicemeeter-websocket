using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace VoiceMeeterWebsocket
{
    public static class Constants
    {
        public const string RegUnInstallDirKey = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall";
        public const string InstallerUnInstKey = "VB:Voicemeeter {17359A74-1236-5467}";
        //public const string VoicemeeterRemoteDll = "VoicemeeterRemote.dll"; //currently unused because I have no idea how to change the constants if OS is not 64bit
        public const string VoicemeeterRemoteDll64 = "VoicemeeterRemote64.dll";
    }
}
