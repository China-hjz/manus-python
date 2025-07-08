from agent import Agent
from tool_registry import ToolRegistry
from task_planner import TaskPlanner
from context_manager import ContextManager
from tools import file_read, file_write_text, file_append_text, file_replace_text, message_notify_user, shell_exec

def main():
    # Initialize components
    tool_registry = ToolRegistry()
    task_planner = TaskPlanner()
    context_manager = ContextManager()

    # Register tools
    tool_registry.register_tool("file_read", file_read, "Read content from a file")
    tool_registry.register_tool("file_write_text", file_write_text, "Write text to a file")
    tool_registry.register_tool("file_append_text", file_append_text, "Append text to a file")
    tool_registry.register_tool("file_replace_text", file_replace_text, "Replace text in a file")
    tool_registry.register_tool("message_notify_user", message_notify_user, "Send a notification to the user")
    tool_registry.register_tool("shell_exec", shell_exec, "Execute a shell command")

    # Initialize agent
    agent = Agent(tool_registry)

    print("Manus Replica - AI Agent")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("\nUser: ")
        if user_input.lower() == 'exit':
            break
        
        print("\n--- Agent Processing ---")
        agent.run(user_input)
        print("--- Processing Complete ---")

if __name__ == "__main__":
    main()

