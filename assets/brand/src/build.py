
from typeset import typeset, width

NARANJA = "#F2681C"

PALETAS = {
    "panel": {  # sobre el panel oscuro propio
        "fuerte": "#FFFFFF",
        "medio": "#D6DFE7",
        "chip": "#DDE6EC",
        "suave": "#A7B7C4",
        "linea": "#22323F",
        "fantasma": 0.20,
        "velo": 0.09,
    },
    "dark": {  # transparente sobre el tema oscuro de GitHub (#0d1117)
        "fuerte": "#E6EDF3",
        "medio": "#C9D6E0",
        "chip": "#C9D6E0",
        "suave": "#8B949E",
        "linea": "#30363D",
        "fantasma": 0.16,
        "velo": 0.07,
    },
    "light": {  # transparente sobre el tema claro de GitHub (#ffffff)
        "fuerte": "#0C1620",
        "medio": "#2C3B48",
        "chip": "#2C3B48",
        "suave": "#57606A",
        "linea": "#D0D7DE",
        "fantasma": 0.13,
        "velo": 0.05,
    },
}

ATRIBUTOS = [("ic-search", "Análisis"), ("ic-target", "Prevención"), ("ic-chip", "IA")]


def T(text, size, x, y, wght, opsz=None, tracking=0.0, fill="#000000", opacity=None):
    d, w = typeset(text, size, x, y, wght, opsz, tracking)
    op = f' fill-opacity="{opacity}"' if opacity is not None else ""
    return f'<path d="{d}" fill="{fill}"{op}/>', w


def iconos(*cuales):
    base = {
        "ic-search": """<g id="ic-search" fill="none" stroke="{o}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="8.6" cy="8.6" r="5.9"/><path d="M12.9 12.9 17.6 17.6"/>
      <path d="M5.9 9.6 7.5 7.1 9.4 10.6 11.3 7.9"/></g>""",
        "ic-target": """<g id="ic-target" fill="none" stroke="{o}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="10" cy="10" r="7.4"/><circle cx="10" cy="10" r="3.2"/>
      <path d="M10 1.2v2.6M10 16.2v2.6M1.2 10h2.6M16.2 10h2.6"/></g>""",
        "ic-chip": """<g id="ic-chip" fill="none" stroke="{o}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
      <rect x="5.2" y="5.2" width="9.6" height="9.6" rx="2.4"/><rect x="8.4" y="8.4" width="3.2" height="3.2" rx="1"/>
      <path d="M8 2.6v2.6M12 2.6v2.6M8 14.8v2.6M12 14.8v2.6M2.6 8h2.6M2.6 12h2.6M14.8 8h2.6M14.8 12h2.6"/></g>""",
        "ic-lock": """<g id="ic-lock" fill="none" stroke="{o}" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">
      <path d="M8.3 11.2V7.9a4.7 4.7 0 0 1 9.4 0v3.3"/>
      <rect x="4.9" y="11.2" width="16.2" height="11.4" rx="2.6"/>
      <circle cx="13" cy="15.9" r="1.4"/><path d="M13 17.6v2.3"/></g>""",
    }
    return "\n    ".join(base[c].format(o=NARANJA) for c in cuales)


def monograma(halo_cls, fuerte):
    """El contra de la G usa el color 'fuerte' del tema: en fondo claro tiene
    que ser oscuro, no blanco, o el interior de la letra desaparece."""
    return f"""<circle{halo_cls} cx="150" cy="128" r="80" fill="none" stroke="{NARANJA}" stroke-opacity="0.20" stroke-width="1.4" stroke-dasharray="3 9"/>
    <path d="M208 128 A58 58 0 1 1 183.27 80.49" fill="none" stroke="{NARANJA}" stroke-width="22"/>
    <rect x="150" y="117" width="70" height="22" rx="1.5" fill="{NARANJA}"/>
    <path d="M168.73 148.81 A28 28 0 1 1 168.73 107.19" fill="none" stroke="{fuerte}" stroke-width="15"/>"""


