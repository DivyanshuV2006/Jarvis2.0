from speak import speak

def openApp(user_input):
    file_path = "C:\\executable_files.txt"
    try:
        with open(file_path, "r") as file:
            executable_paths = file.readlines()
    except FileNotFoundError:
        speak(f"Error: {file_path} not found.")
        return

    user_input = user_input.lower() + ".exe"

    found = False
    for path in executable_paths:
        if path.lower().strip().endswith(user_input):
            found = True
            try:
                import subprocess
                subprocess.Popen(path.strip())
                print(path.strip())
                speak(f"Opening {user_input}...")
            except Exception as e:
                speak(f"Error opening {user_input}: {e}")
            break

    if not found:
        speak(f"Application '{user_input}' not found in {file_path}.")
