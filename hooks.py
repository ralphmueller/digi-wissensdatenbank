"""
MkDocs Hook: Injects the 4 most recently updated pages into index.md.
Replace the placeholder <!-- RECENT_ENTRIES --> in index.md with a list.
"""

from pathlib import Path


def on_page_markdown(markdown, page, config, **kwargs):
    if page.file.src_path != "index.md":
        return markdown

    docs_dir = Path(config["docs_dir"])
    skip_names = {"index.md", "tags.md", "about.md"}
    skip_dirs = {"99-intern"}

    entries = []

    for md_file in docs_dir.rglob("*.md"):
        rel = md_file.relative_to(docs_dir)

        if rel.name in skip_names:
            continue
        if any(part in skip_dirs for part in rel.parts):
            continue

        content = md_file.read_text(encoding="utf-8")
        fm = _parse_frontmatter(content)

        updated = fm.get("updated", "")
        title = fm.get("title", rel.stem)
        page_type = fm.get("type", "")

        # Use .md links so MkDocs resolves them correctly
        url = str(rel.as_posix())

        entries.append({"title": title, "updated": updated, "type": page_type, "url": url})

    entries.sort(key=lambda x: x["updated"], reverse=True)
    top4 = entries[:4]

    type_labels = {"term": "Glossar", "howto": "Anleitung", "article": "Artikel"}

    lines = ["## Zuletzt aktualisiert\n"]
    for e in top4:
        label = type_labels.get(e["type"], e["type"].capitalize() if e["type"] else "")
        date_part = f" — {_format_date(e['updated'])}" if e["updated"] else ""
        label_part = f" ({label})" if label else ""
        lines.append(f"- [{e['title']}]({e['url']}){label_part}{date_part}")

    section = "\n".join(lines)

    if "<!-- RECENT_ENTRIES -->" in markdown:
        return markdown.replace("<!-- RECENT_ENTRIES -->", section)

    return markdown + "\n\n" + section


def _format_date(date_str: str) -> str:
    try:
        y, m, d = date_str.split("-")
        return f"{d}.{m}.{y}"
    except ValueError:
        return date_str


def _parse_frontmatter(content: str) -> dict:
    fm = {}
    if not content.startswith("---"):
        return fm
    end = content.find("---", 3)
    if end == -1:
        return fm
    for line in content[3:end].splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip()
    return fm
