"""Genera los activos de marca de OGIR Positiva.

Todo el texto se convierte a contornos con Inter, así el resultado es idéntico
en cualquier equipo (GitHub no carga fuentes externas dentro de un SVG).
Este archivo es la fuente de verdad: para cambiar algo, editar acá y regenerar.
"""
from typeset import typeset, width

NARANJA = "#F2681C"
BLANCO = "#FFFFFF"
TEXTO = "#D6DFE7"
CHIP = "#DDE6EC"
APAGADO = "#A7B7C4"
LINEA = "#22323F"

# Atributos: se conservan los tres que aportan información (dos verbos del
# oficio + el diferenciador). "Integridad" y "Compromiso" salieron porque son
# valores que cualquier organización declara y por eso informan menos.
ATRIBUTOS = [("ic-search", "Análisis"), ("ic-target", "Prevención"), ("ic-chip", "IA")]


def T(text, size, x, y, wght, opsz=None, tracking=0.0, fill=BLANCO):
    d, w = typeset(text, size, x, y, wght, opsz, tracking)
    return f'<path d="{d}" fill="{fill}"/>', w


ICONOS = {
    "ic-search": """<g id="ic-search" fill="none" stroke="%s" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="8.6" cy="8.6" r="5.9"/><path d="M12.9 12.9 17.6 17.6"/>
      <path d="M5.9 9.6 7.5 7.1 9.4 10.6 11.3 7.9"/></g>""" % NARANJA,
    "ic-target": """<g id="ic-target" fill="none" stroke="%s" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="10" cy="10" r="7.4"/><circle cx="10" cy="10" r="3.2"/>
      <path d="M10 1.2v2.6M10 16.2v2.6M1.2 10h2.6M16.2 10h2.6"/></g>""" % NARANJA,
    "ic-chip": """<g id="ic-chip" fill="none" stroke="%s" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
      <rect x="5.2" y="5.2" width="9.6" height="9.6" rx="2.4"/><rect x="8.4" y="8.4" width="3.2" height="3.2" rx="1"/>
      <path d="M8 2.6v2.6M12 2.6v2.6M8 14.8v2.6M12 14.8v2.6M2.6 8h2.6M2.6 12h2.6M14.8 8h2.6M14.8 12h2.6"/></g>""" % NARANJA,
    "ic-lock": """<g id="ic-lock" fill="none" stroke="%s" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">
      <path d="M8.3 11.2V7.9a4.7 4.7 0 0 1 9.4 0v3.3"/>
      <rect x="4.9" y="11.2" width="16.2" height="11.4" rx="2.6"/>
      <circle cx="13" cy="15.9" r="1.4"/><path d="M13 17.6v2.3"/></g>""" % NARANJA,
}

MONOGRAMA = """<circle{halo} cx="150" cy="128" r="80" fill="none" stroke="{o}" stroke-opacity="0.20" stroke-width="1.4" stroke-dasharray="3 9"/>
    <path d="M208 128 A58 58 0 1 1 183.27 80.49" fill="none" stroke="{o}" stroke-width="22"/>
    <rect x="150" y="117" width="70" height="22" rx="1.5" fill="{o}"/>
    <path d="M168.73 148.81 A28 28 0 1 1 168.73 107.19" fill="none" stroke="{b}" stroke-width="15"/>"""

FANTASMA = """<g transform="translate({tx} {ty}) scale({s})" fill="none" stroke="{o}">
        <path d="M104 0 A104 104 0 1 1 59.65 -85.19" stroke-opacity="0.09" stroke-width="38"/>
        <path d="M123 0 A123 123 0 1 1 70.55 -100.75" stroke-opacity="0.20" stroke-width="1.6"/>
        <path d="M85 0 A85 85 0 1 1 48.75 -69.63" stroke-opacity="0.20" stroke-width="1.6"/>
        <path d="M4 -19 H127 M4 19 H127 M4 -19 V19" stroke-opacity="0.20" stroke-width="1.6"/>
      </g>"""

ESTILO = """
    <style>
      /* Solo bucles ambientales: no hay animacion de entrada. El header se ve
         completo desde el primer fotograma. */

      /* Radar, lado derecho */
      .radar { transform-box: view-box; transform-origin: RADAR_ORIGIN; opacity: 0;
               animation: radar 6s ease-out infinite; }
      @keyframes radar {
        0%   { opacity: 0; transform: scale(.84); }
        25%  { opacity: 1; }
        100% { opacity: 0; transform: scale(1.1); }
      }
      .r1 { animation-delay: 0s; } .r2 { animation-delay: .8s; } .r3 { animation-delay: 1.6s; }

      /* Anillo punteado, lado izquierdo */
      .halo { transform-box: view-box; transform-origin: HALO_ORIGIN;
              animation: spin 34s linear infinite; }
      @keyframes spin { to { transform: rotate(360deg); } }

      @media (prefers-reduced-motion: reduce) {
        .radar { opacity: .85 !important; animation: none !important; transform: none !important; }
        .halo  { animation: none !important; transform: none !important; }
      }
    </style>
"""


