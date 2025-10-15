import frappe

DEFAULT_THEME = "Neo Corporate Blue"

def after_migrate():
    """Ensure Website Theme fixtures exist and set a default Website Theme
    if none is configured yet. Safe on FC and idempotent.
    """
    try:
        # Ensure our default theme exists (fixtures should have created it)
        if not frappe.db.exists("Website Theme", DEFAULT_THEME):
            return

        ws = frappe.get_single("Website Settings")
        if not getattr(ws, "website_theme", None):
            ws.website_theme = DEFAULT_THEME
            ws.flags.ignore_permissions = True
            ws.save()
            frappe.db.commit()
    except Exception:
        # Silent fail — we don't want to break migrations for a missing optional doctype
        frappe.log_error("neolook_themes.after_migrate failed (non-fatal)")
