(function () {
  const menuLabel = __("Desk Theme");

  const ensureMenu = () => {
    const userMenu = frappe.app && frappe.app.user ? frappe.app.user : null;
    if (!userMenu || !userMenu.build_user_menu) return;

    const original = userMenu.build_user_menu.bind(userMenu);
    userMenu.build_user_menu = function () {
      const menu = original();
      const $menu = $(menu);

      const item = $(`<li class="user-action">
        <a class="grey-link" href="javascript:void(0)">${menuLabel}</a>
      </li>`);

      item.on("click", async () => {
        const r = await frappe.call({
          method: "neolook_themes.api.theme_preview_api.get_theme_preview_data"
        });
        const opts = (r?.message?.available || []).sort();
        const d = new frappe.ui.Dialog({
          title: __("Choose Desk Theme"),
          fields: [
            { fieldname: "theme", label: __("Theme"), fieldtype: "Select", options: opts.join("\n") }
          ],
          primary_action_label: __("Apply")
        });
        d.set_values({ theme: opts[0] || "" });
        d.set_primary_action(async (values) => {
          await frappe.call({
            method: "neolook_themes.users.user_extension.save_desk_theme_preference",
            args: { theme: values.theme || "" }
          });
          frappe.show_alert({ message: __("Theme preference saved. Reloading…"), indicator: "green" });
          setTimeout(() => window.location.reload(), 500);
        });
        d.show();
      });

      if (!$menu.find(`a:contains("${menuLabel}")`).length) {
        $menu.find("li.user-action:contains('Preferences')").first().after(item);
      }
      return menu;
    };
  };

  if (document.readyState !== "loading") ensureMenu();
  else document.addEventListener("DOMContentLoaded", ensureMenu);
})();
