import seq_features

def test_number_negatives_single_E_or_D():
    """Perform unit tests on number_negative for single AA"""
    assert seq_features.number_negatives('E') == 1
    assert seq_features.number_negatives('D') == 1


def test_number_negatives_for_empty():
    """Perform unit tests on number_negative for empty entry"""
    assert seq_features.number_negatives('') == 0


def test_number_negatives_for_short_sequences():
    """Perform unit tests on number_negative for short sequence"""
    assert seq_features.number_negatives('ACKLWTTAE') == 1
    assert seq_features.number_negatives('DDDDEEEE') == 8


def test_number_negatives_for_lowercase():
    """Perform unit tests on number_negative for lowercase"""
    assert seq_features.number_negatives('acklwttae') == 1