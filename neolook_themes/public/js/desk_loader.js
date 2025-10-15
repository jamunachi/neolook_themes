// Applies a CSS class on <body> based on saved preference.
frappe.ready(() => {
  try {
    if (!frappe.session || !frappe.session.user || frappe.session.user === "Guest") return;
    if (window.__neolook_desk_loaded__) return;
    window.__neolook_desk_loaded__ = true;

    frappe.call({
      method: "neolook_themes.users.user_extension.get_desk_theme_preference"
    }).then((r) => {
      const theme = r?.message?.theme;
      if (!theme) return;
      const cls = "neolook-theme-" + String(theme).trim().toLowerCase().replace(/\s+/g, "-");
      document.body.classList.add(cls);
    });
  } catch (e) {}
});
