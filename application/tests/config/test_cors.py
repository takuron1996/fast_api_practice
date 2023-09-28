"""mainのテスト."""
from pytest_bdd import scenarios

scenarios(
    "../features/config/cors.feature",
)
