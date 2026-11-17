# Awesome Seedance 2.5 Flash API Prompts

[![Seedance 2.5 Flash on PoYo](https://img.shields.io/badge/Try%20on%20PoYo-seedance--2.5--flash-84cc16)](https://poyo.ai/models/seedance-2-5-flash?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedance-2.5-flash-api-prompts) [![API docs](https://img.shields.io/badge/API-docs-22d3ee)](https://docs.poyo.ai/api-manual/video-series/seedance-2-5-flash?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedance-2.5-flash-api-prompts) [![Prompts](https://img.shields.io/badge/prompts-30-f97316)](#prompt-index)

A curated library of **30 Seedance 2.5 Flash API prompts**, each with the exact request JSON for the PoYo API, a recommended duration and resolution, and an estimated cost. Categories: product ads, cinematic shots, character consistency with reference images, first and last frames, camera moves, and UGC talking heads.

Every request uses model `seedance-2.5-flash` and only fields from the [Seedance 2.5 Flash API reference](https://docs.poyo.ai/api-manual/video-series/seedance-2-5-flash?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedance-2.5-flash-api-prompts). The same request bodies also work with the Seedance 2.5 API: change the model to `seedance-2.5` (which adds 1080p). Prices differ; see the [Seedance 2.5 model page](https://poyo.ai/models/seedance-2-5?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedance-2.5-flash-api-prompts).

Last verified against the live PoYo schema and pricing on **November 17, 2026**.

## Table of contents

- [Quickstart](#quickstart)
- [Prompt index](#prompt-index)
- [Product ads](#product-ads)
- [Cinematic](#cinematic)
- [Character consistency with references](#character-consistency)
- [First frame and first-last frame](#first-last-frame)
- [Camera moves](#camera-moves)
- [UGC and talking head](#ugc-talking-head)
- [Example outputs](#example-outputs)
- [Prompt-writing rules for Seedance 2.5 Flash](#prompt-writing-rules-for-seedance-25-flash)
- [Pricing used for the estimates](#pricing-used-for-the-estimates)
- [Public input media](#public-input-media)
- [Contributing](#contributing)
- [Links](#links)

## Quickstart

1. Create a PoYo API key in the [dashboard](https://poyo.ai/dashboard/api-key?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedance-2.5-flash-api-prompts) and export it as `POYO_API_KEY`.
2. Submit any file in [`requests/`](requests):

```bash
curl -X POST "https://api.poyo.ai/api/generate/submit" \
  -H "Authorization: Bearer $POYO_API_KEY" \
  -H "Content-Type: application/json" \
  -d @requests/07-red-car-mountain-rain.json
```

3. Save `data.task_id` from the response and poll `GET https://api.poyo.ai/api/generate/status/{task_id}` until `status` is `finished` or `failed`, or add a `callback_url` to the request.

Runnable Python, Node.js, and cURL clients that accept these request files are in [Seedance-2.5-Flash-API](https://github.com/PoyoAPI/Seedance-2.5-Flash-API), for example `python python/generate.py ../awesome-seedance-2.5-flash-api-prompts/requests/07-red-car-mountain-rain.json`.

## Prompt index

| # | Prompt | Category | Mode | Settings | Est. credits (USD) |
| --- | --- | --- | --- | --- | --- |
| [01](#01-perfume-hero-shot) | Perfume bottle hero shot | Product ads | Text-to-video | 8 s · 720p · 16:9 | 328 ($1.64) |
| [02](#02-sneaker-splash) | Sneaker splash, vertical | Product ads | Text-to-video | 6 s · 720p · 9:16 | 246 ($1.23) |
| [03](#03-metal-logo-reveal) | Metal logo reveal from a reference image | Product ads | Reference (1 image) | 5 s · 720p · 16:9 | 205 ($1.025) |
| [04](#04-ice-cream-summer-spot) | Ice-cream summer spot from a first frame | Product ads | First frame | 6 s · 480p · auto | 111 ($0.555) |
| [05](#05-skincare-voiceover) | Skincare ad with a spoken line | Product ads | Text-to-video | 10 s · 720p · 9:16 | 410 ($2.05) |
| [06](#06-harbor-letter-30s) | 30-second single take: the harbor letter | Cinematic | Text-to-video | 30 s · 720p · 16:9 | 1,230 ($6.15) |
| [07](#07-red-car-mountain-rain) | Red sports car in mountain rain | Cinematic | Text-to-video | 5 s · 720p · 16:9 | 205 ($1.025) |
| [08](#08-desert-caravan-ultrawide) | Desert caravan, ultrawide | Cinematic | Text-to-video | 10 s · 720p · 21:9 | 410 ($2.05) |
| [09](#09-noir-detective-dialogue) | Rain-soaked noir with dialogue | Cinematic | Text-to-video | 8 s · 720p · 16:9 | 328 ($1.64) |
| [10](#10-kelp-forest-diver) | Underwater kelp forest | Cinematic | Text-to-video | 6 s · 720p · 16:9 | 246 ($1.23) |
| [11](#11-fox-snowy-village) | Same fox, new world | Character consistency with references | Reference (1 image) | 8 s · 720p · 16:9 | 328 ($1.64) |
| [12](#12-fox-motion-transfer) | Motion transfer from a reference video | Character consistency with references | Reference (1 image + 1 video) | 6 s · 480p · 16:9 | 92 ($0.46) |
| [13](#13-fox-audio-rhythm) | Character plus an audio reference | Character consistency with references | Reference (1 image + 1 audio) | 5 s · 480p · 16:9 | 92.5 ($0.4625) |
| [14](#14-guitarist-rooftop) | Same musician, new stage | Character consistency with references | Reference (1 image) | 8 s · 720p · 16:9 | 328 ($1.64) |
| [15](#15-musician-and-fox-campfire) | Two references in one scene | Character consistency with references | Reference (2 images) | 10 s · 720p · 16:9 | 410 ($2.05) |
| [16](#16-ice-cream-to-coral-room) | Surreal transition between two frames | First frame and first-last frame | First + last frame | 5 s · 720p · auto | 205 ($1.025) |
| [17](#17-fox-first-frame) | Continue the motion from a first frame | First frame and first-last frame | First frame | 5 s · 480p · auto | 92.5 ($0.4625) |
| [18](#18-coral-room-finish-table) | Finish the action in a still | First frame and first-last frame | First frame | 6 s · 720p · auto | 246 ($1.23) |
| [19](#19-logo-light-sweep) | Bring a logo still to life | First frame and first-last frame | First frame | 4 s · 480p · auto | 74 ($0.37) |
| [20](#20-storefront-day-to-night) | Day-to-night time-lapse (bring your own frames) | First frame and first-last frame | First + last frame | 6 s · 720p · auto | 246 ($1.23) |
| [21](#21-ceramicist-push-in) | Slow push-in on hands at work | Camera moves | Text-to-video | 5 s · 720p · 16:9 | 205 ($1.025) |
| [22](#22-dolly-zoom-cliff) | Dolly zoom at a cliff edge | Camera moves | Text-to-video | 5 s · 720p · 16:9 | 205 ($1.025) |
| [23](#23-orbit-chef-plating) | Orbit around a chef plating | Camera moves | Text-to-video | 6 s · 720p · 16:9 | 246 ($1.23) |
| [24](#24-fpv-waterfall-canyon) | FPV drone dive through a canyon | Camera moves | Text-to-video | 8 s · 720p · 16:9 | 328 ($1.64) |
| [25](#25-timelapse-camera-reference) | Borrow a camera style from a reference video | Camera moves | Reference (1 video) | 6 s · 480p · 16:9 | 184 ($0.92) |
| [26](#26-ugc-serum-selfie-review) | Selfie product review | UGC and talking head | Text-to-video | 10 s · 720p · 9:16 | 410 ($2.05) |
| [27](#27-guitarist-intro-talking-head) | Talking head from a portrait | UGC and talking head | First frame | 8 s · 720p · auto | 328 ($1.64) |
| [28](#28-pov-unboxing-hands) | POV unboxing, hands only | UGC and talking head | Text-to-video | 8 s · 480p · 9:16 | 148 ($0.74) |
| [29](#29-street-interview) | Two-person street interview | UGC and talking head | Text-to-video | 8 s · 720p · 9:16 | 328 ($1.64) |
| [30](#30-chef-tip-tutorial) | Quick tutorial tip | UGC and talking head | Text-to-video | 10 s · 480p · 16:9 | 185 ($0.925) |

Running all 30 requests once costs about 8,400 credits ($42.00). Prompt 20 is a template and needs your own frames.

<a id="product-ads"></a>
## Product ads

<a id="01-perfume-hero-shot"></a>
### 01. Perfume bottle hero shot

**Mode:** Text-to-video · **Recommended:** 8 s, 720p, 16:9 · **Estimated cost:** 328 credits ($1.64) = 41 × 8 s

One product, one light change, one camera move: the model keeps the bottle sharp instead of inventing new props.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "Luxury perfume commercial. A faceted glass perfume bottle with amber liquid stands on a black marble plinth. A slow arc of warm light sweeps across the glass, throwing caustic reflections onto the marble, while fine mist drifts behind the bottle. Slow push-in from a medium shot to a close-up of the cap. Sound: a soft airy swell and a single deep piano note. No people, no subtitles, no on-screen text.",
    "duration": 8,
    "resolution": "720p",
    "aspect_ratio": "16:9"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/01-perfume-hero-shot.json`

<a id="02-sneaker-splash"></a>
### 02. Sneaker splash, vertical

**Mode:** Text-to-video · **Recommended:** 6 s, 720p, 9:16 · **Estimated cost:** 246 credits ($1.23) = 41 × 6 s

Vertical 9:16 with a single action beat fits Reels, Shorts, and TikTok ad slots.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "Vertical product ad. A white running sneaker drops in slow motion onto a shallow puddle on a dark rooftop at night. Water bursts outward in a crown splash, droplets catch neon-blue rim light, then the shoe lands and the camera tilts up to a low hero angle. Sound: a heavy splash, a bass hit, and city ambience. No logos, no subtitles, no on-screen text.",
    "duration": 6,
    "resolution": "720p",
    "aspect_ratio": "9:16"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/02-sneaker-splash.json`

<a id="03-metal-logo-reveal"></a>
### 03. Metal logo reveal from a reference image

**Mode:** Reference (1 image) · **Recommended:** 5 s, 720p, 16:9 · **Estimated cost:** 205 credits ($1.025) = 41 × 5 s

Telling the model to keep the letter shapes from @Image1 protects the mark while the scene around it moves.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "@Image1 is the brushed-metal PY logo. Start on an extreme macro of the brushed metal surface, then pull back slowly as a thin line of white light travels along the edges of the letters and reveals the full logo on a black background. Keep the letter shapes and proportions exactly as in @Image1. Sound: a low cinematic whoosh and a deep bass hit when the logo is fully revealed. No other text.",
    "reference_image_urls": [
      "https://storage.poyo.ai/qwen-image-3-pro/reference-material.jpg"
    ],
    "duration": 5,
    "resolution": "720p",
    "aspect_ratio": "16:9"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/03-metal-logo-reveal.json`

<a id="04-ice-cream-summer-spot"></a>
### 04. Ice-cream summer spot from a first frame

**Mode:** First frame · **Recommended:** 6 s, 480p, auto · **Estimated cost:** 111 credits ($0.555) = 18.5 × 6 s

Animating an existing product still keeps colors and composition; aspect_ratio auto follows the image.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "The pastel ice-cream scoops slowly soften in warm summer light. A drip runs down the side of the yellow cone, sugar crystals sparkle and tumble across the white floor, and the camera glides slowly from left to right along the row of cones. Sound: light playful ukulele music and a soft crunch of sugar. No people, no subtitles.",
    "image_urls": [
      "https://storage.poyo.ai/models/seedance-2-mini/examples/image-to-video-first-frame.jpg"
    ],
    "duration": 6,
    "resolution": "480p",
    "aspect_ratio": "auto"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/04-ice-cream-summer-spot.json`

<a id="05-skincare-voiceover"></a>
### 05. Skincare ad with a spoken line

**Mode:** Text-to-video · **Recommended:** 10 s, 720p, 9:16 · **Estimated cost:** 410 credits ($2.05) = 41 × 10 s

Quoted dialogue is generated as audio in the same pass, so a short voiceover needs no separate TTS step.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "Vertical beauty ad in a bright bathroom with morning sun. Close-up of a glass dropper releasing a single drop of clear serum onto a fingertip, then the camera rises to a woman in her thirties smoothing it onto her cheek and smiling into the mirror. A calm female voiceover says, \"Ten seconds in the morning. Glow all day.\" Soft water sounds and gentle ambient music. No subtitles, no on-screen text.",
    "duration": 10,
    "resolution": "720p",
    "aspect_ratio": "9:16"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/05-skincare-voiceover.json`

<a id="cinematic"></a>
## Cinematic

<a id="06-harbor-letter-30s"></a>
### 06. 30-second single take: the harbor letter

**Mode:** Text-to-video · **Recommended:** 30 s, 720p, 16:9 · **Estimated cost:** 1,230 credits ($6.15) = 41 × 30 s

Timestamped beats keep one subject and setting consistent across a full 30-second take. This is the text-to-video example from the PoYo API reference.

Example output: `media/01-landing-harbor-30s.mp4` (see [Example outputs](#example-outputs)).

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "One continuous 30-second story of the same young woman in a yellow raincoat delivering a handwritten letter across a small seaside town at dawn. 0-6s: wide aerial shot of the sleepy harbor town, fishing boats rocking, soft morning light; she rides an old bicycle down a cobblestone hill. 6-12s: tracking shot beside her as she weaves past a fish market, seagulls lifting off, a vendor waves at her. 12-18s: low-angle shot as she climbs a steep stone staircase carrying the bicycle, breathing hard, the letter tucked in her pocket. 18-24s: she knocks on a blue door at the top; an elderly man opens it and she hands him the letter. 24-30s: close-up of the man reading, his eyes filling with tears; he smiles and says softly, \"She remembered.\" Camera slowly pulls back to reveal the sunrise over the sea. Natural ambient sound: waves, gulls, bicycle bell, footsteps, gentle piano music. No subtitles, no on-screen text.",
    "duration": 30,
    "resolution": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/06-harbor-letter-30s.json`

<a id="07-red-car-mountain-rain"></a>
### 07. Red sports car in mountain rain

**Mode:** Text-to-video · **Recommended:** 5 s, 720p, 16:9 · **Estimated cost:** 205 credits ($1.025) = 41 × 5 s

A single tracking move plus 'stays sharp and consistent throughout' holds the hero object steady through fast motion.

Example output: `media/03-red-car-rain.mp4` (see [Example outputs](#example-outputs)).

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "Tracking shot alongside a red sports car carving through a winding mountain road in heavy rain. The camera keeps pace beside the car as it leans into a tight curve, spray rising from the tires, rain streaking past, headlights cutting through low clouds, dark pine forest and wet asphalt reflecting the light. The same red car stays sharp and consistent throughout. Sound: engine roar rising through the gears, tires hissing on wet asphalt, steady rain. No subtitles, no on-screen text.",
    "duration": 5,
    "resolution": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/07-red-car-mountain-rain.json`

<a id="08-desert-caravan-ultrawide"></a>
### 08. Desert caravan, ultrawide

**Mode:** Text-to-video · **Recommended:** 10 s, 720p, 21:9 · **Estimated cost:** 410 credits ($2.05) = 41 × 10 s

21:9 plus a slow lateral move reads as a film establishing shot.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "Ultrawide establishing shot of a camel caravan crossing towering sand dunes at golden hour. Long shadows stretch across the ripples, wind lifts fine sand from the dune crests, and the camera trucks slowly to the right, keeping the caravan small against the vast landscape. Sound: wind over sand, soft camel bells, a low cello drone. No subtitles, no on-screen text.",
    "duration": 10,
    "resolution": "720p",
    "aspect_ratio": "21:9"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/08-desert-caravan-ultrawide.json`

<a id="09-noir-detective-dialogue"></a>
### 09. Rain-soaked noir with dialogue

**Mode:** Text-to-video · **Recommended:** 8 s, 720p, 16:9 · **Estimated cost:** 328 credits ($1.64) = 41 × 8 s

Lighting, wardrobe, and one quoted line give a complete scene in eight seconds.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "Black-and-white film noir. A detective in a trench coat and fedora stands under a flickering streetlamp in the rain, lighting a match that briefly illuminates his tired face. He looks down the empty street and mutters, \"She was never coming back.\" Slow push-in to a close-up as the match goes out. Sound: heavy rain, distant thunder, a lonely saxophone. No subtitles, no on-screen text.",
    "duration": 8,
    "resolution": "720p",
    "aspect_ratio": "16:9"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/09-noir-detective-dialogue.json`

<a id="10-kelp-forest-diver"></a>
### 10. Underwater kelp forest

**Mode:** Text-to-video · **Recommended:** 6 s, 720p, 16:9 · **Estimated cost:** 246 credits ($1.23) = 41 × 6 s

Naming light behavior (shafts, particles) and a slow pace gives calm, high-detail underwater footage.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "A free diver glides slowly through a towering kelp forest, sunlight falling in shafts through the green water, small silver fish scattering as she passes and particles drifting in the light. The camera follows from behind and slightly below, then she turns and swims up toward the bright surface. Sound: muffled underwater ambience, gentle bubbles, a soft ambient pad. No subtitles, no on-screen text.",
    "duration": 6,
    "resolution": "720p",
    "aspect_ratio": "16:9"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/10-kelp-forest-diver.json`

<a id="character-consistency"></a>
## Character consistency with references

<a id="11-fox-snowy-village"></a>
### 11. Same fox, new world

**Mode:** Reference (1 image) · **Recommended:** 8 s, 720p, 16:9 · **Estimated cost:** 328 credits ($1.64) = 41 × 8 s

One reference image with an explicit identity line ('the same fox, the same brass compass') carries the character into a new setting.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "@Image1 is the red fox with the brass compass on a cord. The same fox walks through a snowy mountain village at night, past glowing windows and a wooden sled, stops, and looks back at the camera as snowflakes land on its fur. Keep its face, fur colors, and the brass compass exactly as in @Image1. Sound: crunching snow, distant bells, soft wind. No subtitles.",
    "reference_image_urls": [
      "https://storage.poyo.ai/models/seedance-2-5/examples/inputs/reference-fox-image.webp"
    ],
    "duration": 8,
    "resolution": "720p",
    "aspect_ratio": "16:9"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/11-fox-snowy-village.json`

<a id="12-fox-motion-transfer"></a>
### 12. Motion transfer from a reference video

**Mode:** Reference (1 image + 1 video) · **Recommended:** 6 s, 480p, 16:9 · **Estimated cost:** 92 credits ($0.46) = 11.5 × (6 s output + 2 s reference video)

@Image1 sets who, @Video1 sets how it moves and how the camera follows. A reference video changes billing to output plus reference seconds.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "Use @Image1 for the red fox with its brass compass. Follow the trotting rhythm and side-tracking camera of @Video1. The fox trots along a path in an autumn city park, orange leaves swirling around its paws, warm late-afternoon light. Sound: rustling leaves and distant city traffic. No subtitles.",
    "reference_image_urls": [
      "https://storage.poyo.ai/models/seedance-2-5/examples/inputs/reference-fox-image.webp"
    ],
    "reference_video_urls": [
      "https://storage.poyo.ai/models/seedance-2-5/examples/inputs/reference-fox-motion.mp4"
    ],
    "duration": 6,
    "resolution": "480p",
    "aspect_ratio": "16:9"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/12-fox-motion-transfer.json`

<a id="13-fox-audio-rhythm"></a>
### 13. Character plus an audio reference

**Mode:** Reference (1 image + 1 audio) · **Recommended:** 5 s, 480p, 16:9 · **Estimated cost:** 92.5 credits ($0.4625) = 18.5 × 5 s

Audio references must be paired with a reference image or video; give @Audio1 one job (rhythm and mood).

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "@Image1 is the red fox with the brass compass. The fox explores a quiet misty meadow at sunrise, pausing to sniff wildflowers and then bounding forward. Match the rhythm and mood of @Audio1 in the pacing of its movement. No subtitles.",
    "reference_image_urls": [
      "https://storage.poyo.ai/models/seedance-2-5/examples/inputs/reference-fox-image.webp"
    ],
    "reference_audio_urls": [
      "https://storage.poyo.ai/models/seedance-2-5/examples/inputs/reference-fox-audio.mp3"
    ],
    "duration": 5,
    "resolution": "480p",
    "aspect_ratio": "16:9"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/13-fox-audio-rhythm.json`

<a id="14-guitarist-rooftop"></a>
### 14. Same musician, new stage

**Mode:** Reference (1 image) · **Recommended:** 8 s, 720p, 16:9 · **Estimated cost:** 328 credits ($1.64) = 41 × 8 s

Describing the outfit and instrument from the reference reinforces identity when the location changes.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "@Image1 is the bearded musician in the olive flannel shirt with his acoustic guitar. The same man sits on a rooftop at dusk with the city lights coming on behind him, strums the guitar, and sings softly, \"Late train home, I'm on my way.\" Slow orbit from his side to the front. Sound: acoustic guitar, his voice, light city ambience. No subtitles, no on-screen text.",
    "reference_image_urls": [
      "https://storage.poyo.ai/happy-horse-1-1/image-to-video-input.png"
    ],
    "duration": 8,
    "resolution": "720p",
    "aspect_ratio": "16:9"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/14-guitarist-rooftop.json`

<a id="15-musician-and-fox-campfire"></a>
### 15. Two references in one scene

**Mode:** Reference (2 images) · **Recommended:** 10 s, 720p, 16:9 · **Estimated cost:** 410 credits ($2.05) = 41 × 10 s

Each reference gets a role and a position in the frame, so the two characters do not blend.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "@Image1 is the bearded musician with his acoustic guitar; @Image2 is the red fox with the brass compass. At night in a pine forest, the musician sits on a log by a campfire on the left of the frame and plays a gentle melody, while the fox curls up on the right side, its ears twitching to the music. Firelight flickers on both. Slow push-in. Sound: crackling fire, acoustic guitar, crickets. No subtitles.",
    "reference_image_urls": [
      "https://storage.poyo.ai/happy-horse-1-1/image-to-video-input.png",
      "https://storage.poyo.ai/models/seedance-2-5/examples/inputs/reference-fox-image.webp"
    ],
    "duration": 10,
    "resolution": "720p",
    "aspect_ratio": "16:9"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/15-musician-and-fox-campfire.json`

<a id="first-last-frame"></a>
## First frame and first-last frame

<a id="16-ice-cream-to-coral-room"></a>
### 16. Surreal transition between two frames

**Mode:** First + last frame · **Recommended:** 5 s, 720p, auto · **Estimated cost:** 205 credits ($1.025) = 41 × 5 s

Describe the change between the frames, keep aspect_ratio auto, and use two images of the same shape (both 1024x576 here).

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "Surreal match-cut transition: the pastel ice-cream scoops melt into a flowing wave of color across the white floor, the wave rises and hardens into coral walls, and the scene settles into the coral room where a man kneels beside a wooden table under a mosaic canopy. Smooth continuous camera, no cuts. Sound: a soft liquid swoosh that turns into a calm room tone.",
    "image_urls": [
      "https://storage.poyo.ai/models/seedance-2-mini/examples/image-to-video-first-frame.jpg",
      "https://storage.poyo.ai/models/seedance-2-mini/examples/image-to-video-last-frame.jpg"
    ],
    "duration": 5,
    "resolution": "720p",
    "aspect_ratio": "auto"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/16-ice-cream-to-coral-room.json`

<a id="17-fox-first-frame"></a>
### 17. Continue the motion from a first frame

**Mode:** First frame · **Recommended:** 5 s, 480p, auto · **Estimated cost:** 92.5 credits ($0.4625) = 18.5 × 5 s

A cheap 480p first-frame draft: describe what happens next, not what is already in the image.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "The red fox lifts its head, sniffs the morning air, then breaks into a run and disappears between the ferns. The camera stays still as sunbeams shift through the mist. Soft birdsong and rustling leaves.",
    "image_urls": [
      "https://storage.poyo.ai/models/seedance-2-5/examples/inputs/reference-fox-image.webp"
    ],
    "duration": 5,
    "resolution": "480p",
    "aspect_ratio": "auto"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/17-fox-first-frame.json`

<a id="18-coral-room-finish-table"></a>
### 18. Finish the action in a still

**Mode:** First frame · **Recommended:** 6 s, 720p, auto · **Estimated cost:** 246 credits ($1.23) = 41 × 6 s

Give the subject in the first frame a clear goal and an ending pose.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "The man finishes fixing the chair leg, stands up, steps back to look at the table under the mosaic canopy, and nods with satisfaction as loose mosaic pieces on the floor flutter in a light breeze. Locked-off wide shot. Sound: a last tap of a mallet, footsteps, a soft breeze.",
    "image_urls": [
      "https://storage.poyo.ai/models/seedance-2-mini/examples/image-to-video-last-frame.jpg"
    ],
    "duration": 6,
    "resolution": "720p",
    "aspect_ratio": "auto"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/18-coral-room-finish-table.json`

<a id="19-logo-light-sweep"></a>
### 19. Bring a logo still to life

**Mode:** First frame · **Recommended:** 4 s, 480p, auto · **Estimated cost:** 74 credits ($0.37) = 18.5 × 4 s

Four seconds at 480p is the cheapest Seedance 2.5 Flash request (74 credits): ideal for testing a motion idea.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "A slow sweep of white light moves across the brushed-metal PY letters from left to right, catching the bevelled edges, while the camera drifts slightly closer. Keep the letters unchanged. Sound: a soft metallic shimmer. No other text.",
    "image_urls": [
      "https://storage.poyo.ai/qwen-image-3-pro/reference-material.jpg"
    ],
    "duration": 4,
    "resolution": "480p",
    "aspect_ratio": "auto"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/19-logo-light-sweep.json`

<a id="20-storefront-day-to-night"></a>
### 20. Day-to-night time-lapse (bring your own frames)

**Mode:** First + last frame · **Recommended:** 6 s, 720p, auto · **Estimated cost:** 246 credits ($1.23) = 41 × 6 s

Template: replace both URLs with a daytime and a nighttime photo of the same place, taken from the same position and with the same shape.

> Template: replace the `example.com` URLs with your own public image URLs before running.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "Locked-off time-lapse of the storefront: start from the daytime scene in the first frame, let the sky darken, the street lamps and shop lights turn on, and pedestrians blur past, and end exactly on the nighttime scene in the last frame. Soft city ambience.",
    "image_urls": [
      "https://example.com/your-storefront-day.jpg",
      "https://example.com/your-storefront-night.jpg"
    ],
    "duration": 6,
    "resolution": "720p",
    "aspect_ratio": "auto"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/20-storefront-day-to-night.json`

<a id="camera-moves"></a>
## Camera moves

<a id="21-ceramicist-push-in"></a>
### 21. Slow push-in on hands at work

**Mode:** Text-to-video · **Recommended:** 5 s, 720p, 16:9 · **Estimated cost:** 205 credits ($1.025) = 41 × 5 s

'The same pair of hands and the same bowl throughout' keeps the object stable during a slow push-in.

Example output: `media/02-ceramicist-hands.mp4` (see [Example outputs](#example-outputs)).

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "Close-up of a ceramicist's hands shaping wet clay on a spinning pottery wheel. Warm golden window light from the side, dust particles floating in the air, water glistening on the clay as the fingers press inward and the bowl rises and widens. Shallow depth of field, slow push-in, the same pair of hands and the same bowl throughout. Sound: the soft whir of the wheel, wet clay squelching, quiet studio ambience. No music, no subtitles, no on-screen text.",
    "duration": 5,
    "resolution": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/21-ceramicist-push-in.json`

<a id="22-dolly-zoom-cliff"></a>
### 22. Dolly zoom at a cliff edge

**Mode:** Text-to-video · **Recommended:** 5 s, 720p, 16:9 · **Estimated cost:** 205 credits ($1.025) = 41 × 5 s

Name the move and its visible effect: the subject stays the same size while the background stretches.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "Dolly zoom shot: a lone hiker in a red jacket stands at the edge of a sea cliff, framed from the waist up. The camera moves backward while zooming in, so the hiker stays the same size while the ocean and the cliffs behind her stretch and loom closer. Overcast light, wind whipping her hair. Sound: roaring wind, crashing waves far below, a rising tense string note. No subtitles.",
    "duration": 5,
    "resolution": "720p",
    "aspect_ratio": "16:9"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/22-dolly-zoom-cliff.json`

<a id="23-orbit-chef-plating"></a>
### 23. Orbit around a chef plating

**Mode:** Text-to-video · **Recommended:** 6 s, 720p, 16:9 · **Estimated cost:** 246 credits ($1.23) = 41 × 6 s

A 360-degree orbit around a fixed subject is one of the most reliable showcase moves.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "Smooth 360-degree orbit around a chef in a white jacket plating a dessert at a stainless-steel counter in a dim restaurant kitchen. Tweezers place an edible flower, a spoon draws a swoosh of raspberry sauce, and steam rises from a nearby pan in the warm backlight. Sound: kitchen clatter, a sizzling pan, quiet jazz from a radio. No subtitles, no on-screen text.",
    "duration": 6,
    "resolution": "720p",
    "aspect_ratio": "16:9"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/23-orbit-chef-plating.json`

<a id="24-fpv-waterfall-canyon"></a>
### 24. FPV drone dive through a canyon

**Mode:** Text-to-video · **Recommended:** 8 s, 720p, 16:9 · **Estimated cost:** 328 credits ($1.64) = 41 × 8 s

FPV language (dive, bank, skim) produces fast continuous motion without cuts.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "FPV drone shot: the camera dives off the top of a jungle waterfall, follows the falling water down the cliff, banks hard through mist and rainbows, then skims low over a turquoise river winding through a narrow canyon. Fast, smooth, continuous flight with no cuts. Sound: rushing water, wind noise, a driving electronic beat.",
    "duration": 8,
    "resolution": "720p",
    "aspect_ratio": "16:9"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/24-fpv-waterfall-canyon.json`

<a id="25-timelapse-camera-reference"></a>
### 25. Borrow a camera style from a reference video

**Mode:** Reference (1 video) · **Recommended:** 6 s, 480p, 16:9 · **Estimated cost:** 184 credits ($0.92) = 11.5 × (6 s output + 10 s reference video)

@Video1 supplies the locked-off framing and time-lapse pacing; the prompt supplies a new subject. Billed seconds = 6 output + 10 reference.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "Follow the locked-off framing and time-lapse pacing of @Video1. A closed red tulip in a clear glass jar on a sunny kitchen table slowly opens its petals over the course of the shot while the shadows of the window frame move across the table. Soft morning birdsong. No subtitles.",
    "reference_video_urls": [
      "https://storage.poyo.ai/happy-horse/flower-timelapse.mp4"
    ],
    "duration": 6,
    "resolution": "480p",
    "aspect_ratio": "16:9"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/25-timelapse-camera-reference.json`

<a id="ugc-talking-head"></a>
## UGC and talking head

<a id="26-ugc-serum-selfie-review"></a>
### 26. Selfie product review

**Mode:** Text-to-video · **Recommended:** 10 s, 720p, 9:16 · **Estimated cost:** 410 credits ($2.05) = 41 × 10 s

'Handheld selfie' plus casual dialogue gives native-looking UGC for paid social.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "Handheld vertical selfie video: a woman in her twenties in a sunlit bathroom holds a small amber glass serum bottle up to the camera and says casually, \"Okay, two weeks with this serum and my skin has never been this calm. Honestly, I'm obsessed.\" Natural slight camera shake, real room acoustics, faint birdsong outside the window. No subtitles, no on-screen text.",
    "duration": 10,
    "resolution": "720p",
    "aspect_ratio": "9:16"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/26-ugc-serum-selfie-review.json`

<a id="27-guitarist-intro-talking-head"></a>
### 27. Talking head from a portrait

**Mode:** First frame · **Recommended:** 8 s, 720p, auto · **Estimated cost:** 328 credits ($1.64) = 41 × 8 s

Start from a real portrait as the first frame; the spoken line and the action that follows animate it.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "The musician looks into the camera, smiles, and says, \"This one's called Late Train Home.\" Then he looks down at the guitar and starts strumming a slow folk melody. The lamp light flickers warmly behind him. Sound: his voice, acoustic guitar, quiet room tone.",
    "image_urls": [
      "https://storage.poyo.ai/happy-horse-1-1/image-to-video-input.png"
    ],
    "duration": 8,
    "resolution": "720p",
    "aspect_ratio": "auto"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/27-guitarist-intro-talking-head.json`

<a id="28-pov-unboxing-hands"></a>
### 28. POV unboxing, hands only

**Mode:** Text-to-video · **Recommended:** 8 s, 480p, 9:16 · **Estimated cost:** 148 credits ($0.74) = 18.5 × 8 s

Hands-only POV avoids face consistency issues and keeps the focus on the product.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "Vertical POV shot looking down at a wooden desk: two hands slide open a matte black gift box, lift tissue paper, and pull out a pair of white wireless earbuds in a charging case, then flip the case open toward the camera. Daylight from a nearby window. Sound: paper rustling, the soft click of the case, a quiet excited \"Oh, nice.\" No logos, no subtitles, no on-screen text.",
    "duration": 8,
    "resolution": "480p",
    "aspect_ratio": "9:16"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/28-pov-unboxing-hands.json`

<a id="29-street-interview"></a>
### 29. Two-person street interview

**Mode:** Text-to-video · **Recommended:** 8 s, 720p, 9:16 · **Estimated cost:** 328 credits ($1.64) = 41 × 8 s

Assign each line to a named speaker so dialogue lands on the right face.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "Vertical street interview on a busy city sidewalk in the afternoon. A young male interviewer holds a small microphone toward an older woman with silver hair and asks, \"What's the best advice you've ever gotten?\" She laughs and answers, \"Never skip breakfast, and never skip a chance to dance.\" Handheld camera, natural light, passersby in the background. Sound: street ambience, their voices. No subtitles, no on-screen text.",
    "duration": 8,
    "resolution": "720p",
    "aspect_ratio": "9:16"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/29-street-interview.json`

<a id="30-chef-tip-tutorial"></a>
### 30. Quick tutorial tip

**Mode:** Text-to-video · **Recommended:** 10 s, 480p, 16:9 · **Estimated cost:** 185 credits ($0.925) = 18.5 × 10 s

A 480p draft for an explainer: one speaker, one demonstration, one line of advice.

```json
{
  "model": "seedance-2.5-flash",
  "input": {
    "prompt": "A friendly chef in a home kitchen faces the camera, holds up a lemon, and says, \"Roll it on the counter first and you'll get twice the juice.\" He presses the lemon under his palm, rolls it, cuts it, and squeezes it into a glass bowl. Medium shot, bright natural light. Sound: his voice, the knife on the board, juice dripping. No subtitles, no on-screen text.",
    "duration": 10,
    "resolution": "480p",
    "aspect_ratio": "16:9"
  }
}
```

Run it: `curl -X POST https://api.poyo.ai/api/generate/submit -H "Authorization: Bearer $POYO_API_KEY" -H "Content-Type: application/json" -d @requests/30-chef-tip-tutorial.json`

## Example outputs

Real Seedance 2.5 Flash outputs for prompts in this library. Files are added to [`media/`](media) as they are rendered.

| Prompt | File | Settings | Status |
| --- | --- | --- | --- |
| [06. 30-second single take: the harbor letter](#06-harbor-letter-30s) | `media/01-landing-harbor-30s.mp4` | 30 s · 720p · 16:9 | [Watch](media/01-landing-harbor-30s.mp4) |
| [07. Red sports car in mountain rain](#07-red-car-mountain-rain) | `media/03-red-car-rain.mp4` | 5 s · 720p · 16:9 | [Watch](media/03-red-car-rain.mp4) |
| [21. Slow push-in on hands at work](#21-ceramicist-push-in) | `media/02-ceramicist-hands.mp4` | 5 s · 720p · 16:9 | [Watch](media/02-ceramicist-hands.mp4) |

## Prompt-writing rules for Seedance 2.5 Flash

- **One subject, one action, one camera move** per clip; add beats with timestamps for long takes (`0-6s: ... 6-12s: ...`).
- **Write the sound.** Audio is generated in the same pass by default: put dialogue in quotes and name ambience, effects, and music. Add "no music" to drop a layer, or set `generate_audio` to `false`.
- **Give every reference a role** by upload order: `@Image1`, `@Video1`, `@Audio1`. Audio references need at least one reference image or video.
- **Do not mix modes.** Send `image_urls` (first / last frame) and the `reference_*` fields in separate requests.
- **First and last frames:** keep `aspect_ratio` at `auto` and use two images of the same shape; describe the change between them.
- **Say what must not change** ("keep the letter shapes exactly as in @Image1", "the same red car stays sharp").
- **End with exclusions:** "No subtitles, no on-screen text" keeps burned-in captions out of the frame.
- **Draft at 480p, render at 720p.** Switch the model to `seedance-2.5` for 1080p.
- **Avoid real brands, logos you do not own, and named people.** Content review can reject such prompts; failed tasks are not charged.

## Pricing used for the estimates

From PoYo `models.json` (entry `seedance-2-5-flash`). 1 credit = $0.005. Billing is per second.

| Resolution | No reference video | With reference video |
| --- | --- | --- |
| 480p | 18.5 credits ($0.0925) per second | 11.5 credits ($0.0575) per billed second |
| 720p | 41 credits ($0.205) per second | 25.5 credits ($0.1275) per billed second |

With `reference_video_urls`, billed seconds are the output duration plus each reference video's duration floored to whole seconds. Reference images and audio do not change the rate. Confirm current prices on the [model page](https://poyo.ai/models/seedance-2-5-flash?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedance-2.5-flash-api-prompts) before a production rollout.

## Public input media

The reference and frame URLs below are public PoYo example files, so the requests run as-is.

| Key | URL | Content |
| --- | --- | --- |
| `FOX_IMAGE` | <https://storage.poyo.ai/models/seedance-2-5/examples/inputs/reference-fox-image.webp> | Red fox with a brass compass on a cord, misty forest, 1280x720 WebP |
| `FOX_VIDEO` | <https://storage.poyo.ai/models/seedance-2-5/examples/inputs/reference-fox-motion.mp4> | Fox trotting with a side-tracking camera, 2.21 s MP4 (billed as 2 s) |
| `FOX_AUDIO` | <https://storage.poyo.ai/models/seedance-2-5/examples/inputs/reference-fox-audio.mp3> | 5.0 s MP3 |
| `ICE_CREAM` | <https://storage.poyo.ai/models/seedance-2-mini/examples/image-to-video-first-frame.jpg> | Pastel ice-cream cones on a white set, 1024x576 JPEG |
| `CORAL_ROOM` | <https://storage.poyo.ai/models/seedance-2-mini/examples/image-to-video-last-frame.jpg> | Man assembling a table under a mosaic canopy in a coral room, 1024x576 JPEG |
| `GUITARIST` | <https://storage.poyo.ai/happy-horse-1-1/image-to-video-input.png> | Bearded man with an acoustic guitar in a lamp-lit library, 896x1200 PNG |
| `PY_LOGO` | <https://storage.poyo.ai/qwen-image-3-pro/reference-material.jpg> | Brushed-metal PY letters on black, 2304x1728 JPEG |
| `PEONY_TIMELAPSE` | <https://storage.poyo.ai/happy-horse/flower-timelapse.mp4> | Peony blooming in a white vase on a windowsill, locked-off time-lapse, 10.05 s MP4 (billed as 10 s) |

## Contributing

Pull requests with new prompts are welcome. Add an entry to [`prompts.json`](prompts.json) with a request that validates against the API reference, run `python scripts/build.py`, and include the rendered output if you have one. Do not include real brands, private people, or media you do not have rights to.

## Links

- [Seedance 2.5 Flash API on PoYo](https://poyo.ai/models/seedance-2-5-flash?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedance-2.5-flash-api-prompts)
- [Seedance 2.5 Flash API reference](https://docs.poyo.ai/api-manual/video-series/seedance-2-5-flash?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedance-2.5-flash-api-prompts)
- [Seedance-2.5-Flash-API](https://github.com/PoyoAPI/Seedance-2.5-Flash-API): cURL, Python, and Node.js examples
- [Seedance-2.5-API](https://github.com/PoyoAPI/Seedance-2.5-API): Seedance 2.5 with 1080p
- [awesome-poyo-api](https://github.com/PoyoAPI/awesome-poyo-api): every PoYo model repository
- [poyo-devtools](https://github.com/PoyoAPI/poyo-devtools): PoYo CLI, MCP bridge (tool `poyo_seedance_2_5_flash`), and Agent Skill

## License

[MIT](LICENSE)
