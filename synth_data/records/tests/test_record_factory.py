from synth_data.records.record_factory import telephone_number_generator


def test_telephone_generator():
    generator = telephone_number_generator('###-###-####')

    assert next(generator) != next(generator)
    assert next(generator) != "###-###-####"