def fantasma(tx, ty, s, op, velo):
    return f"""<g transform="translate({tx} {ty}) scale({s})" fill="none" stroke="{NARANJA}">
        <path d="M104 0 A104 104 0 1 1 59.65 -85.19" stroke-opacity="{velo}" stroke-width="38"/>
        <path d="M123 0 A123 123 0 1 1 70.55 -100.75" stroke-opacity="{op}" stroke-width="1.6"/>
        <path d="M85 0 A85 85 0 1 1 48.75 -69.63" stroke-opacity="{op}" stroke-width="1.6"/>
        <path d="M4 -19 H127 M4 19 H127 M4 -19 V19" stroke-opacity="{op}" stroke-width="1.6"/>
      </g>"""


ESTILO = """
    <style>
      /* Solo bucles ambientales: sin animación de entrada, el gráfico se ve
         completo desde el primer fotograma. */
      .radar { transform-box: view-box; transform-origin: RADAR_ORIGIN; opacity: 0;
               animation: radar 6s ease-out infinite; }
      @keyframes radar {
        0%   { opacity: 0; transform: scale(.84); }
        25%  { opacity: 1; }
        100% { opacity: 0; transform: scale(1.1); }
      }
      .r1 { animation-delay: 0s; } .r2 { animation-delay: .8s; } .r3 { animation-delay: 1.6s; }

      .halo { transform-box: view-box; transform-origin: HALO_ORIGIN;
              animation: spin 34s linear infinite; }
      @keyframes spin { to { transform: rotate(360deg); } }

      @media (prefers-reduced-motion: reduce) {
        .radar { opacity: .85 !important; animation: none !important; transform: none !important; }
        .halo  { animation: none !important; transform: none !important; }
      }
    </style>
"""


def estilo(radar, halo):
    return ESTILO.replace("RADAR_ORIGIN", radar).replace("HALO_ORIGIN", halo)


def fila_atributos(x0, y_icono, p, size=19, gap=12, pad=20):
    partes, x = [], x0
    base_y = y_icono + 10 + size * 0.727 / 2
    for i, (icono, etiqueta) in enumerate(ATRIBUTOS):
        if i:
            partes.append(f'<rect x="{x:.1f}" y="{y_icono - 1}" width="1.5" height="22" fill="{p["linea"]}"/>')
            x += 1.5 + pad
        partes.append(f'<use href="#{icono}" x="{x:.1f}" y="{y_icono}"/>')
        t, w = T(etiqueta, size, x + 20 + gap, base_y, 500, size, fill=p["chip"])
        partes.append(t)
        x += 20 + gap + w + pad
    return "\n      ".join(partes), x - pad - x0


def ancho_atributos(size=19, gap=12, pad=20):
    total = sum(20 + gap + width(e, size, 500, size) for _, e in ATRIBUTOS)
    return total + (len(ATRIBUTOS) - 1) * (1.5 + pad * 2)


