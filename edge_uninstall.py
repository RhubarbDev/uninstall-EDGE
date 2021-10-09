import winreg
import os

def get_edge_version():
    keypath = r"Software\Microsoft\Edge\BLBeacon"
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, keypath, 0, winreg.KEY_READ)
    return winreg.QueryValueEx(key, "version")[0]

def del_edge(path):
    os.chdir(path)
    os.system(f"start cmd /K setup.exe --uninstall --system-level --verbose-logging --force-uninstall")

version = get_edge_version()
edge_path = f"C:/Program Files (x86)/Microsoft/Edge/Application/{version}/Installer"
del_edge(edge_path)
