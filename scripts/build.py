"""Build README.md and requests/*.json from prompts.json.

Prices come from PoYo's models.json (entry "seedance-2-5-flash"). The script reads
it from --models <path>, or from the poyoapi checkout via git, and stores the
rates it used in pricing.json so the repo can be rebuilt without models.json.

    python scripts/build.py
    python scripts/build.py --models path/to/models.json
"""
from __future__ import annotations

import argparse
import json
import subprocess
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "awesome-seedance-2.5-flash-api-prompts"
CAMPAIGN = REPO
MODEL_ENTRY = "seedance-2-5-flash"
VERIFIED = "November 17, 2026"
CREDIT_USD = Decimal("0.005")


def utm(url: str) -> str:
    return f"{url}{'&' if '?' in url else '?'}utm_source=github&utm_medium=readme&utm_campaign={CAMPAIGN}"


def load_rates(models_path: str | None) -> dict:
    text = None
    if models_path:
        text = Path(models_path).read_text(encoding="utf-8")
    else:
        try:
            text = subprocess.run(["git", "-C", "C:/code/poyoapi", "show", "origin/main:data/models.json"],
                                  check=True, capture_output=True).stdout.decode("utf-8")
        except (OSError, subprocess.CalledProcessError):
            text = None
    if text is None:
        return json.loads((ROOT / "pricing.json").read_text(encoding="utf-8"))
    entry = next(m for m in json.loads(text) if m["id"] == MODEL_ENTRY)
    rates = {"source": "PoYo models.json, entry seedance-2-5-flash", "updatedAt": entry.get("updatedAt"), "no_video": {}, "with_video": {}}
    for t in entry["pricingTiers"]:
        key = "with_video" if (t.get("dims") or {}).get("videoInput") else "no_video"
        rates[key][t["resolution"]] = {"credits": t["credits"], "usd": t["priceUSD"], "unit": t["unit"]}
    (ROOT / "pricing.json").write_text(json.dumps(rates, indent=2) + "\n", encoding="utf-8", newline="\n")
    return rates


def fmt_num(d: Decimal) -> str:
    s = format(d.normalize(), "f")
    if "." in s:
        whole, frac = s.split(".")
        return f"{int(whole):,}.{frac}"
    return f"{int(s):,}"


def usd(d: Decimal) -> str:
    s = format(d.normalize(), "f")
    if "." not in s:
        return f"${s}.00"
    whole, frac = s.split(".")
    return f"${whole}.{frac.ljust(2, '0')}"


def substitute(value, media: dict):
    if isinstance(value, str):
        for key, url in media.items():
            value = value.replace("{" + key + "}", url)
        return value
    if isinstance(value, list):
        return [substitute(v, media) for v in value]
    if isinstance(value, dict):
        return {k: substitute(v, media) for k, v in value.items()}
    return value


def mode_of(inp: dict) -> str:
    refs = [k for k in ("reference_image_urls", "reference_video_urls", "reference_audio_urls") if inp.get(k)]
    if refs:
        parts = []
        for key, noun in (("reference_image_urls", "image"), ("reference_video_urls", "video"), ("reference_audio_urls", "audio")):
            n = len(inp.get(key) or [])
            if n:
                parts.append(f"{n} {noun}{'s' if n > 1 and noun != 'audio' else ''}")
        return "Reference (" + " + ".join(parts) + ")"
    if inp.get("image_urls"):
        return "First + last frame" if len(inp["image_urls"]) == 2 else "First frame"
    return "Text-to-video"


