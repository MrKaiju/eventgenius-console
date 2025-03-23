
class Atlas:
    def __init__(self):
        self.managers = {
            "Ops": ["Aura", "Pulse", "Guardian", "Echo"],
            "Tech": ["Forge", "Sage", "Proof"],
            "Research": ["Nova", "Loop", "Quanta", "Librus"]
        }
        self.direct_agents = ["Keystone", "Sentinel"]

    def route_command(self, command):
        objective = command.get("objective")
        if objective in ["UX", "Marketing", "Compliance", "Strategic"]:
            return "Manager Agent 1 (Ops)"
        elif objective in ["Engineering", "R&D Implementation", "QA"]:
            return "Manager Agent 2 (Tech)"
        elif objective in ["Research", "Finance", "Documentation"]:
            return "Manager Agent 3 (Research)"
        elif objective == "Architecture":
            return "Keystone"
        elif objective == "Security":
            return "Sentinel"
        else:
            return "Atlas - Manual Review"

    def get_agents_by_manager(self, manager_name):
        return self.managers.get(manager_name, [])

    def get_direct_reports(self):
        return self.direct_agents
