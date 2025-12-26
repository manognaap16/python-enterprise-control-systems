from scoring.confidence_engine import ConfidenceEngine


def main():
    engine = ConfidenceEngine()

    # Sample inputs
    data_quality_input = {
        "records": 120,
        "missing_values": 10
    }

    risk_input = {
        "total_tasks": 20,
        "failed_tasks": 4
    }

    result = engine.evaluate(data_quality_input, risk_input)

    print("Decision Confidence Result")
    print("--------------------------")
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
