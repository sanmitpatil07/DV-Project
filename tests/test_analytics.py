from config.settings import settings

def test_analytics_settings():
    assert settings.PROJECT_NAME == "Global Superstore Analytics"
    assert settings.TARGET_PROFIT_MARGIN == 0.15