# ---------------------------------------------------------------- header ----
def header(animated=False, tema="panel"):
    p = PALETAS[tema]
    con_panel = tema == "panel"
    halo = ' class="halo"' if animated else ""
    css = estilo("1180px 150px", "150px 128px") if animated else ""

    radar = " ".join(
        f'<circle{f" class=\"radar r{i}\"" if animated else ""} cx="1180" cy="150" r="{r}" '
        f'stroke-opacity="{op * (1 if con_panel else 0.8):.3f}" stroke-width="1.4"/>'
        for i, (r, op) in enumerate(((150, 0.16), (195, 0.12), (240, 0.09)), start=1)
    )

    og, w_og = T("OGIR", 66, 292, 136, 800, 32, -1.6, fill=p["fuerte"])
    pos, _ = T("Positiva", 66, 292 + w_og + 17, 136, 800, 32, -1.6, fill=NARANJA)
    sub, _ = T("Oficina de Gestión Integral de Riesgos", 25, 294, 178, 400, 25, fill=p["medio"])
    tag, _ = T("Transformamos la gestión de riesgos en valor sostenible.", 18, 94, 289, 400, 18, fill=p["suave"])
    attrs, _ = fila_atributos(294, 208, p)

    if con_panel:
        fondo = f"""<rect x="8" y="8" width="1184" height="304" rx="22" fill="url(#panel)"/>
  <g clip-path="url(#panelClip)">
    <g fill="none" stroke="{NARANJA}">{radar}</g>
    {fantasma(1105, 150, 1, p["fantasma"], p["velo"])}
    <rect x="8" y="252" width="1184" height="60" fill="#080F16"/>
    <rect x="8" y="8" width="1184" height="1.5" fill="url(#topLight)"/>
  </g>"""
        borde = f'<rect x="8.75" y="8.75" width="1182.5" height="302.5" rx="21.25" fill="none" stroke="#1D2C39" stroke-width="1.5"/>'
        defs_panel = """<linearGradient id="panel" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0C1620"/><stop offset="0.55" stop-color="#0E1B26"/><stop offset="1" stop-color="#0A131B"/>
    </linearGradient>
    <linearGradient id="topLight" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/><stop offset="0.35" stop-color="#FFFFFF" stop-opacity="0.10"/>
      <stop offset="0.65" stop-color="#FFFFFF" stop-opacity="0.10"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="panelClip"><rect x="8" y="8" width="1184" height="304" rx="22"/></clipPath>"""
    else:
        # Sin panel el recorte no hace falta, pero el radar sí: se deja suelto
        # y más tenue para que no ensucie el fondo del lector.
        fondo = f"""<g fill="none" stroke="{NARANJA}">{radar}</g>
  {fantasma(1105, 150, 1, p["fantasma"], p["velo"])}"""
        borde = ""
        defs_panel = ""

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="1200" height="320" role="img" aria-label="OGIR Positiva — Oficina de Gestión Integral de Riesgos. Organización privada. Transformamos la gestión de riesgos en valor sostenible.">
  <title>OGIR Positiva — Oficina de Gestión Integral de Riesgos</title>

  <defs>
    {defs_panel}
    <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{NARANJA}" stop-opacity="0.12"/><stop offset="0.16" stop-color="{NARANJA}"/>
      <stop offset="0.84" stop-color="{NARANJA}"/><stop offset="1" stop-color="{NARANJA}" stop-opacity="0.12"/>
    </linearGradient>
    {iconos("ic-search", "ic-target", "ic-chip", "ic-lock")}
{css}  </defs>

  {fondo}

  <rect x="8" y="250.5" width="1184" height="2.5" fill="url(#rule)"/>

  <g>
    {monograma(halo, p["fuerte"])}
  </g>

  <rect x="262" y="88" width="1.5" height="140" fill="{p['linea']}"/>

  {og}
  {pos}
  {sub}

  <g>
      {attrs}
  </g>

  <g><title>Organización privada</title><use href="#ic-lock" x="54" y="269"/></g>
  {tag}

  {borde}
</svg>
"""


# ------------------------------------------------------------------ slim ----
def slim(tema="panel"):
    p = PALETAS[tema]
    con_panel = tema == "panel"
    og, w_og = T("OGIR", 36, 150, 66, 800, 32, -0.9, fill=p["fuerte"])
    pos, _ = T("Positiva", 36, 150 + w_og + 9, 66, 800, 32, -0.9, fill=NARANJA)
    tag, _ = T("Oficina de Gestión Integral de Riesgos", 16, 152, 94, 400, 16, fill=p["suave"])
    radar = "".join(
        f'<circle class="radar r{i}" cx="1180" cy="70" r="{r}" stroke-opacity="{op}" stroke-width="1.3"/>'
        for i, (r, op) in enumerate(((95, 0.16), (130, 0.12), (165, 0.09)), start=1)
    )
    if con_panel:
        fondo = f"""<rect x="8" y="8" width="1184" height="124" rx="18" fill="url(#panel)"/>
  <g clip-path="url(#c)">
    <g fill="none" stroke="{NARANJA}">{radar}</g>
    {fantasma(1110, 70, 0.62, p["fantasma"], p["velo"])}
    <rect x="8" y="127" width="1184" height="5" fill="url(#rule)"/>
  </g>"""
        defs_panel = """<linearGradient id="panel" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0C1620"/><stop offset="1" stop-color="#0A131B"/>
    </linearGradient>
    <clipPath id="c"><rect x="8" y="8" width="1184" height="124" rx="18"/></clipPath>"""
        borde = '<rect x="8.75" y="8.75" width="1182.5" height="122.5" rx="17.25" fill="none" stroke="#1D2C39" stroke-width="1.5"/>'
    else:
        fondo = f"""<g fill="none" stroke="{NARANJA}">{radar}</g>
  {fantasma(1110, 70, 0.62, p["fantasma"], p["velo"])}
  <rect x="8" y="127" width="1184" height="3" fill="url(#rule)"/>"""
        defs_panel = ""
        borde = ""

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 140" width="1200" height="140" role="img" aria-label="OGIR Positiva — Oficina de Gestión Integral de Riesgos">
  <title>OGIR Positiva</title>
  <defs>
    {defs_panel}
    <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{NARANJA}" stop-opacity="0.12"/><stop offset="0.16" stop-color="{NARANJA}"/>
      <stop offset="0.84" stop-color="{NARANJA}"/><stop offset="1" stop-color="{NARANJA}" stop-opacity="0.12"/>
    </linearGradient>
{estilo("1180px 70px", "150px 128px")}  </defs>
  {fondo}
  <g transform="translate(72 70) scale(0.52) translate(-150 -128)">
    {monograma(' class="halo"', p["fuerte"])}
  </g>
  <rect x="126" y="42" width="1.5" height="56" fill="{p['linea']}"/>
  {og}
  {pos}
  {tag}
  {borde}
</svg>
"""


