import platform
import psutil
import speedtest
import socket
import wmi

def get_installed_software():
    software_list = []
    for software in psutil.disk_partitions():
        software_list.append(software.device)
    return software_list

def get_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  # Convert to Mbps
    upload_speed = st.upload() / 10**6  # Convert to Mbps
    return download_speed, upload_speed

def get_screen_resolution():
    screen_info = platform.uname()
    return screen_info

def get_cpu_info():
    cpu_info = platform.processor()
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)
    return cpu_info, cpu_cores, cpu_threads

def get_gpu_info():
    try:
        w = wmi.WMI()
        gpu_info = w.Win32_VideoController()[0].Caption
    except Exception as e:
        gpu_info = "Not available"
    return gpu_info

def get_ram_size():
    ram_info = psutil.virtual_memory().total // (1024**3)  # Convert to GB
    return ram_info

def get_screen_size():
    screen_size = platform.system()  # You can use additional libraries for more details
    return screen_size

def get_network_info():
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])
    public_ip = socket.gethostbyname(socket.gethostname())
    return mac_address, public_ip

def get_windows_version():
    windows_version = platform.version()
    return windows_version

if __name__ == "__main__":
    installed_software = get_installed_software()
    internet_speed = get_internet_speed()
    screen_resolution = get_screen_resolution()
    cpu_info, cpu_cores, cpu_threads = get_cpu_info()
    gpu_info = get_gpu_info()
    ram_size = get_ram_size()
    screen_size = get_screen_size()
    mac_address, public_ip = get_network_info()
    windows_version = get_windows_version()

    print("1. Installed Software List:", installed_software)
    print("2. Internet Speed (Download, Upload) in Mbps:", internet_speed)
    print("3. Screen Resolution:", screen_resolution)
    print("4. CPU Model:", cpu_info)
    print("5. Number of CPU Cores:", cpu_cores)
    print("   Number of CPU Threads:", cpu_threads)
    print("6. GPU Model:", gpu_info)
    print("7. RAM Size (in GB):", ram_size)
    print("8. Screen Size:", screen_size)
    print("9. Wifi/Ethernet MAC Address:", mac_address)
    print("10. Public IP Address:", public_ip)
    print("11. Windows Version:", windows_version)
