# Dynamic Resource Monitoring Framework

This Python application continuously monitors **CPU**, **GPU**, and **RAM** usage and estimates their energy consumption. It visualizes real-time data in a scatter plot for easy monitoring of system resource consumption.

---

## 🚀 Features

- Monitors **CPU usage (%)** using `psutil`.
- Monitors **RAM usage (%)** using `psutil`.
- Monitors **GPU power consumption (W)** using `nvidia-smi` and `subprocess`.
- Provides a **real-time scatter plot** of CPU, RAM, and GPU consumption.
- Lightweight and easy to extend for additional metrics or visualization features.

---
## How It Works

The **Dynamic Resource Monitoring Framework** continuously monitors system resources and visualizes energy consumption:

### 1. Continuous Monitoring Loop
The script runs in a loop (currently 10 iterations, extendable) to periodically capture resource usage data in near real-time.

### 2. CPU & RAM Monitoring
- Uses **`psutil`** to fetch:
  - **CPU usage (%)**
  - **Memory usage (%)**

### 3. GPU Monitoring
- Uses **`nvidia-smi`** via **`subprocess`** to query GPU power draw in **watts**.
- Returns `None` if GPU is not available or the query fails.

### 4. Visualization
- Each iteration updates a **scatter plot** displaying resource usage:
  - **Red dots:** CPU usage  
  - **Blue dots:** Memory usage  
  - **Green dots:** GPU power consumption

### 5. Plot Display
- After all iterations, the final plot is displayed with **legends**, allowing a visual comparison of CPU, RAM, and GPU consumption over time.
