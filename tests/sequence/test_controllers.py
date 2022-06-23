import pytest

from alticci.sequence.controllers import retrieve_alticci_sequence_term


class TestAlticciSequenceTermController:
    def test_recursive_cases(self):
        terms = [i for i in range(3, 11)]
        values = []
        expected_values = [1, 2, 2, 3, 4, 5, 7, 9]

        for term in terms:
            value = retrieve_alticci_sequence_term(term)
            assert type(value) == int
            values.append(value)

        assert values == expected_values

    def test_base_cases(self):
        terms = [i for i in range(3)]
        values = []
        expected_values = [0, 1, 1]

        for term in terms:
            value = retrieve_alticci_sequence_term(term)
            assert type(value) == int
            values.append(value)

        assert values == expected_values

    def test_negative_cases(self):
        terms = [i for i in range(-1, -4, -1)]

        with pytest.raises(
            ValueError,
            match="Cannot calculate negative term value: "
        ):
            for term in terms:
                retrieve_alticci_sequence_term(term)
