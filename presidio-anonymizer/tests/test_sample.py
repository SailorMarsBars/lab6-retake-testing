import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer_anonymizes_correctly():
    # Setup inputs
    text = "My name is Bond."
    start = 11
    end = 15
    
    # Execute refactored function
    result = sample_run_anonymizer(text, start, end)
    
    # Assertions for text output
    assert result.text == "My name is BIP."
    
    # Assertions for items structure
    assert len(result.items) == 1
    item = result.items[0]
    
    assert item.start == 11
    assert item.end == 14
    assert item.entity_type == "PERSON"
    assert item.text == "BIP"
    assert item.operator == "replace"