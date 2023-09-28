Feature: プリフライトリクエストを用いてCORSの設定をテスト
    Background:
        Given テスト用のクライアントを生成

    Scenario Outline: CORSに設定されているパスがアクセス可能なことをテスト
        Given エンドポイントに/を設定
        And ヘッダーのOriginに<url>を設定
        And ヘッダーのAccess-Control-Request-MethodにGETを追加
        When optionsを実行
        Then ステータスコードが200
        And ヘッダーのaccess-control-allow-originに<url>が設定されていること

        Examples:
            | url |
            | http://allowed.origin.com |

    Scenario Outline: CORSに設定されてないパスがアクセス不可能なことをテスト
        Given エンドポイントに/を設定
        And ヘッダーのOriginにhttp://disallowed.origin.comを設定
        And ヘッダーのAccess-Control-Request-MethodにGETを追加
        When optionsを実行
        Then ステータスコードが400
        And ヘッダーにaccess-control-allow-originが設定されていないこと
