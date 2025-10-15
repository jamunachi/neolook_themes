import frappe
from frappe import _

@frappe.whitelist()
def get_theme_preview_data(theme_name: str | None = None):
    if not frappe.has_permission("Website Theme", "read"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)

    if theme_name:
        theme = frappe.get_doc("Website Theme", theme_name)
        return {
            "name": theme.name,
            "theme_scss": getattr(theme, "theme_scss", None),
            "custom_scss": getattr(theme, "custom_scss", None),
        }

    names = frappe.get_all("Website Theme", pluck="name")
    return {"available": names}
