import json
from datetime import datetime
from pathlib import Path


class AuditLogger:
    def __init__(self, log_file="audit_log.json"):
        self.log_file = Path(log_file)
        self._ensure_log_file()

    def _ensure_log_file(self):
        if not self.log_file.exists():
            with open(self.log_file, "w") as file:
                json.dump([], file)

    def log_decision(self, context, decision_result):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "context": context,
            "decision": decision_result
        }

        with open(self.log_file, "r+") as file:
            data = json.load(file)
            data.append(entry)
            file.seek(0)
            json.dump(data, file, indent=2)
