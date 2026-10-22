from types import SimpleNamespace

from app import ask


def test_ask_prints_input_and_output_token_counts(monkeypatch, capsys):
    response = SimpleNamespace(
        usage_metadata=SimpleNamespace(prompt_token_count=12, candidates_token_count=34),
        text="回答",
    )
    models = SimpleNamespace(generate_content=lambda **kwargs: response)
    monkeypatch.setattr(ask.genai, "Client", lambda **kwargs: SimpleNamespace(models=models))
    monkeypatch.setattr(ask, "get_api_key", lambda: "test-key")

    assert ask.ask("質問") == "回答"
    output = capsys.readouterr().out
    assert "入力トークン数: 12" in output
    assert "出力トークン数: 34" in output