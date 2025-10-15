import frappe
from frappe import _
from frappe.defaults import set_user_default, get_user_default

THEME_KEY = "neolook_desk_theme"

@frappe.whitelist()
def save_desk_theme_preference(theme: str):
    user = frappe.session.user
    if not user or user == "Guest":
        frappe.throw(_("Login required"), frappe.PermissionError)
    if theme and not frappe.db.exists("Website Theme", theme):
        frappe.throw(_("Theme '{0}' not found").format(theme))
    set_user_default(THEME_KEY, theme or "")
    return {"ok": True}

@frappe.whitelist()
def get_desk_theme_preference():
    user = frappe.session.user
    if not user or user == "Guest":
        return {"theme": None}
    return {"theme": get_user_default(THEME_KEY)}
