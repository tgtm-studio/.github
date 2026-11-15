# tgtm studio brand

The studio mark is the lowercase word `tgtm`. One orange line runs through both t's
and rests on top of the g. That line is the signature; keep it intact everywhere.

## Colours

| Name | Hex | Use |
|---|---|---|
| Signal orange | `#FF5A1F` | The crossbar. The only accent colour. |
| Ink | `#111111` | Avatar background, letters on light backgrounds |
| White | `#FFFFFF` | Letters on dark backgrounds |

## Files

| File | Use |
|---|---|
| `png/avatar-500.png`, `png/avatar-1000.png` | GitHub org avatar, social profiles |
| `svg/avatar.svg` | Master avatar (ink tile) |
| `svg/avatar-orange.svg`, `png/avatar-orange-1000.png` | Alternative tile for special occasions |
| `svg/mark-on-light.svg`, `svg/mark-on-dark.svg`, `png/mark-on-*.png` | Mark without a tile, transparent background |
| `svg/lockup-on-light.svg`, `svg/lockup-on-dark.svg`, `png/lockup-on-*.png` | Mark plus "studio", for headers, READMEs and slides |
| `svg/favicon.svg`, `png/favicon-*.png`, `png/favicon.ico`, `png/apple-touch-icon.png` | 16–512px icons: a single t with the orange bar |
| `svg/favicon-on-light.svg` | Small icon without a tile |

## Rules

- Use the favicon t below 48px; the full `tgtm` gets muddy there.
- Keep clear space around the mark of at least the height of the g bowl.
- Don't recolour the crossbar, add effects, outline the letters or set `tgtm` in a font.
- Product logos (Spinout and later games) are separate; this mark is only for the studio.

## Geometry and regenerating

Everything is drawn on a 240-unit grid with a 12-unit stroke, square ends, a 56-unit
x-height and 22-unit bowls. "studio" uses the same construction at half size.
`make_logo.py` writes all SVGs:

```bash
python3 make_logo.py svg
```

PNGs are rendered with [resvg](https://github.com/linebender/resvg)
(`cargo install resvg`), e.g. `resvg svg/lockup-on-light.svg -w 2000 png/lockup-on-light.png`.
`favicon.ico` is made from `favicon-32.png` with `sips -s format ico`.
