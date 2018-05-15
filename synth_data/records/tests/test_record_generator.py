from synth_data.records.generators import number_generator


def test_number_generator():
    generator = number_generator('###-###-####')

    assert next(generator) != next(generator)
    assert next(generator) != "###-###-####"
