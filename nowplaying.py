import pywintypes
import win32gui
import win32process
import psutil


def gethwndsforpid(pid):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                hwnds.append(hwnd)
        return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds


def getspwindowtext():
    for PID in win32process.EnumProcesses():
        if "Spotify" in psutil.Process(PID).name():
            if gethwndsforpid(PID):
                hwnd = gethwndsforpid(PID)[0]
                windowText = win32gui.GetWindowText(hwnd)
                return windowText


def artist():
    try:
        temp = getspwindowtext()
        artist = temp.split(" - ")[0]
        return artist
    except:
        return "ERROR: Can't Get Artist Info"


def song():
    try:
        temp = getspwindowtext()
        song = temp.split(" - ")[1]
        return song
    except:
        return "ERROR: Can't Get Song Info"
