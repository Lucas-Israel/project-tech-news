from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
import pytest
from unittest.mock import patch

mock_return = [
    {
        "title": "abc",
        "reading_time": 5,
    },
    {
        "title": "def",
        "reading_time": 9,
    },
    {
        "title": "aaa",
        "reading_time": 22,
    },
]

expected_return = {
    "readable": [{"chosen_news": [("abc", 5)], "unfilled_time": 3}],
    "unreadable": [("def", 9), ("aaa", 22)],
}


def test_reading_plan_group_news():
    reading_plan = ReadingPlanService
    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        reading_plan.group_news_for_available_time(0)

    with patch.object(
        reading_plan, "_db_news_proxy", return_value=mock_return
    ):
        data = reading_plan.group_news_for_available_time(8)
        # print(data)

        assert data == expected_return
