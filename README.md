# The Trojan Horse

An M&A journal by Francis Ruan, live at https://trojanhorse.blog.

This repository is the whole website. The pages are static HTML that is **generated** by `build-site.py` from Python data modules. To change a page, edit its source and rebuild. Do not hand-edit the generated `.html` files, because the next build overwrites them.

## Quick start

```bash
git clone https://github.com/fyruan-star/trojanhorse-blog.git
cd trojanhorse-blog
python3 build-site.py          # Python 3, standard library only, nothing to install
python3 -m http.server 8731    # preview at http://localhost:8731/
```

A clean build reproduces the live site byte for byte. Pushing to `main` publishes it through GitHub Pages, usually within a minute and with no review step.

## Read next

- `HANDOFF.md` is the working guide: the current state of the site, which source file feeds which page, step-by-step procedures, editorial standards, a decision log and the open items.
- `CLAUDE.md` holds the standing rules for AI assistants. Claude Code loads it automatically when it is opened in this folder.

## Note on visibility

The repository is public and Pages serves every committed file, so nothing private belongs here: no keys, no personal data, no unpublished drafts. Retired writing lives in a local `archive/` folder that is git-ignored.
