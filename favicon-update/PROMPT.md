# Starting prompt for Claude Code

Paste the text below as your first message, with this folder attached.

---

The site is already built and deployed. This is a small, self-contained update: replacing the favicon and app icon.

Read `README.md` in this folder first — it explains what's changing and why there are now two separate icon designs rather than one.

What I need:

1. Copy the six files from this folder into the site root (not `assets/`): `favicon.svg`, `favicon-16.png`, `favicon-32.png`, `apple-touch-icon.svg`, `favicon-180.png`, `favicon-512.png`. Delete the old favicon files they replace.
2. Update the `<link>` tags in the document head to match the markup block in `README.md`. Note the addition of a 16×16 entry.
3. If there's a web app manifest, point its 512 icon at `favicon-512.png`.
4. Check nothing else in the codebase still references the old icon paths.

Two things that are easy to get wrong, both explained in the README: the tab favicon and the app icon are deliberately different files and neither should be generated from the other, and `favicon-180.png` must stay a full opaque square with square corners.

Then deploy. Tell me what you changed before you push.

---

## After the deploy

To see the new home-screen icon on iPhone, delete the existing bookmark and re-add the site from Safari. iOS caches touch icons aggressively and will keep showing the old tile otherwise.

Worth checking once it's live:

- *"Show me the page source head so I can confirm the icon tags."*
- *"Confirm all six icon files return 200 from the site root."*
