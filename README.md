# Privacy for Small Business

A beginner-friendly manual for protecting your customers' data, using AI tools safely, and writing simple privacy policies — for small businesses, solo founders, freelancers, and author-LLCs. Includes a printable checklist. No jargon, no scare tactics, no legalese — just clear steps you can take today.

Published by **Asdale Dynamics, LLC** (Indiana, formed October 2026). Asdale Dynamics is a beginner-friendly AI education company founded by **Dylan Asdale**, a registered nurse turned AI author and founder of Asdale Dynamics. We explain things "like a friend would": plain English, step by step, never condescending. Learn more at [dylanasdale.github.io](https://dylanasdale.github.io).

---

## Who this is for

You run a small business — maybe an author LLC, an online shop, a freelance service, or a local shop — and you collect customer information: names, emails, orders, payment details. You want to handle that data responsibly, use AI tools without leaking customer info, and have simple policies in place. You don't have a legal team. This manual is written for you.

No technical or legal background needed. Read it in one sitting, or a section at a time.

---

## What's inside

| Path | Contents |
|------|----------|
| `docs/index.md` | Full manual in Markdown — customer data, AI tool safety, simple policies |
| `docs/checklist.md` | Printable checklist — actionable items grouped by category |
| `site/index.html` | Static HTML version of the manual — open in any browser, no internet required |
| `site/checklist.html` | Interactive printable checklist with localStorage progress |
| `site/assets/style.css` | Shared stylesheet for the HTML site |
| `LICENSE` | MIT License |

---

## Topics covered

1. **Customer data** — what you collect, where it lives, collecting less, storing safely, sharing with vendors, honoring deletion requests, breach response
2. **AI tool safety** — what never to paste into AI (customer data, contracts, financials, employee info), local models, disabling training, vetting AI vendors, AI meeting notetakers
3. **Simple policies** — privacy policy basics, data retention schedule, employee guidelines, vendor assessment checklist, incident response plan
4. **Printable checklist** — one-page reference for tracking your progress

---

## How to use

### Option 1: Read the Markdown manual

```bash
cat docs/index.md
# Or open docs/index.md in any Markdown viewer or editor
```

### Option 2: Open the static HTML site

No build step. No dependencies. Just open the file:

```bash
# macOS
open site/index.html

# Linux
xdg-open site/index.html

# Windows
start site/index.html
```

Or serve locally:

```bash
cd site && python3 -m http.server 8000
# Open http://localhost:8000
```

### Option 3: Print the checklist

Open `site/checklist.html` in your browser and use **File → Print**. The print stylesheet hides navigation and optimizes for paper.

---

## Run verification

A simple verification script checks HTML structure, internal links, CSS, required files, attribution, and scans for secrets:

```bash
./verify.sh
```

Or run the Python validator directly:

```bash
python3 verify.py
```

---

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See [`LICENSE`](LICENSE).

---

## Attribution

Created by **Asdale Dynamics, LLC** — a beginner-friendly AI education company founded by Dylan Asdale, registered nurse turned AI author. Dylan's book *The Massive AI Manual* and hub site [dylanasdale.github.io](https://dylanasdale.github.io) explain AI plainly, step by step, like a friend would.

**This guide is educational only. It is not legal advice.** Privacy laws vary by location and industry (for example, healthcare businesses may have additional obligations). For contracts, customer data handling, or regulatory questions, consult a qualified attorney or privacy professional.
