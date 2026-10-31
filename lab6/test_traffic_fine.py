import pytest
from traffic_fine import speeding_fine, license_action, total_penalty


# --- Speeding Fine Tests ---

def test_no_speeding_below_limit():
    assert speeding_fine(50, 60, "city") == 0


def test_no_speeding_exact_limit_boundary():
    assert speeding_fine(60, 60, "school") == 0


def test_school_zone_excess_over_40():
    assert speeding_fine(100, 50, "school") == 6000


def test_highway_zone_excess_between_20_and_40():
    assert speeding_fine(75, 50, "highway") == 2000


def test_highway_zone_excess_exact_40_boundary():
    assert speeding_fine(90, 50, "highway") == 2000


def test_highway_zone_excess_exact_20_boundary():
    assert speeding_fine(70, 50, "highway") == 1000


def test_default_zone_excess_under_20():
    assert speeding_fine(65, 50, "residential") == 500


# --- License Action Tests ---

def test_clean_record():
    assert license_action(2, False, False) == "none"


def test_points_notice():
    assert license_action(4, False, False) == "notice"


def test_points_warning():
    assert license_action(8, False, False) == "warning"


def test_repeat_offender_suspend():
    assert license_action(8, False, True) == "suspend"


def test_points_ge_12_non_commercial_suspend():
    assert license_action(12, False, False) == "suspend"


def test_points_ge_12_commercial_revoke():
    assert license_action(12, True, False) == "revoke"


# --- Total Penalty Tests ---

def test_empty_fines():
    assert total_penalty([]) == 0


def test_total_penalty_strictly_below_limit():
    assert total_penalty([1000, 2500, 1500]) == 5000


def test_total_penalty_exact_limit_boundary():
    assert total_penalty([4000, 6000]) == 10000


def test_total_penalty_exceeding_limit_capped():
    assert total_penalty([6000, 5000]) == 10000


def test_negative_fine_raises_value_error():
    with pytest.raises(ValueError, match="negative fine"):
        total_penalty([500, -100, 200])
