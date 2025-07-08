import os

def file_read(abs_path):
    try:
        with open(abs_path, 'r') as f:
            content = f.read()
        return {"success": True, "content": content}
    except Exception as e:
        return {"success": False, "error": str(e)}

def file_write_text(abs_path, content):
    try:
        with open(abs_path, 'w') as f:
            f.write(content)
        return {"success": True, "path": abs_path}
    except Exception as e:
        return {"success": False, "error": str(e)}

def file_append_text(abs_path, content):
    try:
        with open(abs_path, 'a') as f:
            f.write(content)
        return {"success": True, "path": abs_path}
    except Exception as e:
        return {"success": False, "error": str(e)}

def file_replace_text(abs_path, old_str, new_str):
    try:
        with open(abs_path, 'r') as f:
            content = f.read()
        if old_str not in content:
            return {"success": False, "error": f"'{old_str}' not found in file."}
        new_content = content.replace(old_str, new_str, 1) # Replace only the first occurrence
        with open(abs_path, 'w') as f:
            f.write(new_content)
        return {"success": True, "path": abs_path}
    except Exception as e:
        return {"success": False, "error": str(e)}

def message_notify_user(text, attachments=None):
    print(f"[User Notification]: {text}")
    if attachments:
        print(f"Attachments: {attachments}")
    return {"success": True, "message": "Notification sent."}


def shell_exec(command, session_id="default_session", working_dir="."):
    # This is a simplified mock-up. A real shell tool would interact with a sandbox shell.
    print(f"[Shell Exec] Session: {session_id}, Working Dir: {working_dir}, Command: {command}")
    try:
        # For demonstration, we'll just simulate a successful execution
        # In a real scenario, you'd use subprocess or similar
        result = os.popen(command).read()
        return {"success": True, "output": result}
    except Exception as e:
        return {"success": False, "error": str(e)}


