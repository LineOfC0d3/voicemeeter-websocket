using Microsoft.Win32;
using System.Runtime.InteropServices;
using VoiceMeeterWebsocket.VoiceMeeterWrapper.Enums;

namespace VoiceMeeterWebsocket.VoiceMeeterWrapper
{
    public static class VoiceMeeterRemote
    {
        [DllImport(Constants.VoicemeeterRemoteDll64, EntryPoint = "VBVMR_Login")]
        public static extern LoginResponse Login();
        [DllImport(Constants.VoicemeeterRemoteDll64, EntryPoint = "VBVMR_Logout")]
        public static extern LoginResponse Logout();

        [DllImport("kernel32.dll")]
        private static extern IntPtr LoadLibrary(string dllToLoad);
        private static IntPtr? _dllHandle;
        public static void LoadDll(string dllPath)
        {
            if (!_dllHandle.HasValue)
            {
                _dllHandle = LoadLibrary(dllPath);
            }
        }
    }
}