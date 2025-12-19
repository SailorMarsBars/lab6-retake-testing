from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def sample_run_anonymizer(text: str, start: int, end: int):
    """
    Refactored function that takes parameters and returns the result 
    for better testability.
    """
    # Initialize the engine
    engine = AnonymizerEngine()

    # Invoke the anonymize function with the provided parameters
    result = engine.anonymize(
        text=text,
        analyzer_results=[
            RecognizerResult(entity_type="PERSON", start=start, end=end, score=0.8)
        ],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})}
    )

    return result

if __name__ == "__main__":
    # 1. Collect inputs (or hardcode them for the sample run)
    user_text = "My name is Bond."
    user_start = 11
    user_end = 15

    # 2. Call the refactored function and save the result to a variable
    anonymized_result = sample_run_anonymizer(user_text, user_start, user_end)

    # 3. Print the result to match the required output format
    print(anonymized_result)