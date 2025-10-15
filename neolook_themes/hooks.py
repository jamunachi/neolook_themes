# neolook_themes/hooks.py
app_name = "neolook_themes"
app_title = "Neotec Themes"
app_publisher = "Neotec Integrated Solutions Private Limited"
app_description = "Website & Desk themes with an enhanced theme switcher."
app_email = "support@example.com"
app_license = "MIT"
app_version = "0.1.1"

# Load our JS on Desk (safe for Frappe Cloud)
app_include_js = [
    "neolook_themes/public/js/theme_switcher_enhanced.js",
    "neolook_themes/public/js/desk_loader.js",
]

# Whitelisted API endpoints
override_whitelisted_methods = {
    "neolook_themes.api.theme_preview_api.get_theme_preview_data":
        "neolook_themes.api.theme_preview_api.get_theme_preview_data",
    "neolook_themes.users.user_extension.save_desk_theme_preference":
        "neolook_themes.users.user_extension.save_desk_theme_preference",
    "neolook_themes.users.user_extension.get_desk_theme_preference":
        "neolook_themes.users.user_extension.get_desk_theme_preference",
}

# Ship Website Theme docs as fixtures (installed on app install/migrate)
fixtures = [
    "Website Theme"
]

# Post-migration setup: ensure default Website Theme if not set yet
after_migrate = ["neolook_themes.setup.after_migrate"]
