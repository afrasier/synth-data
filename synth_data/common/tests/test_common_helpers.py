from synth_data.common.common_helpers import format_seconds


def test_format_seconds():
    assert format_seconds(59) == "0 d 0 h 0 m 59 s"
    assert format_seconds(60) == "0 d 0 h 1 m 0 s"
    assert format_seconds(3600) == "0 d 1 h 0 m 0 s"
    assert format_seconds(3600 * 24) == "1 d 0 h 0 m 0 s"

    assert format_seconds(60 + 1) == "0 d 0 h 1 m 1 s"
    assert format_seconds(3600 + 1) == "0 d 1 h 0 m 1 s"
    assert format_seconds(3600 * 24 + 1) == "1 d 0 h 0 m 1 s"
