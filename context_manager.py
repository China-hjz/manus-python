class ContextManager:
    def __init__(self):
        self.context = []

    def add_message(self, role, content):
        self.context.append({"role": role, "content": content})

    def get_context(self):
        return self.context

    def clear_context(self):
        self.context = []