# -------------------------------------------------------------- linktree ----
# Icono de Font Awesome Free 7.3.1, bajo licencia CC BY 4.0. La licencia exige
# atribución: por eso el comentario de copyright viaja dentro del archivo y no
# debe borrarse.  https://fontawesome.com/license/free
LINKTREE_PATH = (
    "M112 237.4L237.8 237.4L148.4 152L197.9 101L283.1 188.8L283.1 64L357 64L357 188.8"
    "L442.2 101.2L491.6 152L402.2 237.2L527.9 237.2L527.9 307.7L401.5 307.7L491.5 395.3"
    "L442.2 445.1L320 322.1L197.8 445.1L148.3 395.5L238.3 307.9L111.9 307.9L111.9 237.4z"
    "M282.9 408.8L356.8 408.8L356.8 576L282.9 576L282.9 408.8z"
)


def linktree(size=26):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640" width="{size}" height="{size}" role="img" aria-label="Linktree">
  <title>Linktree</title>
  <!--!Font Awesome Free 7.3.1 by @fontawesome - https://fontawesome.com
       License - https://fontawesome.com/license/free (Icons: CC BY 4.0)
       Copyright 2026 Fonticons, Inc.-->
  <path d="{LINKTREE_PATH}" fill="{NARANJA}"/>
</svg>
"""


# ---------------------------------------------------------------- footer ----
def footer(tema="dark"):
    """Footer minimalista: regla de acento a todo el ancho y el monograma
    solo, a la izquierda. Los textos y enlaces van en Markdown debajo, porque
    un <a> dentro de un SVG cargado con <img> no es clickeable."""
    p = PALETAS[tema]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 110" width="1200" height="110" role="img" aria-label="OGIR Positiva">
  <title>OGIR Positiva</title>
  <defs>
    <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{NARANJA}" stop-opacity="0"/><stop offset="0.5" stop-color="{NARANJA}"/>
      <stop offset="1" stop-color="{NARANJA}" stop-opacity="0"/>
    </linearGradient>
{estilo("600px 40px", "150px 128px")}  </defs>

  <rect x="0" y="6" width="1200" height="2.5" fill="url(#rule)"/>

  <g transform="translate(58 66) scale(0.30) translate(-150 -128)">
    {monograma(' class="halo"', p["fuerte"])}
  </g>
</svg>
"""


if __name__ == "__main__":
    salidas = {
        # Con panel oscuro: un solo archivo, sirve en cualquier tema
        "ogir-header.svg": header(False, "panel"),
        "ogir-header-animated.svg": header(True, "panel"),
        "ogir-header-slim.svg": slim("panel"),
        # Transparentes: par claro/oscuro para usar con <picture>
        "ogir-header-transparent-light.svg": header(False, "light"),
        "ogir-header-transparent-dark.svg": header(False, "dark"),
        "ogir-header-transparent-light-animated.svg": header(True, "light"),
        "ogir-header-transparent-dark-animated.svg": header(True, "dark"),
        "ogir-slim-transparent-light.svg": slim("light"),
        "ogir-slim-transparent-dark.svg": slim("dark"),
        # Footer (siempre transparente)
        "ogir-footer-light.svg": footer("light"),
        "ogir-footer-dark.svg": footer("dark"),
        # Icono suelto para la fila de enlaces
        "ogir-linktree.svg": linktree(),
    }
    for nombre, contenido in salidas.items():
        with open(nombre, "w", encoding="utf-8") as fh:
            fh.write(contenido)
        print("escrito", nombre)
