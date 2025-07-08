import json

class Agent:
    def __init__(self, tool_registry):
        self.tool_registry = tool_registry
        self.context = []

    def run(self, initial_prompt):
        self.context.append({"role": "user", "content": initial_prompt})
        while True:
            # Simulate LLM thinking and tool selection
            # In a real scenario, this would involve an LLM call
            # For now, we'll hardcode a simple tool call for demonstration
            if len(self.context) == 1: # First turn
                tool_call = {
                    "tool_name": "message_notify_user",
                    "args": {"text": "Hello from Manus Replica!"}
                }
            else:
                # For subsequent turns, just end the loop for this simple demo
                print("Task completed for this demo.")
                break

            print(f"Agent thinking... Decided to call tool: {tool_call['tool_name']} with args: {tool_call['args']}")
            
            max_retries = 3
            for attempt in range(max_retries):
                observation = self.execute_tool_call(tool_call)
                if "error" not in json.loads(observation):
                    break
                print(f"Tool execution failed (attempt {attempt + 1}/{max_retries}): {observation}")
                if attempt == max_retries - 1:
                    print("Max retries reached. Aborting task.")
                    return

            self.context.append({"role": "tool_output", "content": observation})
            print(f"Observation: {observation}")

            # In a real scenario, the agent would analyze the observation
            # and decide the next step (another tool call or task completion)
            if tool_call['tool_name'] == 'message_notify_user':
                break # End after first message for demo

    def execute_tool_call(self, tool_call):
        tool_name = tool_call["tool_name"]
        args = tool_call["args"]
        if tool_name in self.tool_registry.tools:
            tool_func = self.tool_registry.tools[tool_name]["function"]
            try:
                result = tool_func(**args)
                return json.dumps(result) # Return JSON string of result
            except Exception as e:
                return json.dumps({"error": str(e)})
        else:
            return json.dumps({"error": f"Tool '{tool_name}' not found."})



