"""Generate the tgtm studio logo SVGs. Geometry on a 240-unit grid, stroke 12."""
import pathlib, sys

OUT = pathlib.Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)

ORANGE = "#FF5A1F"
INK = "#111111"
WHITE = "#FFFFFF"

# Mark, centred in a 240x240 box. Baseline y=140, x-height top (outer) y=84.
LETTERS = (
    'M34 60V140'                                    # t stem
    'M108 90V152A22 22 0 0 1 64 152'                # g stem + hook
    'M132 60V140'                                   # t stem
    'M164 140V84'                                   # m first stem
    'M164 104A14 14 0 0 1 192 104V140'              # m first arch
    'M192 104A14 14 0 0 1 220 104V140'              # m second arch
)
G_BOWL = '<circle cx="86" cy="112" r="22"/>'
# Shared crossbar: reaches 20 units past each t stem's centre, same on both sides.
BAR = 'M14 78H152'

# "studio" in the same construction, origin x=0, baseline 140.
STUDIO = (
    'M34 90H20A11 11 0 0 0 20 112A11 11 0 0 1 20 134H6'  # s
    'M56 60V140M46 84H76'                                # t
    'M96 84V118A16 16 0 0 0 128 118V84M128 84V140'       # u
    'M198 60V140'                                        # d stem
    'M224 90V140'                                        # i
)
STUDIO_BOWLS = '<circle cx="176" cy="112" r="22"/><circle cx="272" cy="112" r="22"/>'
STUDIO_DOT = '<rect x="218" y="62" width="12" height="12"/>'


def svg(view, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view}" role="img">'
            f'<title>{title}</title>{body}</svg>\n')


def mark(fg, bar=ORANGE):
    return (f'<g fill="none" stroke-width="12" stroke-linecap="butt">'
            f'<g stroke="{fg}"><path d="{LETTERS}"/>{G_BOWL}</g>'
            f'<path d="{BAR}" stroke="{bar}"/></g>')


def studio(fg, x, scale=0.5):
    y = 140 - 140 * scale
    return (f'<g transform="translate({x} {y}) scale({scale})">'
            f'<g fill="none" stroke="{fg}" stroke-width="12"><path d="{STUDIO}"/>{STUDIO_BOWLS}</g>'
            f'<g fill="{fg}">{STUDIO_DOT}</g></g>')


def tile(bg):
    return f'<rect width="240" height="240" fill="{bg}"/>'


def small_t(fg, bar=ORANGE):
    # Favicon: one bold t, stroke 28, orange crossbar.
    return (f'<g fill="none" stroke-width="28"><path d="M92 48V192" stroke="{fg}"/>'
            f'<path d="M60 92H180" stroke="{bar}"/></g>')


files = {
    "avatar.svg": svg("0 0 240 240", tile(INK) + mark(WHITE), "tgtm studio"),
    "avatar-orange.svg": svg("0 0 240 240", tile(ORANGE) + mark(INK, INK), "tgtm studio"),
    "mark-on-light.svg": svg("4 50 232 140", mark(INK), "tgtm studio"),
    "mark-on-dark.svg": svg("4 50 232 140", mark(WHITE), "tgtm studio"),
    "lockup-on-light.svg": svg("4 50 409 140", mark(INK) + studio(INK, 253), "tgtm studio"),
    "lockup-on-dark.svg": svg("4 50 409 140", mark(WHITE) + studio(WHITE, 253), "tgtm studio"),
    "favicon.svg": svg("0 0 240 240", tile(INK) + small_t(WHITE), "tgtm studio"),
    "favicon-on-light.svg": svg("0 0 240 240", small_t(INK), "tgtm studio"),
}
for name, data in files.items():
    (OUT / name).write_text(data)
    print("wrote", name)
