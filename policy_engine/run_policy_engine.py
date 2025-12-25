from evaluator.policy_evaluator import PolicyEvaluator

policy_file = "rules/policies.json"

engine = PolicyEvaluator(policy_file)

test_context = {
    "cpu_usage": 90,
    "user_role": "user"
}

result = engine.evaluate(test_context)
print(result)
