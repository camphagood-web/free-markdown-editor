# Free Markdown Editor

A free, open-source desktop Markdown editor for macOS, Windows, and Linux. The app appears as **Markdown Editor** on macOS.

This project builds on [MarkText](https://github.com/marktext/marktext), an MIT-licensed WYSIWYG Markdown editor. It keeps MarkText's editor engine and file workflows, and adds a distinct macOS app identity, icon, and a simpler default writing style. The design was informed by observing Typora's installed app, but this project does not contain Typora's code or assets and is not affiliated with Typora.

## Features

- Live Markdown editing with CommonMark and GitHub Flavored Markdown support
- Tables, code blocks, math, diagrams, and source mode
- File and folder browsing, search, focus mode, and export to HTML or PDF
- A centered, distraction-free writing view by default

## Build from source

Requires Node.js 20.19 or newer and pnpm 10.33.4. The repository is a pnpm workspace; the desktop app lives in `packages/desktop`.

```sh
corepack enable
pnpm install --frozen-lockfile
pnpm run dev
```

To package the app for your platform:

```sh
pnpm run build:mac
# or: pnpm run build:win
# or: pnpm run build:linux
```

Build outputs go to `dist/`. macOS builds made without an Apple signing identity are unsigned and may require local approval to open on another Mac.

## Development checks

```sh
pnpm run build:unpack
pnpm run typecheck
pnpm run lint
```

## Credits and license

Free Markdown Editor is based on [MarkText](https://github.com/marktext/marktext) by Luo Ran and its contributors. The upstream copyright and MIT license are retained in [LICENSE](LICENSE). Third-party components retain their own licenses.
