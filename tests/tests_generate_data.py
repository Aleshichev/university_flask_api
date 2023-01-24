import pytest

from handlers.generate_data import random_group, first_name, last_name, random_students, random_letter, random_naumber


@pytest.mark.parametrize("func, expected_result", [(random_group(), list),
                                                   (first_name(), list),
                                                   (last_name(), list),
                                                   (random_students(), list),
                                                   (random_letter(), str),
                                                   (random_naumber(), str)
                                                   ])

def test_random_group(func, expected_result):
    assert type(func) == expected_result


if __name__ == '__main__':
    pytest.main()
