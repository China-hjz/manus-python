import json
import time
from agent import Agent
from tool_registry import ToolRegistry
from task_planner import TaskPlanner
from context_manager import ContextManager
from tools import file_read, file_write_text, file_append_text, file_replace_text, message_notify_user, shell_exec

class WebAgent:
    def __init__(self):
        # Initialize components
        self.tool_registry = ToolRegistry()
        self.task_planner = TaskPlanner()
        self.context_manager = ContextManager()
        
        # Register tools
        self.tool_registry.register_tool("file_read", file_read, "Read content from a file")
        self.tool_registry.register_tool("file_write_text", file_write_text, "Write text to a file")
        self.tool_registry.register_tool("file_append_text", file_append_text, "Append text to a file")
        self.tool_registry.register_tool("file_replace_text", file_replace_text, "Replace text in a file")
        self.tool_registry.register_tool("message_notify_user", message_notify_user, "Send a notification to the user")
        self.tool_registry.register_tool("shell_exec", shell_exec, "Execute a shell command")
        
        # Initialize agent
        self.agent = Agent(self.tool_registry)
        
    def process_message(self, user_message):
        """Process a user message and return the agent's response"""
        try:
            # Add user message to context
            self.context_manager.add_message("user", user_message)
            
            # Simulate agent thinking and tool selection
            # In a real scenario, this would involve an LLM call
            response_text = f"Manus Replica 已收到您的消息: '{user_message}'"
            
            # Simulate some processing time
            time.sleep(1)
            
            # Determine what tool to call based on the message
            if "文件" in user_message or "file" in user_message.lower():
                tool_call = {
                    "tool_name": "file_write_text",
                    "args": {
                        "abs_path": "/tmp/test_output.txt",
                        "content": f"用户请求: {user_message}\n处理时间: {time.strftime('%Y-%m-%d %H:%M:%S')}"
                    }
                }
                response_text += "\n\n我已经为您创建了一个测试文件。"
            elif "命令" in user_message or "shell" in user_message.lower():
                tool_call = {
                    "tool_name": "shell_exec",
                    "args": {
                        "command": "echo 'Hello from Manus Replica Shell!'",
                        "session_id": "web_session",
                        "working_dir": "/tmp"
                    }
                }
                response_text += "\n\n我已经执行了一个测试命令。"
            else:
                tool_call = {
                    "tool_name": "message_notify_user",
                    "args": {"text": response_text}
                }
            
            # Execute the tool call
            observation = self.agent.execute_tool_call(tool_call)
            observation_data = json.loads(observation)
            
            # Add tool execution result to context
            self.context_manager.add_message("tool_output", observation)
            
            # Generate final response
            if observation_data.get("success"):
                response_text += f"\n\n✅ 工具执行成功: {tool_call['tool_name']}"
                if "output" in observation_data:
                    response_text += f"\n输出: {observation_data['output']}"
            else:
                response_text += f"\n\n❌ 工具执行失败: {observation_data.get('error', '未知错误')}"
            
            return {
                "success": True,
                "response": response_text,
                "tool_used": tool_call['tool_name'],
                "context_length": len(self.context_manager.get_context())
            }
            
        except Exception as e:
            return {
                "success": False,
                "response": f"处理消息时发生错误: {str(e)}",
                "error": str(e)
            }
    
    def get_status(self):
        """Get the current status of the agent"""
        return {
            "tools_available": len(self.tool_registry.tools),
            "context_length": len(self.context_manager.get_context()),
            "available_tools": list(self.tool_registry.tools.keys())
        }

