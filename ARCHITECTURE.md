# Architecture

## Overview
This repository is a Hugo-based static website for the "Satoshi's Plebs Podcast". Content lives as Markdown in `content/`, templates and logic live in `layouts/`, and static assets (CSS, images, JS) live in `static/`. The site is configured by `hugo.yaml` and built by Hugo into a static output directory (typically `public/`).

## Main entry points
- `hugo.yaml`: Site configuration (base URL, menus, taxonomies, rendering settings).
- `content/_index.md`: Home page content (title/description/body).
- `layouts/index.html`: Home page template.
- `layouts/_default/baseof.html`: Global page wrapper that injects head/header/footer partials and renders the main block.
- `layouts/episodes/list.html`: Episodes list page (search + pagination UI).
- `layouts/episodes/single.html`: Episode detail page (metadata, player, transcript, tags).
- `layouts/log/single.html`: Log post detail page.
- `layouts/partials/*.html`: Shared template fragments (head, header, footer, player, episode footer).
- `static/css/style.css`: Site styling.

## Data flow
1. Hugo reads `hugo.yaml` to configure the site (menus, taxonomies, base URL).
2. Markdown content in `content/` is parsed into pages with front matter (e.g., `episode`, `podhome_id`, `btc_price_usd`).
3. Hugo selects a layout based on section/type:
   - Home: `layouts/index.html`
   - Episodes list: `layouts/episodes/list.html`
   - Episode single: `layouts/episodes/single.html`
   - Log single: `layouts/log/single.html`
   - Fallbacks: `layouts/_default/*.html`
4. Layouts render content and metadata, pull in partials, and emit static HTML. The episodes list template also injects client-side JS for search and pagination.
5. Static assets from `static/` are copied verbatim into the build output.

## Where to add features
- New site-wide layout changes: `layouts/_default/baseof.html` or `layouts/partials/*.html`.
- New section types (e.g., "Guests", "Resources"): add `content/<section>/` plus `layouts/<section>/list.html` and `layouts/<section>/single.html`.
- New homepage sections: `layouts/index.html` (and associated styles in `static/css/style.css`).
- New styling or UI behaviors: `static/css/style.css` and, for page-specific JS, inline scripts in the relevant layout or a new file under `static/`.
- New content fields: update front matter in `content/` files and read them in templates (e.g., `.Params.<field>` in the relevant layout).
- New shortcodes: add to `layouts/shortcodes/` and reference from Markdown content.
