from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer_anonymizes_correctly():
    # 1. Define inputs
    input_text = "My name is Bond."
    input_start = 11
    input_end = 15
    
    # 2. Call the refactored function (Fixes: Missing/incorrect call)
    result = sample_run_anonymizer(input_text, input_start, input_end)
    
    # 3. Assertions
    assert result.text == "My name is BIP."
    assert len(result.items) == 1
    
    # Access the anonymized item
    item = result.items[0]
    
    # Fixes: Missing/incorrect start and end asserts
    # The output 'start' should be 11
    assert item.start == 11
    
    # The output 'end' should be 14 (since 'BIP' is 3 chars long: 11, 12, 13)
    assert item.end == 14
    
    # Additional validation
    assert item.entity_type == "PERSON"
    assert item.text == "BIP"
    assert item.operator == "replace"