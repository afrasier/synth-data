from synth_data.records.generators import number_generator, date_generator


def test_number_generator():
    generator = number_generator('###-###-####')

    assert next(generator) != next(generator)
    assert next(generator) != "###-###-####"


def test_date_generator():
    generator = date_generator(range_start='1990-01-01T00:00:00Z', range_end='2000-01-01T00:00:00Z')

    assert next(generator) != next(generator)
