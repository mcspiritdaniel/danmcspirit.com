# Icon update — danmcspirit.com

Replaces the previously deployed favicon. Nothing else about the site changes.

## What's changing

The old icon was a cream `Mᶜ` on navy, sized to fill the tile so it would survive a 16px browser tab. That sizing is right for a favicon and wrong for a home-screen app icon: at 120px the artwork ran nearly edge to edge, which reads as cropped type rather than a drawn mark.

The new set is a solo **M** set in Newsreader — the site's own serif — in navy `#23426A` on cream `#EDE7D9`. The raised `c` is gone. It was 37% of the M's cap height, which put it under 3 pixels tall at 16px, and its mismatched weight was what made the pair look unresolved at every size. Dropping it lets the M run 37% larger (cap height 115px on a 512 tile, against 84px in the pair). The tile never appears without "Dan McSpirit" set beneath it, so the label carries the specificity the `c` was straining to add.

## Two designs, not one

| | Tab favicon | App icon |
|---|---|---|
| Ground | Cream `#EDE7D9` | Cream `#EDE7D9` |
| Ink | Navy `#23426A` | Navy `#23426A` |
| Ink box | 82% of tile width | 62% of tile width |
| Keyline | none | inset 38/512, navy at 35% opacity, `rx="64"` |
| Files | `favicon-32.png`, `favicon-16.png` | `favicon-180.png`, `favicon-512.png` |

They have different jobs. At 16px every pixel of margin is a pixel the letterform doesn't get, so the favicon is pushed out as far as it goes. At 120px the margin and the keyline are what make the mark look considered.

**Do not generate one from the other, and do not re-render either from a single master.**

## Files

| File | Size | Notes |
|---|---|---|
| `favicon-16.png` | 16×16 | Tab favicon |
| `favicon-32.png` | 32×32 | Tab favicon |
| `favicon-180.png` | 180×180 | apple-touch-icon |
| `favicon-512.png` | 512×512 | PWA manifest / high-DPI |

**The set is PNG-only, deliberately.** There is no `favicon.svg`. An SVG can't carry Newsreader's letterform without either embedding the font file or hand-tracing the outlines, and a traced approximation is what made the previous version drift away from the approved design. The M in these PNGs is the real typeface, optically centred on its ink box (cap-top to baseline), not on the em box. PNGs at these four sizes cover every browser and platform in use.

## Markup

All four files belong at the **site root**, not in `assets/`.

```html
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="/favicon-16.png" sizes="16x16" type="image/png">
<link rel="apple-touch-icon" href="/favicon-180.png">
```

Remove any existing `<link rel="icon" type="image/svg+xml">` tag — the SVG no longer exists and the tag would 404 and take precedence in browsers that support it.

## Two constraints

**`favicon-180.png` must stay a full opaque square with square corners.** iOS applies its own squircle mask. Baking corner rounding or transparency into the PNG produces a visible double radius. The exported file is already correct — don't run it through an icon generator that "helpfully" rounds it.

**iOS caches home-screen icons.** After deploying, delete the existing bookmark and re-add the site from Safari, or you'll keep seeing the old navy tile regardless of what's on the server.
