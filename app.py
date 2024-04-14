import os

def openApp(app_name):
    # Split the PATH variable into a list of directories
    path_dirs = os.environ["PATH"].split(os.pathsep)

    # Search for the app in each directory in the PATH
    for path_dir in path_dirs:
        # Construct the full path to the app executable
        app_path = os.path.join(path_dir, app_name + ".exe")

        # Check if the app exists at the constructed path
        if os.path.exists(app_path):
            # If found, try to open the app
            try:
                os.startfile(app_path)
                print(f"Opened {app_name} successfully.")
                return
            except OSError as e:
                print(f"Error: {e}")
                return

    # If the app is not found in any directory in the PATH
    print(f"Could not find {app_name} in PATH.")


    # If the app is not found
    print(f"Could not find {app_name}.")
