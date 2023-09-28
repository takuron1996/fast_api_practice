#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""テストで共通のfixture."""

from fastapi.testclient import TestClient
from pytest_bdd import given, parsers, then, when

from main import app


@given("テスト用のクライアントを生成", target_fixture="client")
def client():
    """テスト用のクライアントを生成."""
    return TestClient(app)

@given(parsers.parse("エンドポイントに{url}を設定"), target_fixture="url")
def endpoint_url(url):
    """endpointを設定."""
    return url

@given(parsers.parse("ヘッダーの{key}に{value}を設定"),
       target_fixture="headers")
def set_headers(key, value):
    """ヘッダーを設定."""
    return {key: value}

@given(parsers.parse("ヘッダーの{key}に{value}を追加"),
       target_fixture="headers")
def add_headers(headers, key, value):
    """ヘッダーに追加."""
    headers.update({key: value})
    return headers

@when("optionsを実行", target_fixture="response")
def run_options(client, url, headers):
    """optionsを実行."""
    return client.options(url, headers=headers)

@then(parsers.parse("ステータスコードが{code}"),converters={"code": int})
def status_code(response, code):
    """ステータスコードの検証."""
    assert response.status_code == code

@then(parsers.parse("ヘッダーの{key}に{value}が設定されていること"))
def cors_header(response, key, value):
    """CORSヘッダーの検証."""
    assert response.headers[key] == value

@then(parsers.parse("ヘッダーに{key}が設定されていないこと"))
def not_cors_header(response, key):
    """CORSヘッダーの検証."""
    assert  key not in response.headers
