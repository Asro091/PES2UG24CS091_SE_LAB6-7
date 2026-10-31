import pytest
from traffic_fine import speeding_fine, license_action, total_penalty


class TestSpeedingFineLineCoverage:
    def test_no_speeding(self):
        # Covers speed <= limit (lines 2-3)
        assert speeding_fine(50, 60, "city") == 0

    def test_school_zone_excess_over_40(self):
        # Covers zone == "school" and excess > 40 (lines 4-6, 11-12)
        assert speeding_fine(100, 50, "school") == 6000

    def test_highway_zone_excess_between_20_and_40(self):
        # Covers zone == "highway" and excess > 20 (lines 7-8, 13-14)
        assert speeding_fine(75, 50, "highway") == 2000

    def test_default_zone_excess_under_20(self):
        # Covers else zone and base return (lines 9-10, 15)
        assert speeding_fine(65, 50, "residential") == 500


class TestLicenseActionLineCoverage:
    def test_commercial_license_revoked(self):
        # Covers points >= 12 and is_commercial=True (lines 19-21)
        assert license_action(15, True, False) == "revoke"

    def test_non_commercial_license_suspended(self):
        # Covers points >= 12 and is_commercial=False (line 22)
        assert license_action(14, False, False) == "suspend"

    def test_repeat_offender_suspended(self):
        # Covers points >= 8 and repeat_offender=True (lines 23-25)
        assert license_action(10, False, True) == "suspend"

    def test_first_time_offender_warning(self):
        # Covers points >= 8 and repeat_offender=False (line 26)
        assert license_action(9, False, False) == "warning"

    def test_points_notice(self):
        # Covers points >= 4 (lines 27-28)
        assert license_action(6, False, False) == "notice"

    def test_clean_record_none(self):
        # Covers points < 4 (line 29)
        assert license_action(2, False, False) == "none"


class TestTotalPenaltyLineCoverage:
    def test_total_penalty_capped(self):
        # Covers loop, addition, cap > 10000, and return (lines 33-35, 37-40)
        assert total_penalty([6000, 5000]) == 10000

    def test_negative_fine_raises_error(self):
        # Covers fine < 0 raising ValueError (lines 35-36)
        with pytest.raises(ValueError, match="negative fine"):
            total_penalty([500, -100])
