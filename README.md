# The Trojan Horse

The website at **https://trojanhorse.blog**. Every change committed here goes live by itself in about two minutes.

## Change something

1. Open the file from the table below, here on GitHub.
2. Click the **pencil icon**, change the words, then click **Commit changes**.
3. Wait two minutes and refresh the site.

| To change | Open |
| --- | --- |
| Homepage tagline, essay, story order, podcast list | `content/home.py` |
| A Trojan Horse story | `content/stories/` |
| The Prologue timeline | `content/prologue.py` |
| Any other page | `content/` (file names match the pages) |
| Colours, fonts, layout | `assets/site.css` |
| Images and logos | `assets/images/` |

Change only the words inside the quotation marks. Keep tags such as `<p>` and `<a href="...">`. Write `&rsquo;` for an apostrophe, `&amp;` for &, and `&ldquo;` `&rdquo;` for quotation marks.

## Add a story

1. Copy `content/stories/uber.py` to `content/stories/yourname.py` and replace its words.
2. Put the company logo in `assets/images/logos/` and update `LOGO` in your file.
3. Add `"yourname"` to `STORIES` in `content/home.py`.

## If the site did not update

Open the **Actions** tab. A red ✗ means the edit broke the build. Click it to read the error, fix the file, and commit again. The site keeps showing the last good version until then.

## No edit access?

Click the pencil anyway. GitHub turns your edit into a pull request, and the owner publishes it.

---

House style and sourcing rules: `CLAUDE.md`. Full guide: `docs/HANDOFF.md`. Preview on your own computer (optional): `python3 build.py && python3 -m http.server -d _site 8731`.
