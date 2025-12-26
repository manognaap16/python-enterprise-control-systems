class RiskAnalyzer:
    def evaluate(self, metrics: dict):
        """
        metrics example:
        {
            "total_tasks": 10,
            "failed_tasks": 3
        }
        """
        total_tasks = metrics.get("total_tasks", 0)
        failed_tasks = metrics.get("failed_tasks", 0)

        if total_tasks == 0:
            return {
                "risk_score": 1.0,
                "reason": "No execution data available"
            }

        failure_ratio = failed_tasks / total_tasks
        risk_score = min(1.0, failure_ratio)

        return {
            "risk_score": round(risk_score, 2),
            "reason": "Risk based on task failure ratio"
        }
