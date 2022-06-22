def retrieve_alticci_term(term: int) -> int:
    if term < 0:
        raise ValueError(f"Cannot calculate negative term value: {term}")
    elif term == 0:
        return 0
    elif term in [1, 2]:
        return 1

    value = retrieve_alticci_term(term-3) + retrieve_alticci_term(term-2)

    return value
