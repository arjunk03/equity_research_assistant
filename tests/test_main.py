import pytest

from equitty_research_assistant import main


def test_main_prints_greeting(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert "equitty-research-assistant" in captured.out
