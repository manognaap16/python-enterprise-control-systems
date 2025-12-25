import json
from pathlib import Path


class PolicyEvaluator:
    def __init__(self, policy_file_path):
        self.policies = self._load_policies(policy_file_path)

    def _load_policies(self, path):
        with open(path, "r") as file:
            return json.load(file)

    def evaluate(self, context):
        """
        context example:
        {
            "cpu_usage": 85,
            "user_role": "user"
        }
        """
        matched_policies = []

        for policy in self.policies:
            if self._check_condition(policy["condition"], context):
                matched_policies.append(policy)

        if not matched_policies:
            return {
                "decision": "ALLOW",
                "reason": "No policy violations"
            }

        # Resolve conflicts using priority (lower number = higher priority)
        matched_policies.sort(key=lambda x: x["priority"])
        selected_policy = matched_policies[0]

        return {
            "decision": selected_policy["action"],
            "reason": selected_policy["description"],
            "policy_id": selected_policy["policy_id"]
        }

    def _check_condition(self, condition, context):
        for key, value in condition.items():
            if key == "cpu_usage_gt":
                if context.get("cpu_usage", 0) <= value:
                    return False
            elif key == "user_role_not":
                if context.get("user_role") == value:
                    return False
            elif key == "user_role_is":
                if context.get("user_role") != value:
                    return False
        return True
