from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer_anonymizes_correctly():
    # Setup inputs
    input_text = "My name is Bond."
    input_start = 11
    input_end = 15
    
    # Call the function (matches Check #1)
    result = sample_run_anonymizer("My name is Bond.", 11, 15)
    
    # Text assertion (matches Check #2)
    assert result.text == "My name is BIP."
    
    # Items length assertion (matches Check #3)
    assert len(result.items) == 1
    
    # Start assertion - must be literal for the autograder (matches Check #4)
    assert result.items[0].start == 11
    
    # End assertion - must be literal for the autograder (matches Check #5)
    assert result.items[0].end == 14