def estilo(radar_origin, halo_origin):
    return ESTILO.replace("RADAR_ORIGIN", radar_origin).replace("HALO_ORIGIN", halo_origin)


def fila_atributos(x0, y_icono, size=19, gap_icono=12, pad=20):
    """Devuelve (svg, ancho_total) con los atributos y sus separadores."""
    partes, x = [], x0
    base_y = y_icono + 10 + size * 0.727 / 2  # centrado optico contra el icono de 20px
    for i, (icono, etiqueta) in enumerate(ATRIBUTOS):
        if i:
            partes.append(f'<rect x="{x:.1f}" y="{y_icono - 1}" width="1.5" height="22" fill="{LINEA}"/>')
            x += 1.5 + pad
        partes.append(f'<use href="#{icono}" x="{x:.1f}" y="{y_icono}"/>')
        p, w = T(etiqueta, size, x + 20 + gap_icono, base_y, 500, size, fill=CHIP)
        partes.append(p)
        x += 20 + gap_icono + w + pad
    return "\n      ".join(partes), x - pad - x0


def ancho_atributos(size=19, gap_icono=12, pad=20):
    total = sum(20 + gap_icono + width(e, size, 500, size) for _, e in ATRIBUTOS)
    return total + (len(ATRIBUTOS) - 1) * (1.5 + pad * 2)


# ---------------------------------------------------------------- header ----
def header(animated: bool) -> str:
    halo_cls = ' class="halo"' if animated else ""
    radar = []
    for i, (r, op) in enumerate(((150, 0.16), (195, 0.12), (240, 0.09)), start=1):
        cls = f' class="radar r{i}"' if animated else ""
        radar.append(f'<circle{cls} cx="1180" cy="150" r="{r}" stroke-opacity="{op}" stroke-width="1.4"/>')

    css = estilo("1180px 150px", "150px 128px") if animated else ""
    atributos, _ = fila_atributos(294, 208)

    og, w_og = T("OGIR", 66, 292, 136, 800, 32, -1.6)
    pos, _ = T("Positiva", 66, 292 + w_og + 17, 136, 800, 32, -1.6, fill=NARANJA)
    sub, _ = T("Oficina de Gestión Integral de Riesgos", 25, 294, 178, 400, 25, fill=TEXTO)
    tag, _ = T("Transformamos la gestión de riesgos en valor sostenible.", 18, 94, 289, 400, 18, fill=APAGADO)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="1200" height="320" role="img" aria-label="OGIR Positiva — Oficina de Gestión Integral de Riesgos. Organización privada. Transformamos la gestión de riesgos en valor sostenible.">
  <title>OGIR Positiva — Oficina de Gestión Integral de Riesgos</title>

  <defs>
    <linearGradient id="panel" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0C1620"/><stop offset="0.55" stop-color="#0E1B26"/><stop offset="1" stop-color="#0A131B"/>
    </linearGradient>
    <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{NARANJA}" stop-opacity="0.12"/><stop offset="0.16" stop-color="{NARANJA}"/>
      <stop offset="0.84" stop-color="{NARANJA}"/><stop offset="1" stop-color="{NARANJA}" stop-opacity="0.12"/>
    </linearGradient>
    <linearGradient id="topLight" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{BLANCO}" stop-opacity="0"/><stop offset="0.35" stop-color="{BLANCO}" stop-opacity="0.10"/>
      <stop offset="0.65" stop-color="{BLANCO}" stop-opacity="0.10"/><stop offset="1" stop-color="{BLANCO}" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="panelClip"><rect x="8" y="8" width="1184" height="304" rx="22"/></clipPath>
    {ICONOS['ic-search']}
    {ICONOS['ic-target']}
    {ICONOS['ic-chip']}
    {ICONOS['ic-lock']}
{css}  </defs>

  <rect x="8" y="8" width="1184" height="304" rx="22" fill="url(#panel)"/>

  <g clip-path="url(#panelClip)">
    <g fill="none" stroke="{NARANJA}">
      {" ".join(radar)}
    </g>
    {FANTASMA.format(tx=1105, ty=150, s=1, o=NARANJA)}
    <rect x="8" y="252" width="1184" height="60" fill="#080F16"/>
    <rect x="8" y="8" width="1184" height="1.5" fill="url(#topLight)"/>
  </g>

  <rect x="8" y="250.5" width="1184" height="2.5" fill="url(#rule)"/>

  <g>
    {MONOGRAMA.format(halo=halo_cls, o=NARANJA, b=BLANCO)}
  </g>

  <rect x="262" y="88" width="1.5" height="140" fill="{LINEA}"/>

  {og}
  {pos}
  {sub}

  <g>
      {atributos}
  </g>

  <g><title>Organización privada</title><use href="#ic-lock" x="54" y="269"/></g>
  {tag}

  <rect x="8.75" y="8.75" width="1182.5" height="302.5" rx="21.25" fill="none" stroke="#1D2C39" stroke-width="1.5"/>
