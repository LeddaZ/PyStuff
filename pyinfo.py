# PyInfo
# Python script to get system information

# Import modules
import platform
import psutil

print("==============")
print("=== PyInfo ===")
print("==============")
print()

# Get OS name, release and architecture
os_name=platform.uname()[0]
os_rel=platform.uname()[2]
os_arch=platform.architecture()[0]

# Print build number if OS is Windows
if os_name == "Windows":
    win_build=platform.uname()[3]
    print("Operating system: " + os_name + " " + os_rel + " " + os_arch + " (build " + win_build + ")")
else:
    print("Operating system: " + os_name + " " + os_rel + " " + os_arch)

# Print Python version
py_ver=platform.python_version()
print("Python version: " + py_ver)

