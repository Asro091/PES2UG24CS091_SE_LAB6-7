import pytest
from traffic_fine import speeding_fine, license_action, total_penalty


class TestSpeedingFineBranchCoverage:
    def test_no_speeding_below_limit(self):
        # Branch: speed < limit -> returns 0
        assert speeding_fine(50, 60, "city") == 0

    def test_no_speeding_exact_limit_boundary(self):
        # Branch: speed == limit -> returns 0
        assert speeding_fine(60, 60, "school") == 0

    def test_school_zone_excess_over_40(self):
        # Branches: zone == "school", excess > 40
        assert speeding_fine(100, 50, "school") == 6000

    def test_highway_zone_excess_between_20_and_40(self):
        # Branches: zone != "school", zone == "highway", excess > 20 (and <= 40)
        assert speeding_fine(75, 50, "highway") == 2000

    def test_highway_zone_excess_exact_40_boundary(self):
        # Branch boundary: excess == 40 (not > 40, but > 20)
        assert speeding_fine(90, 50, "highway") == 2000

    def test_highway_zone_excess_exact_20_boundary(self):
        # Branch boundary: excess == 20 (not > 20, returns base)
        assert speeding_fine(70, 50, "highway") == 1000

    def test_default_zone_excess_under_20(self):
        # Branches: zone != "school", zone != "highway" (else), excess <= 20
        assert speeding_fine(65, 50, "residential") == 500


class TestLicenseActionBranchCoverage:
    def test_points_ge_12_commercial_true(self):
        # Branches: points >= 12 (True), is_commercial (True) -> "revoke"
        assert license_action(12, True, False) == "revoke"

    def test_points_ge_12_commercial_false(self):
        # Branches: points >= 12 (True), is_commercial (False) -> "suspend"
        assert license_action(12, False, False) == "suspend"

    def test_points_ge_8_repeat_offender_true(self):
        # Branches: points >= 12 (False), points >= 8 (True), repeat_offender (True) -> "suspend"
        assert license_action(8, False, True) == "suspend"

    def test_points_ge_8_repeat_offender_false(self):
        # Branches: points >= 12 (False), points >= 8 (True), repeat_offender (False) -> "warning"
        assert license_action(8, False, False) == "warning"

    def test_points_ge_4(self):
        # Branches: points >= 12 (False), points >= 8 (False), points >= 4 (True) -> "notice"
        assert license_action(4, False, False) == "notice"

    def test_points_lt_4(self):
        # Branches: points >= 12 (False), points >= 8 (False), points >= 4 (False) -> "none"
        assert license_action(3, False, False) == "none"


class TestTotalPenaltyBranchCoverage:
    def test_empty_fines_list(self):
        # Branch: for loop over empty sequence (0 iterations)
        assert total_penalty([]) == 0

    def test_total_penalty_strictly_below_limit(self):
        # Branches: loop with items, fine >= 0, total <= 10000 (False branch of total > 10000)
        assert total_penalty([1000, 2500, 1500]) == 5000

    def test_total_penalty_exact_limit_boundary(self):
        # Boundary: total == 10000 (total > 10000 evaluates to False)
        assert total_penalty([4000, 6000]) == 10000

    def test_total_penalty_exceeding_limit_capped(self):
        # Branch: total > 10000 (True) -> capped to 10000
        assert total_penalty([6000, 5000]) == 10000

    def test_negative_fine_raises_value_error(self):
        # Branch: fine < 0 (True) -> raises ValueError
        with pytest.raises(ValueError, match="negative fine"):
            total_penalty([500, -100, 200])
