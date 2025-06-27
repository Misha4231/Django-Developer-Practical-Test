from django.conf import settings

def settings_context(request):
    unsafe_keys = ["SECRET_KEY", "DATABASES"]
    # get all settings except unsafe keys
    safe_settings = {k: v for k, v in settings._wrapped.__dict__.items() if k not in unsafe_keys}

    return {'SETTINGS': safe_settings}