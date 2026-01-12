# Application to estimate the CPU, GPU and RAM Energy consumption
# Sowparnika_02_06_2023

import psutil
import GPUtil
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import re

for i in range(10):
    cpu_usage = psutil.cpu_percent()
    mem_usage = psutil.virtual_memory().percent

    def get_gpu_power():
        try:
            output = subprocess.check_output(['nvidia-smi', '--query-gpu=power.draw', '--format=csv,noheader,nounits'])
            power = float(re.findall(r"\d+\.\d+", output.decode('utf-8'))[0])
            return power
        except (subprocess.CalledProcessError, IndexError):
            return None
    gpu_usage = get_gpu_power()    
    
    
    print(cpu_usage)
    print(mem_usage)
    print(gpu_usage)

    plt.scatter(i, cpu_usage, color = "red")
    plt.scatter(i, mem_usage, color = "blue")
    plt.scatter(i, gpu_usage, color = "green")
    plt.legend(["CPU", "Memory", "GPU"], loc ="lower right")
    plt.pause(0.05)

plt.show()
