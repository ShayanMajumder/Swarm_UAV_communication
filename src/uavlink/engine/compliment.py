def compliment(factor):
    if factor > 1:
        raise ValueError("Factor must be less than 1")
    return 1 - factor