def cost(inp: dict, raw_inp: dict, data: dict, rates: dict) -> tuple[Decimal, str]:
    res = inp.get("resolution", "720p")
    dur = Decimal(inp["duration"])
    ref_keys = [v.strip("{}") for v in raw_inp.get("reference_video_urls", [])]
    if ref_keys:
        ref_seconds = sum(Decimal(data["reference_video_seconds"][k]) for k in ref_keys)
        rate = Decimal(str(rates["with_video"][res]["credits"]))
        billed = dur + ref_seconds
        return rate * billed, f"{fmt_num(rate)} × ({dur} s output + {ref_seconds} s reference video)"
    rate = Decimal(str(rates["no_video"][res]["credits"]))
    return rate * dur, f"{fmt_num(rate)} × {dur} s"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--models")
    args = ap.parse_args()
    data = json.loads((ROOT / "prompts.json").read_text(encoding="utf-8"))
    rates = load_rates(args.models)
    media, model = data["media"], data["model"]
    cats = {c["id"]: c["title"] for c in data["categories"]}

    req_dir = ROOT / "requests"
    req_dir.mkdir(exist_ok=True)
    for old in req_dir.glob("*.json"):
        old.unlink()

    rows, sections = [], {c: [] for c in cats}
    total = Decimal(0)
    for p in data["prompts"]:
        inp = substitute(p["input"], media)
        body = {"model": model, "input": inp}
        fname = f"{p['id']}-{p['slug']}.json"
        (req_dir / fname).write_text(json.dumps(body, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
        credits, formula = cost(inp, p["input"], data, rates)
        total += credits
        anchor = f"{p['id']}-{p['slug']}"
        rows.append(f"| [{p['id']}](#{anchor}) | {p['title']} | {cats[p['category']]} | {mode_of(inp)} | {inp['duration']} s · {inp.get('resolution', '720p')} · {inp.get('aspect_ratio', 'auto')} | {fmt_num(credits)} ({usd(credits * CREDIT_USD)}) |")
        block = [f'<a id="{anchor}"></a>', f"### {p['id']}. {p['title']}", ""]
        block.append(f"**Mode:** {mode_of(inp)} · **Recommended:** {inp['duration']} s, {inp.get('resolution', '720p')}, {inp.get('aspect_ratio', 'auto')} · **Estimated cost:** {fmt_num(credits)} credits ({usd(credits * CREDIT_USD)}) = {formula}")
        block += ["", p["why"], ""]
        if p.get("byo"):
            block += ["> Template: replace the `example.com` URLs with your own public image URLs before running.", ""]
        if p.get("media_file"):
            block += [f"Example output: `{p['media_file']}` (see [Example outputs](#example-outputs)).", ""]
        block += ["```json", json.dumps(body, indent=2, ensure_ascii=False), "```", "",
                  f"Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H \"Authorization: Bearer $POYO_API_KEY\" -H \"Content-Type: application/json\" -d @requests/{fname}`", ""]
        sections[p["category"]].append("\n".join(block))

    nv, wv = rates["no_video"], rates["with_video"]
    out = []
    out += [
        "# Awesome Seedance 2.5 Flash API Prompts",
        "",
        f"[![Seedance 2.5 Flash on PoYo](https://img.shields.io/badge/Try%20on%20PoYo-seedance--2.5--flash-84cc16)]({utm('https://poyo.ai/models/seedance-2-5-flash')}) [![API docs](https://img.shields.io/badge/API-docs-22d3ee)]({utm('https://docs.poyo.ai/api-manual/video-series/seedance-2-5-flash')}) [![Prompts](https://img.shields.io/badge/prompts-{len(data['prompts'])}-f97316)](#prompt-index)",
        "",
        f"A curated library of **{len(data['prompts'])} Seedance 2.5 Flash API prompts**, each with the exact request JSON for the PoYo API, a recommended duration and resolution, and an estimated cost. Categories: product ads, cinematic shots, character consistency with reference images, first and last frames, camera moves, and UGC talking heads.",
        "",
        "Every request uses model `seedance-2.5-flash` and only fields from the [Seedance 2.5 Flash API reference](" + utm("https://docs.poyo.ai/api-manual/video-series/seedance-2-5-flash") + "). The same request bodies also work with the Seedance 2.5 API: change the model to `seedance-2.5` (which adds 1080p). Prices differ; see the [Seedance 2.5 model page](" + utm("https://poyo.ai/models/seedance-2-5") + ").",
        "",
        f"Last verified against the live PoYo schema and pricing on **{VERIFIED}**.",
        "",
        "## Table of contents",
        "",
        "- [Quickstart](#quickstart)",
        "- [Prompt index](#prompt-index)",
    ]
    for cid, title in cats.items():
        out.append(f"- [{title}](#{cid})")
    out += ["- [Example outputs](#example-outputs)", "- [Prompt-writing rules for Seedance 2.5 Flash](#prompt-writing-rules-for-seedance-25-flash)",
            "- [Pricing used for the estimates](#pricing-used-for-the-estimates)", "- [Public input media](#public-input-media)", "- [Contributing](#contributing)", "- [Links](#links)", ""]
    out += [
        "## Quickstart",
        "",
        f"1. Create a PoYo API key in the [dashboard]({utm('https://poyo.ai/dashboard/api-key')}) and export it as `POYO_API_KEY`.",
        "2. Submit any file in [`requests/`](requests):",
        "",
        "```bash",
        'curl -X POST "https://api.poyo.ai/api/generate/submit" \\',
        '  -H "Authorization: Bearer $POYO_API_KEY" \\',
        '  -H "Content-Type: application/json" \\',
        "  -d @requests/07-red-car-mountain-rain.json",
        "```",
        "",
        "3. Save `data.task_id` from the response and poll `GET https://api.poyo.ai/api/generate/status/{task_id}` until `status` is `finished` or `failed`, or add a `callback_url` to the request.",
        "",
        "Runnable Python, Node.js, and cURL clients that accept these request files are in [Seedance-2.5-Flash-API](https://github.com/PoyoAPI/Seedance-2.5-Flash-API), for example `python python/generate.py ../awesome-seedance-2.5-flash-api-prompts/requests/07-red-car-mountain-rain.json`.",
        "",
        "## Prompt index",
        "",
        "| # | Prompt | Category | Mode | Settings | Est. credits (USD) |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    out += rows
    out += ["", f"Running all {len(data['prompts'])} requests once costs about {fmt_num(total)} credits ({usd(total * CREDIT_USD)}). Prompt 20 is a template and needs your own frames.", ""]
    for cid, title in cats.items():
        out += [f'<a id="{cid}"></a>', f"## {title}", ""] + sections[cid]
    media_rows = [p for p in data["prompts"] if p.get("media_file")]
    out += [
        "## Example outputs",
        "",
        "Real Seedance 2.5 Flash outputs for prompts in this library. Files are added to [`media/`](media) as they are rendered.",
        "",
        "| Prompt | File | Settings | Status |",
        "| --- | --- | --- | --- |",
    ]
    for p in media_rows:
        inp = p["input"]
        added = (ROOT / p["media_file"]).is_file()
        status = f"[Watch]({p['media_file']})" if added else "TODO: add file"
        out.append(f"| [{p['id']}. {p['title']}](#{p['id']}-{p['slug']}) | `{p['media_file']}` | {inp['duration']} s · {inp['resolution']} · {inp['aspect_ratio']} | {status} |")
    out += [
        "",
        "## Prompt-writing rules for Seedance 2.5 Flash",
        "",
        "- **One subject, one action, one camera move** per clip; add beats with timestamps for long takes (`0-6s: ... 6-12s: ...`).",
        "- **Write the sound.** Audio is generated in the same pass by default: put dialogue in quotes and name ambience, effects, and music. Add \"no music\" to drop a layer, or set `generate_audio` to `false`.",
        "- **Give every reference a role** by upload order: `@Image1`, `@Video1`, `@Audio1`. Audio references need at least one reference image or video.",
        "- **Do not mix modes.** Send `image_urls` (first / last frame) and the `reference_*` fields in separate requests.",
        "- **First and last frames:** keep `aspect_ratio` at `auto` and use two images of the same shape; describe the change between them.",
        "- **Say what must not change** (\"keep the letter shapes exactly as in @Image1\", \"the same red car stays sharp\").",
        "- **End with exclusions:** \"No subtitles, no on-screen text\" keeps burned-in captions out of the frame.",
        "- **Draft at 480p, render at 720p.** Switch the model to `seedance-2.5` for 1080p.",
        "- **Avoid real brands, logos you do not own, and named people.** Content review can reject such prompts; failed tasks are not charged.",
        "",
        "## Pricing used for the estimates",
        "",
        f"From PoYo `models.json` (entry `seedance-2-5-flash`). 1 credit = $0.005. Billing is per second.",
        "",
        "| Resolution | No reference video | With reference video |",
        "| --- | --- | --- |",
        f"| 480p | {fmt_num(Decimal(str(nv['480p']['credits'])))} credits ({usd(Decimal(str(nv['480p']['usd'])))}) per second | {fmt_num(Decimal(str(wv['480p']['credits'])))} credits ({usd(Decimal(str(wv['480p']['usd'])))}) per billed second |",
        f"| 720p | {fmt_num(Decimal(str(nv['720p']['credits'])))} credits ({usd(Decimal(str(nv['720p']['usd'])))}) per second | {fmt_num(Decimal(str(wv['720p']['credits'])))} credits ({usd(Decimal(str(wv['720p']['usd'])))}) per billed second |",
        "",
        "With `reference_video_urls`, billed seconds are the output duration plus each reference video's duration floored to whole seconds. Reference images and audio do not change the rate. Confirm current prices on the " + f"[model page]({utm('https://poyo.ai/models/seedance-2-5-flash')}) before a production rollout.",
        "",
        "## Public input media",
        "",
        "The reference and frame URLs below are public PoYo example files, so the requests run as-is.",
        "",
        "| Key | URL | Content |",
        "| --- | --- | --- |",
    ]
    for key, url in media.items():
        out.append(f"| `{key}` | <{url}> | {data['media_notes'][key]} |")
    out += [
        "",
        "## Contributing",
        "",
        "Pull requests with new prompts are welcome. Add an entry to [`prompts.json`](prompts.json) with a request that validates against the API reference, run `python scripts/build.py`, and include the rendered output if you have one. Do not include real brands, private people, or media you do not have rights to.",
        "",
        "## Links",
        "",
        f"- [Seedance 2.5 Flash API on PoYo]({utm('https://poyo.ai/models/seedance-2-5-flash')})",
        f"- [Seedance 2.5 Flash API reference]({utm('https://docs.poyo.ai/api-manual/video-series/seedance-2-5-flash')})",
        "- [Seedance-2.5-Flash-API](https://github.com/PoyoAPI/Seedance-2.5-Flash-API): cURL, Python, and Node.js examples",
        "- [Seedance-2.5-API](https://github.com/PoyoAPI/Seedance-2.5-API): Seedance 2.5 with 1080p",
        "- [awesome-poyo-api](https://github.com/PoyoAPI/awesome-poyo-api): every PoYo model repository",
        "- [poyo-devtools](https://github.com/PoyoAPI/poyo-devtools): PoYo CLI, MCP bridge (tool `poyo_seedance_2_5_flash`), and Agent Skill",
        "",
        "## License",
        "",
        "[MIT](LICENSE)",
        "",
    ]
    (ROOT / "README.md").write_text("\n".join(out), encoding="utf-8", newline="\n")
    print(f"wrote README.md and {len(data['prompts'])} request files; total {fmt_num(total)} credits")


if __name__ == "__main__":
    main()
