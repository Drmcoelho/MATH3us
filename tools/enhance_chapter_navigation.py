#!/usr/bin/env python3
"""Aplica navegação sequencial e hierarquia editorial aos capítulos HTML do MATH3us.

O script é idempotente: remove um bloco previamente gerado e o recria.
Ele não altera o conteúdo matemático nem cria dependências externas; cada capítulo
continua sendo um HTML autocontido e funcional sem rede.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Chapter:
    path: str
    number: int
    title: str


CHAPTERS = [
    Chapter("caps/00-inferencia/index.html", 0, "A Inferência"),
    Chapter("caps/01-exaustao/index.html", 1, "A Exaustão"),
    Chapter("caps/02-ternas/index.html", 2, "As Ternas do Ímpar"),
    Chapter("caps/03-quatro/index.html", 3, "A Singularidade do Quatro"),
    Chapter("caps/04-algarismos/index.html", 4, "Os Algarismos Repetidos"),
]

START = "<!-- MATH3US:READER-NAV:START -->"
END = "<!-- MATH3US:READER-NAV:END -->"

CSS = r"""
  .reader-nav{border:1px solid var(--rule); background:var(--box); margin:0 0 1.5rem; padding:.75rem 1rem}
  .reader-nav ul{list-style:none; display:flex; flex-wrap:wrap; gap:.5rem 1rem; align-items:center; margin:0; padding:0}
  .reader-nav a{color:var(--accent); text-decoration-thickness:.08em; text-underline-offset:.18em}
  .reader-nav .spacer{flex:1}
  .reader-nav-bottom{margin:2.5rem 0 0}
  details.editorial{border-top:1px solid var(--rule); margin-top:2rem; padding-top:1rem}
  details.editorial summary{cursor:pointer; color:var(--accent); font-variant:small-caps; letter-spacing:.08em}
  @media (max-width:42rem){.reader-nav .spacer{display:none}.reader-nav ul{display:grid;grid-template-columns:1fr 1fr}.reader-nav li:first-child{grid-column:1/-1}}
"""


def rel_href(current: Chapter, target: Chapter | None) -> str | None:
    if target is None:
        return None
    return f"../{Path(target.path).parent.name}/"


def nav_html(index: int, *, bottom: bool = False) -> str:
    current = CHAPTERS[index]
    previous = CHAPTERS[index - 1] if index > 0 else None
    following = CHAPTERS[index + 1] if index + 1 < len(CHAPTERS) else None
    class_name = "reader-nav reader-nav-bottom" if bottom else "reader-nav"
    parts = [START, f'<nav class="{class_name}" aria-label="Navegação entre capítulos">', "  <ul>"]
    parts.append('    <li><a href="../../">Índice da obra</a></li>')
    parts.append('    <li><a href="#conteudo-capitulo">Início do capítulo</a></li>')
    parts.append('    <li class="spacer" aria-hidden="true"></li>')
    if previous:
        parts.append(f'    <li><a rel="prev" href="{rel_href(current, previous)}">← Cap. {previous.number}: {previous.title}</a></li>')
    if following:
        parts.append(f'    <li><a rel="next" href="{rel_href(current, following)}">Cap. {following.number}: {following.title} →</a></li>')
    parts.extend(["  </ul>", "</nav>", END])
    return "\n".join(parts)


def strip_generated(text: str) -> str:
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    return pattern.sub("", text)


def inject_css(text: str) -> str:
    if ".reader-nav{" in text:
        return text
    return text.replace("</style>", CSS + "\n</style>", 1)


def inject_landmark(text: str) -> str:
    return text.replace("<main>", '<main id="conteudo-capitulo">', 1)


def inject_navigation(text: str, index: int) -> str:
    top = nav_html(index)
    bottom = nav_html(index, bottom=True)
    text = text.replace('<main id="conteudo-capitulo">', '<main id="conteudo-capitulo">\n' + top, 1)
    footer_match = re.search(r"<footer\b", text)
    if footer_match:
        text = text[: footer_match.start()] + bottom + "\n" + text[footer_match.start() :]
    else:
        text = text.replace("</main>", bottom + "\n</main>", 1)
    return text


def main() -> None:
    for index, chapter in enumerate(CHAPTERS):
        path = ROOT / chapter.path
        original = path.read_text(encoding="utf-8")
        updated = strip_generated(original)
        updated = inject_css(updated)
        updated = inject_landmark(updated)
        updated = inject_navigation(updated, index)
        path.write_text(updated, encoding="utf-8")
        print(f"atualizado: {chapter.path}")


if __name__ == "__main__":
    main()
