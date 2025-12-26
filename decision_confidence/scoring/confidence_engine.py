from data_quality.quality_checker import DataQualityChecker
from risk.risk_analyzer import RiskAnalyzer


class ConfidenceEngine:
    def __init__(self):
        self.quality_checker = DataQualityChecker()
        self.risk_analyzer = RiskAnalyzer()

    def evaluate(self, data_quality_input: dict, risk_input: dict):
        quality_result = self.quality_checker.evaluate(data_quality_input)
        risk_result = self.risk_analyzer.evaluate(risk_input)

        quality_score = quality_result["quality_score"]
        risk_score = risk_result["risk_score"]

        # Confidence is high when quality is high and risk is low
        confidence = quality_score * (1 - risk_score)

        explanation = (
            f"Confidence derived from data quality ({quality_score}) "
            f"and risk level ({risk_score})."
        )

        return {
            "confidence_score": round(confidence * 100, 2),
            "quality_score": quality_score,
            "risk_score": risk_score,
            "explanation": explanation
        }
