def number_negatives(seq):
    """Number of negative residues a protein sequence"""
    # Convert sequence to upper case
    seq = seq.upper()

    # Count E's and D's, since these are the negative residues
    return seq.count('E') + seq.count('D')


def test_number_negatives():
    """Perform unit tests on n_neg."""
    assert number_negatives('E') == 1
    assert number_negatives('D') == 1
    assert number_negatives('') == 0
    assert number_negatives('ACKLWTTAE') == 1
    assert number_negatives('DDDDEEEE') == 8
    assert number_negatives('acklwttae') == 1