def multiple_choice(right_answer, given_answer):
    if given_answer is None:
        return 0
    if given_answer is right_answer:
        return 1
    if given_answer is not right_answer:
        return -0.2
