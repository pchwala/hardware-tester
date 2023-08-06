import subprocess
import re

# I didn't have time to properly comment out the code for these functions
# but basically what all of these do is they take output of certain linux commands that return hardware info,
# and format it in a way that is user-friendly and easy to work with and manipulate


def exec_and_output(command):
    return subprocess.check_output(command, shell=True).decode().strip()


def get_disk_info(device):
    command = "sudo smartctl -i " + device
    all_info = subprocess.check_output(command, shell=True).decode().strip()
    disk = ""
    model = ""

    if "nvm" in device:
        for line in all_info.split("\n"):
            if "Total" in line:
                temp = re.sub(r".*\[", "", line, 1)
                disk += re.search(r"\d+ \w+", temp).group(0)
                disk += " | NVMe"

            if "Model" in line:
                model += re.sub(r"Model Number:\s*", "", line, 1)

        if model != "":
            disk += " | "
            disk += model

    else:
        for line in all_info.split("\n"):
            if "Capacity" in line:
                temp = re.sub(r".*\[", "", line, 1)
                disk += re.search(r"\d* \w*", temp).group(0)
                disk += " | "

            if "Rotation Rate" in line:
                match = re.search(r"\d", line)
                if match:
                    disk += "HDD"
                else:
                    disk += "SSD"

            if "Form Factor" in line:
                disk += " | "
                disk += re.sub(r".*Form Factor:\s*", "", line, 1)

            if "Device Model" in line:
                model += re.sub(r".*Device Model:\s*", "", line, 1)

        if model != "":
            disk += " | "
            disk += model

    print(disk)
    return disk


class HwInfo:
    def __init__(self):

        self.serial = ""
        self.manufacturer = ""
        self.model = ""
        self.CPU_model = ""
        self.RAM_value = ""
        self.HDD1_value = ""
        self.HDD2_value = ""
        self.GPU_model = ""
        self.battery_health = ""
        self.battery0 = ""
        self.battery1 = ""
        self.monitor_size = ""
        self.resolution = ""
        self.license = ""

    def read_hardware_info(self):
        all_info = exec_and_output('sudo dmidecode | grep -A 9 "System Information"')
        for line in all_info.split("\n"):
            if "Manufacturer" in line:
                self.manufacturer = re.sub(".*Manufacturer.*: ", "", line, 1)

            elif "Product Name" in line:
                self.model += re.sub(".*Product Name.*: ", "", line, 1)

            elif "Version" in line:
                self.model += " (" + re.sub(".*Version.*: ", "", line, 1) + ")"

            elif "Serial Number" in line:
                self.serial = re.sub(".*Serial Number.*: ", "", line, 1)

        disk_devices = []
        all_info = exec_and_output("sudo smartctl --scan")
        for line in all_info.split("\n"):
            temp = re.split(r'\s', line, 1)
            if '/dev' in temp[0]:
                disk_devices.append(temp[0])

        if len(disk_devices) > 0:
            self.HDD1_value = get_disk_info(disk_devices[0])
        if len(disk_devices) > 1:
            self.HDD2_value = get_disk_info(disk_devices[1])

        all_info = exec_and_output("sudo lshw -short")
        for line in all_info.split("\n"):
            if "System Memory" in line:
                self.RAM_value = re.search(r'\d*G', line).group(0) + "B"
                self.RAM_value = re.sub(r'GB', " GB", self.RAM_value, 1)

            if "processor" in line:
                temp = re.sub(r".*processor\s*", "", line, 1)
                try:
                    self.CPU_model = re.search(r"i\d.*", temp).group(0)

                except AttributeError:
                    self.CPU_model = temp

            if "display" in line:
                temp = re.sub(r".*display\s*", "", line, 1)
                # FORMATTING ERRORS CHECK FOR AMD GPUs
                temp = re.sub(r".*\[", "", temp, 1)
                temp = re.sub(r"]", "", temp, 1)

                if self.GPU_model == "":
                    self.GPU_model += temp
                else:
                    self.GPU_model += " || " + temp

        all_info = exec_and_output("xdpyinfo | grep dimensions")
        self.resolution = re.search(r"\d+x\d+", all_info).group(0)
        if "1920x1080" in self.resolution:
            self.monitor_size = "FHD"
        elif "1366x768" in self.resolution:
            self.monitor_size = "HD"
        elif "2560x1440" in self.resolution:
            self.monitor_size = "QHD"

        command = "sudo hexdump -s 56 -e '" + '/29 "%s\n"' + "' /sys/firmware/acpi/tables/MSDM"
        try:
            all_info = exec_and_output(command)
            self.license = all_info
        except Exception:
            self.license = "brak licencji"

        all_info = exec_and_output('acpi -bi')
        for line in all_info.split("\n"):
            if "Battery 0" in line:
                if "capacity" in line:
                    self.battery0 = re.search(r'\d*%', line).group(0)

            if "Battery 1" in line:
                if "capacity" in line:
                    try:
                        self.battery1 = re.search(r'\d*%', line).group(0)
                    except Exception:
                        self.battery1 = "XD"

        if (self.battery0 != "") and (self.battery1 != ""):
            self.battery_health = self.battery0 + "/" + self.battery1

        elif (self.battery0 != "") or (self.battery1 != ""):
            self.battery_health = self.battery0 + self.battery1

        else:
            self.battery_health = "brak"

    def save_to_file(self):

        with open("hwinfo.dat", 'w') as file:

            file.write(self.serial + '\n')
            file.write(self.manufacturer + '\n')
            file.write(self.model + '\n')
            file.write(self.CPU_model + '\n')
            file.write(self.HDD1_value + '\n')
            file.write(self.HDD2_value + '\n')
            file.write(self.RAM_value + '\n')
            file.write(self.GPU_model + '\n')
            file.write(self.battery_health + '\n')
            file.write(self.resolution + '\n')
            file.write(self.monitor_size + '\n')
            file.write(self.license + '\n')

        result = subprocess.run("chmod 666 hwinfo.dat", shell=True)


hwinfo = HwInfo()

hwinfo.read_hardware_info()
hwinfo.save_to_file()
