import psutil

# Get a list of all running processes
process_list = psutil.process_iter()

# Iterate through the list of processes and print their names
for process in process_list:
    try:
        process_info = process.as_dict(attrs=['pid', 'name'])
        print(
            f"Process ID: {process_info['pid']}, Process Name: {process_info['name']}")
    except psutil.NoSuchProcess:
        # Handle the case where a process no longer exists
        pass
