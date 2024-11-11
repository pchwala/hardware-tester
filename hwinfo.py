import subprocess
import re



def exec_and_output(command):
    return subprocess.check_output(command, shell=True).decode().strip()


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
        """Gets hardware information from the system."""

        output = subprocess.check_output(['system_profiler', 'SPHardwareDataType'])
        output = output.decode().split('\n')
        for line in output:
            if "Serial Number" in line:
                self.serial = line.split(':')[1].strip()

            elif "Model Identifier" in line:
                self.model = line.split(':')[1].strip()
                if "MacBook" in self.model:
                    self.manufacturer = "Apple"

            elif "Processor Name" in line:
                self.CPU_model = line.split(':')[1].strip()

            elif "Processor Speed" in line:
                self.CPU_model += " " + line.split(':')[1].strip()

            elif "Memory" in line:
                self.RAM_value = line.split(':')[1].strip()


        HDDs = []
        output = subprocess.check_output(['system_profiler', 'SPStorageDataType'])
        output = output.decode().split('\n\n')
        for section in output:
            output_section = section.split('\n')
            temp_name = ""
            temp_value = ""
            temp_type = ""
            for line in output_section:
                if "Capacity" in line:
                    temp_value = re.search(r"\d+.\d+ GB", line).group(0)

                elif "Device Name" in line:
                    temp_name = line.split(':')[1].strip()

                elif "Medium Type" in line:
                    temp_type = line.split(':')[1].strip()

                elif "Internal: Yes" in line:
                    hdd_value = temp_value + ' | ' + temp_type + ' | ' + temp_name
                    HDDs.append(hdd_value)

        HDDs = list(set(HDDs))
        try:
            self.HDD1_value = HDDs[0]
            self.HDD2_value = HDDs[1]
        except IndexError:
            print("There is none or only one HDD")


        output = subprocess.check_output(['system_profiler', 'SPDisplaysDataType'])
        output = output.decode().split('\n')
        for line in output:
            if "Chipset Model" in line:
                self.GPU_model = line.split(':')[1].strip()

            elif "Resolution" in line:
                self.resolution = re.search(r"\d+ x \d+", line).group(0)

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
