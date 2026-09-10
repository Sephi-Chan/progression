"""Conversion directe Markdown → HTML/PDF, sans classes ni habillage du contenu."""
from argparse import ArgumentParser
from html import escape
from pathlib import Path

from markdown_it import MarkdownIt
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('source', nargs='?', type=Path, default=ROOT / 'exemple.md')
    parser.add_argument('--pages', type=int, help='Nombre de pages attendu, si connu')
    args = parser.parse_args()
    source = args.source.resolve()
    body = MarkdownIt('commonmark').render(source.read_text(encoding='utf-8'))
    css = (ROOT / 'style.css').read_text(encoding='utf-8')
    html = f'''<!doctype html><html lang="fr"><head><meta charset="utf-8">
<title>{escape(source.stem)}</title><style>{css}</style></head>
<body>{body}</body></html>'''
    # Les sorties restent à côté du Markdown : ses liens relatifs restent valides.
    document = HTML(string=html, base_url=source.parent.as_uri() + '/').render()
    if args.pages is not None and len(document.pages) != args.pages:
        raise ValueError(f'{len(document.pages)} pages, {args.pages} attendues')
    for number, page in enumerate(document.pages, 1):
        for box in page._page_box.descendants():
            if not getattr(box, 'text', '').strip():
                continue
            if (box.position_x < 0 or box.position_y < 0
                    or box.position_x + box.width > page.width + 1
                    or box.position_y + box.height > page.height + 1):
                raise ValueError(f'Débordement page {number} : {box.text!r}')
    source.with_suffix('.html').write_text(html, encoding='utf-8')
    document.write_pdf(source.with_suffix('.pdf'))
    print(f'{source.with_suffix(".pdf")} : {len(document.pages)} pages')


if __name__ == '__main__':
    main()
