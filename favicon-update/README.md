# Icon update — danmcspirit.com

Replaces the previously deployed favicon. Nothing else about the site changes.

## Why

The old icon was cream `Mᶜ` on navy, sized to fill the tile so it would survive a 16px browser tab. That sizing is correct for a favicon and wrong for a home-screen app icon: at 120px the artwork ran nearly edge to edge, which reads as a cropped screenshot rather than a drawn mark. The raised `c` was also a constant-weight arc with no terminals, so it didn't match the modulated serif `M` beside it.

Both are fixed, and the set is now **two designs, not one**.

## The two files

| | Tab favicon | App icon |
|---|---|---|
| Source | `favicon.svg` | `apple-touch-icon.svg` |
| Ground | Cream `#EDE7D9` | Cream `#EDE7D9` |
| Ink | Navy `#23426A` | Navy `#23426A` |
| Artwork size | ~79% of tile | ~58% of tile |
| Keyline | none | inset 38/512, navy at 35% opacity, `rx="64"` |
| Rendered to | `favicon-16.png`, `favicon-32.png` | `favicon-180.png`, `favicon-512.png` |

They have different jobs. At 16px every pixel of margin is a pixel the letterforms don't get, so the favicon is pushed out as far as it goes. At 120px the margin and the keyline are what make the mark look considered. **Do not generate one from the other.**

## The mark

`Mᶜ` — the old contraction for *Mac*, which turns generic initials into the name specifically. Both letterforms are filled vector paths in the SVG; there is no webfont dependency and no `<text>` element, so the files render identically in every browser and in contexts that don't load fonts at all.

The `c` is constructed from two offset circles (outer r=42 centred at 50,50; inner r=29 centred at 55,50, in a 100-unit box) and cut open on the right at ±50°. The offset is what produces the stroke modulation — thick on the left, thinning to angled terminals — so it sits properly beside the serif `M`.

## Files

| File | Notes |
|---|---|
| `favicon.svg` | Primary favicon, 512×512 viewBox. Scales to any size. |
| `favicon-16.png` | 16×16 PNG. |
| `favicon-32.png` | 32×32 PNG fallback. |
| `apple-touch-icon.svg` | App icon source, 512×512 viewBox. Keyline variant. |
| `favicon-180.png` | 180×180 apple-touch-icon. |
| `favicon-512.png` | 512×512 for PWA manifest / high-DPI. |

## Markup

All six files belong at the **site root**, not in `assets/`.

```html
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="/favicon-16.png" sizes="16x16" type="image/png">
<link rel="apple-touch-icon" href="/favicon-180.png">
```

## Two constraints

**`favicon-180.png` must be a full opaque square with square corners.** iOS applies its own squircle mask. Baking corner rounding or transparency into the PNG produces a visible double radius. The exported file is already correct — don't run it through an icon generator that "helpfully" rounds it.

**iOS caches home-screen icons.** After deploying, delete the existing bookmark and re-add the site from Safari, or you'll keep seeing the old navy tile regardless of what's on the server.
