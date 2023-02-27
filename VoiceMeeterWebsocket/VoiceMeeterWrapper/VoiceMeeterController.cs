using Microsoft.Win32;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using VoiceMeeterWebsocket;
using VoiceMeeterWebsocket.VoiceMeeterWrapper.Enums;

namespace VoiceMeeterWebsocket.VoiceMeeterWrapper
{
    public class VoiceMeeterController
    {
        public LoginResponse LoginResponse { get; private set; }

        public VoiceMeeterController()
        {
            string? voiceMeeterDllPath = FindVoiceMeeterDllPath();
            if(voiceMeeterDllPath != null)
            {
                VoiceMeeterRemote.LoadDll(Path.Combine(voiceMeeterDllPath, Constants.VoicemeeterRemoteDll64));
                LoginResponse = VoiceMeeterRemote.Login();
            }
        }

        private string? FindVoiceMeeterDllPath()
        {
            using (RegistryKey? key = Registry.LocalMachine.OpenSubKey($"{Constants.RegUnInstallDirKey}\\{Constants.InstallerUnInstKey}"))
            {
                if (key != null)
                {
                    object? keyValue = key.GetValue("UninstallString", null);
                    if (keyValue != null)
                    {
                        return Path.GetDirectoryName(keyValue.ToString());
                    }
                }
            }

            return null;
        }
    }
}
