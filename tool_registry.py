class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register_tool(self, name, function, description):
        self.tools[name] = {
            "function": function,
            "description": description
        }

    def get_tool(self, name):
        return self.tools.get(name)


