class TaskPlanner:
    def __init__(self):
        self.current_plan = None

    def create_plan(self, goal, phases):
        self.current_plan = {
            "goal": goal,
            "phases": phases,
            "current_phase_id": 1
        }
        return self.current_plan

    def advance_phase(self):
        if self.current_plan and self.current_plan["current_phase_id"] < len(self.current_plan["phases"]):
            self.current_plan["current_phase_id"] += 1
            return True
        return False

    def get_current_phase(self):
        if self.current_plan:
            return self.current_plan["phases"][self.current_plan["current_phase_id"] - 1]
        return None

    def get_current_plan(self):
        return self.current_plan


