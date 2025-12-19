from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def sample_run_anonymizer(text: str, start: int, end: int):
    # Initialize the engine
    engine = AnonymizerEngine()

    # Invoke the anonymize function with parameters 
    # and return the result for testing
    result = engine.anonymize(
        text=text,
        analyzer_results=[
            RecognizerResult(entity_type="PERSON", start=start, end=end, score=0.8)
        ],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})}
    )
    return result

if __name__ == "__main__": 
    # Use parameters for easy testing/running
    # Result is saved to a variable as required
    final_result = sample_run_anonymizer(text="My name is Bond.", start=11, end=15)
    
    # Print the saved variable
    print(final_result)