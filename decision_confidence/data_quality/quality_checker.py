class DataQualityChecker:
    def evaluate(self, data: dict):
        """
        data example:
        {
            "records": 100,
            "missing_values": 5
        }
        """
        total_records = data.get("records", 0)
        missing_values = data.get("missing_values", 0)

        if total_records == 0:
            return {
                "quality_score": 0.0,
                "reason": "No data available"
            }

        missing_ratio = missing_values / total_records
        quality_score = max(0.0, 1.0 - missing_ratio)

        return {
            "quality_score": round(quality_score, 2),
            "reason": "Quality based on missing data ratio"
        }
