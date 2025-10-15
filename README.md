# Neotec Themes (`neolook_themes`)

**Neotec-branded theme pack** for Frappe v14+ and Frappe Cloud (FC-safe).  
Provides 8 ready-to-use Website Themes and a **Desk theme switcher** with per-user preference.

---

## ✨ Features
- 8 Neotec themes (Website Themes shipped via fixtures)
- Per-user Desk theme preference (saved as User Default)
- User menu **Desk Theme** picker
- Auto-apply theme on Desk via lightweight JS (no core patches)
- FC-friendly install (valid `pyproject.toml`, assets under `public/`)

**Themes included**
- Neo Classic Light
- Neo Corporate Blue *(default website theme after install, if none set)*
- Neo Ocean Blue Desk
- Neo Graphite
- Neo Classic Dark
- Neo Night Indigo
- Neo Desert Sand Light
- Neo High Contrast Pro

---

## ✅ Compatibility
- **Frappe v14+** (tested on v14 and v15 stacks)
- ERPNext optional (not required)
- Frappe Cloud compatible

---

## 🧩 How it works
- Website themes are installed from `fixtures/website_theme.json`.
- A small JS loader (`public/js/desk_loader.js`) applies a CSS class on `<body>`
  based on the user’s chosen Desk theme.
- A user-menu entry (`theme_switcher_enhanced.js`) lets users pick a theme.
- A post-migrate hook sets **Website Settings → Website Theme** to **Neo Corporate Blue**
  **only if** none is configured yet (safe & idempotent).

---

## 🚀 Installation

### Frappe Cloud (recommended)
1. Push this repo to GitHub (public or private).
2. In your FC site → **Apps → Install from Git** → paste the repo URL.
3. After app install: **Build Assets → Migrate → Clear Cache**.

### Local / Bench
```bash
# get the app
bench get-app https://github.com/<your-org>/neolook_themes.git

# install on your site
bench --site your.site.name install-app neolook_themes

# finalize
bench --site your.site.name migrate
bench build
bench clear-cache
```

---

## 🎛️ Usage

### Set the site’s Website Theme
- After install, if your site had no theme set, the app sets **Neo Corporate Blue** automatically.
- To change: **Website → Website Theme** → pick/set your default.

### Switch Desk theme per user
- Click your **user avatar → Desk Theme**.
- Choose one of the **Neo** themes.
- The page reloads and applies it (adds a class like `neolook-theme-neo-corporate-blue` on `<body>`).

### Add or customize themes
1. Copy an existing entry in `neolook_themes/fixtures/website_theme.json`.
2. Adjust `theme_scss` (you can add variables, fonts, etc.).
3. Commit and deploy.
4. Run `bench --site your.site.name migrate` to apply fixtures.
5. (Optional) Provide per-theme Desk CSS and load it by extending `desk_loader.js`
   to inject a `<link>` to `/assets/neolook_themes/css/<theme>.css`.

---

## 🧪 Troubleshooting

- **“Not a valid Frappe App! …”** → Ensure `pyproject.toml` exists at repo root and is valid.
- **Themes didn’t appear** → Make sure `fixtures/website_theme.json` is committed; run `bench migrate`.
- **User menu item missing** → Rebuild and clear cache: `bench build && bench clear-cache`.
- **Website theme unchanged** → Open **Website Settings** and pick a theme manually.

---

## 📄 License
MIT © Neotec Integrated Solutions Private Limited

---

## 🆘 Support
- Issues & feature requests: GitHub Issues on your repo
- Commercial support: Neotec Integrated Solutions Private Limited — support@example.com
