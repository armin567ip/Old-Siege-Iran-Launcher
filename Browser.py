import ctypes
import wmi
import webview
if __name__ == '__main__':
    webview.create_window('Old Siege',
                          'https://www.digikala.com/',
                          min_size=(1383, 800)
                          )
c=wmi.WMI()
def check_process_running(str_):
    if(c.Win32_Process(name=str_)):
        webview.start()

    else:
        ctypes.windll.user32.MessageBoxW(0, "! لطفا از طریق لانچر اقدام به ورود کنید", "خطا", 16)
check_process_running("Old Siege.exe") 
