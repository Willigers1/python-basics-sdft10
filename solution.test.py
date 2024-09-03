def test_handles_N_zero(self):
        from solution import MatchingCouples
        result = MatchingCouples([0, 0, 0])
        assert result == 1  # 1 way to choose 0 items from 0 items