"""Génère les supports élèves et le guide enseignant P1 en HTML et PDF.

Exécution : python3 generer_pdf.py
Dépendances : markdown-it-py, weasyprint, PyYAML.
Le contenu est converti directement. Seul le front matter fournit les codes
imprimés en marge, sans classes ni identifiants ajoutés au HTML.
"""
from html import escape
import json
from pathlib import Path
import re

from markdown_it import MarkdownIt
from weasyprint import HTML
import yaml

ROOT = Path(__file__).resolve().parent
SOURCES = [ROOT / 'DIAGNOSTIC_S01.md', *sorted(ROOT.glob('S??_FICHES_ELEVES.md')), ROOT / 'BILAN_S07.md']


def read_student(source):
    text = source.read_text(encoding='utf-8')
    match = re.match(r'\A---\r?\n(.*?)\r?\n---\r?\n', text, re.S)
    if not match:
        raise ValueError(f'{source.name} : bloc codes_fiches manquant')
    metadata = yaml.safe_load(match[1])
    if not isinstance(metadata, dict) or set(metadata) != {'codes_fiches'}:
        raise ValueError(f'{source.name} : seule la clé codes_fiches est attendue')
    codes = metadata['codes_fiches']
    if (not isinstance(codes, list) or not codes
            or any(not isinstance(c, str) or not re.fullmatch(r'[A-Za-z0-9 -]{1,48}', c) for c in codes)):
        raise ValueError(f'{source.name} : codes invalides (lettres, chiffres, espaces, tirets ; 48 caractères maximum)')
    if len(set(codes)) != len(codes):
        raise ValueError(f'{source.name} : codes répétés')
    return text[match.end():].lstrip(), codes


def render(markdown, title, codes=None):
    student = codes is not None
    parser = MarkdownIt('commonmark')
    if not student:
        parser.enable('table')
    tokens = parser.parse(markdown)
    headings = sum(t.type == 'heading_open' and t.tag == 'h1' for t in tokens)
    if student and headings != len(codes):
        raise ValueError(f'{title} : {headings} titres # pour {len(codes)} codes ; un code par fiche requis')
    for token in tokens:
        for child in token.children or []:
            if child.type == 'link_open':
                href = child.attrGet('href') or ''
                if href and ':' not in href and not href.startswith(('#', '/')):
                    child.attrSet('href', '../' + href)
    body = parser.renderer.render(tokens, parser.options, {})
    stylesheet = 'style.css' if student else 'style_enseignant.css'
    css = (ROOT / stylesheet).read_text(encoding='utf-8')
    if student:
        # La correspondance ordinal/titre/page est contrôlée après composition.
        # Ces règles ne changent que le contenu du pied de page, pas sa mise en forme.
        css += '\n' + '\n'.join(
            f'@page :nth({n}) {{ @bottom-left {{ content: {json.dumps(code)}; }} }}'
            for n, code in enumerate(codes, 1))
    html = f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>{escape(title)}</title><style>{css}</style></head><body>{body}</body></html>'
    document = HTML(string=html, base_url=(ROOT / 'HTML').as_uri() + '/').render()
    validate(document, title, codes)
    return html, document


def validate(document, name, codes=None):
    if codes is not None and len(document.pages) != len(codes):
        raise ValueError(f'{name} : {len(document.pages)} pages pour {len(codes)} fiches. Une fiche déborde : répartir le contenu avec un nouveau titre # et ajouter son code avant de régénérer.')
    for number, page in enumerate(document.pages, 1):
        texts = []
        headings = set()
        for box in page._page_box.descendants():
            if box.element_tag == 'h1' and type(box).__name__ == 'BlockBox':
                headings.add(id(box.element))
            if not getattr(box, 'text', '').strip():
                continue
            texts.append(box.text)
            if (box.position_x < 0 or box.position_y < 0
                    or box.position_x + box.width > page.width + 1
                    or box.position_y + box.height > page.height + 1):
                raise ValueError(f'{name}, page {number} : débordement de {box.text!r}')
        if not texts:
            raise ValueError(f'{name}, page {number} : page vide')
        if codes is not None:
            text = ' '.join(texts)
            if text.count('Prénom :') != 1 or text.count('Date :') != 1:
                raise ValueError(f'{name}, page {number} : en-têtes absents ou répétés')
            if len(headings) != 1:
                raise ValueError(f'{name}, page {number} : un titre # par page requis pour fiabiliser le code')
            if texts.count(codes[number - 1]) != 1:
                raise ValueError(f'{name}, page {number} : code de fiche absent, coupé ou répété')


def main():
    # Composer et valider l'ensemble avant de remplacer les exports existants.
    exports = []
    contents, all_codes = [], []
    for source in SOURCES:
        markdown, codes = read_student(source)
        contents.append(markdown)
        all_codes.extend(codes)
        html, document = render(markdown, source.stem.replace('_', ' '), codes)
        exports.append((source.stem, html, document))
    if len(all_codes) != len(set(all_codes)):
        raise ValueError('Un même code est utilisé dans plusieurs fichiers élèves')
    html, document = render('\n\n'.join(contents), 'P1 — Recueil élèves', all_codes)
    exports.append(('P1_RECUEIL_ELEVES', html, document))
    source = ROOT / 'GUIDE_ENSEIGNANT.md'
    html, document = render(source.read_text(encoding='utf-8'), 'P1 — Guide enseignant synthétique')
    exports.append((source.stem, html, document))
    for folder in ['HTML', 'PDF']:
        (ROOT / folder).mkdir(exist_ok=True)
    for stem, html, document in exports:
        (ROOT / 'HTML' / f'{stem}.html').write_text(html, encoding='utf-8')
        document.write_pdf(ROOT / 'PDF' / f'{stem}.pdf')
        print(f'{stem} : {len(document.pages)} pages')


if __name__ == '__main__':
    main()
