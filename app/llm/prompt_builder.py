def build_rating_prompt(
    teaching_rating: float,
    learning_rating: float
) -> str:

    prompt = f"""

You are an AI training evaluator.

A DM is teaching a reporter.

DM teaching rating: {teaching_rating}/10
Reporter learning rating: {learning_rating}/10

Evaluate the training efficiency.

Return JSON ONLY.

Example:

{{
 "efficiency_score": 8.5,
 "feedback": "DM teaches clearly and reporter demonstrates strong understanding."
}}

Rules:
- Score between 1 and 10
- Provide concise feedback
"""

    return prompt