</svg>
"""


# ------------------------------------------------------------------ slim ----
def slim() -> str:
    og, w_og = T("OGIR", 36, 150, 66, 800, 32, -0.9)
    pos, _ = T("Positiva", 36, 150 + w_og + 9, 66, 800, 32, -0.9, fill=NARANJA)
    tag, _ = T("Oficina de Gestión Integral de Riesgos", 16, 152, 94, 400, 16, fill=APAGADO)
    radar = "".join(
        f'<circle class="radar r{i}" cx="1180" cy="70" r="{r}" stroke-opacity="{op}" stroke-width="1.3"/>'
        for i, (r, op) in enumerate(((95, 0.16), (130, 0.12), (165, 0.09)), start=1)
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 140" width="1200" height="140" role="img" aria-label="OGIR Positiva — Oficina de Gestión Integral de Riesgos">
  <title>OGIR Positiva</title>
  <defs>
    <linearGradient id="panel" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0C1620"/><stop offset="1" stop-color="#0A131B"/>
    </linearGradient>
    <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{NARANJA}" stop-opacity="0.12"/><stop offset="0.16" stop-color="{NARANJA}"/>
      <stop offset="0.84" stop-color="{NARANJA}"/><stop offset="1" stop-color="{NARANJA}" stop-opacity="0.12"/>
    </linearGradient>
    <clipPath id="c"><rect x="8" y="8" width="1184" height="124" rx="18"/></clipPath>
{estilo("1180px 70px", "150px 128px")}  </defs>

  <rect x="8" y="8" width="1184" height="124" rx="18" fill="url(#panel)"/>
  <g clip-path="url(#c)">
    <g fill="none" stroke="{NARANJA}">{radar}</g>
    {FANTASMA.format(tx=1110, ty=70, s=0.62, o=NARANJA)}
    <rect x="8" y="127" width="1184" height="5" fill="url(#rule)"/>
  </g>
  <g transform="translate(72 70) scale(0.52) translate(-150 -128)">
    {MONOGRAMA.format(halo=' class="halo"', o=NARANJA, b=BLANCO)}
  </g>
  <rect x="126" y="42" width="1.5" height="56" fill="{LINEA}"/>
  {og}
  {pos}
  {tag}
  <rect x="8.75" y="8.75" width="1182.5" height="122.5" rx="17.25" fill="none" stroke="#1D2C39" stroke-width="1.5"/>
</svg>
"""


# ---------------------------------------------------------------- social ----
def social() -> str:
    cx = 640
    w_og = width("OGIR", 78, 800, 32, -2)
    w_pos = width("Positiva", 78, 800, 32, -2)
    x0 = cx - (w_og + 20 + w_pos) / 2
    og, _ = T("OGIR", 78, x0, 420, 800, 32, -2)
    pos, _ = T("Positiva", 78, x0 + w_og + 20, 420, 800, 32, -2, fill=NARANJA)

    w_sub = width("Oficina de Gestión Integral de Riesgos", 29, 400, 29)
    sub, _ = T("Oficina de Gestión Integral de Riesgos", 29, cx - w_sub / 2, 468, 400, 29, fill=TEXTO)

    attrs, _ = fila_atributos(cx - ancho_atributos(20) / 2, 528, size=20)

    radar = "".join(
        f'<circle cx="{cx}" cy="205" r="{r}" stroke-opacity="{op}" stroke-width="1.6"/>'
        for r, op in ((300, 0.10), (400, 0.07), (500, 0.05))
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 640" width="1280" height="640" role="img" aria-label="OGIR Positiva — Oficina de Gestión Integral de Riesgos">
  <title>OGIR Positiva — Oficina de Gestión Integral de Riesgos</title>
  <defs>
    <linearGradient id="panel" x1="0" y1="0" x2="0.6" y2="1">
      <stop offset="0" stop-color="#0D1822"/><stop offset="0.6" stop-color="#0E1B26"/><stop offset="1" stop-color="#09121A"/>
    </linearGradient>
    <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{NARANJA}" stop-opacity="0"/><stop offset="0.5" stop-color="{NARANJA}"/>
      <stop offset="1" stop-color="{NARANJA}" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="c"><rect x="0" y="0" width="1280" height="640"/></clipPath>
    {ICONOS['ic-search']}
    {ICONOS['ic-target']}
    {ICONOS['ic-chip']}
  </defs>
  <rect width="1280" height="640" fill="url(#panel)"/>
  <g clip-path="url(#c)" fill="none" stroke="{NARANJA}">{radar}</g>
  <g transform="translate({cx} 205) scale(1.3) translate(-150 -128)">
    {MONOGRAMA.format(halo="", o=NARANJA, b=BLANCO)}
  </g>
  {og}
  {pos}
  {sub}
  <rect x="{cx - 90}" y="498" width="180" height="2.5" fill="url(#rule)"/>
  <g>
      {attrs}
  </g>
</svg>
"""


if __name__ == "__main__":
    salidas = {
        "ogir-header.svg": header(False),
        "ogir-header-animated.svg": header(True),
        "ogir-header-slim.svg": slim(),
        "ogir-social.svg": social(),
    }
    for nombre, contenido in salidas.items():
        with open(nombre, "w", encoding="utf-8") as fh:
            fh.write(contenido)
        print("escrito", nombre)
