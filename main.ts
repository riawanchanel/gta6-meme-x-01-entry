// gta6-meme-x-01 entry (Node 22, standard library only).
// The entry is the X post itself: POST.json at the repository root names the
// post, and this program copies it to the output directory where the gate
// reads it. Before copying, it self-checks POST.json: the url must be a real
// x.com status address, not the starter placeholder, so a misconfigured
// entry fails loudly here instead of at the gate.

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const postPath = join(BOT_DIR, 'POST.json');
let post: { url?: unknown };
try {
  post = JSON.parse(readFileSync(postPath, 'utf8'));
} catch (err) {
  console.error(`POST.json is missing or not valid JSON in ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}

const url = typeof post.url === 'string' ? post.url : '';
const status = /^https:\/\/(x\.com|twitter\.com)\/[^/]+\/status\/\d+$/.exec(url);
if (!status || url.includes('<') || url.includes('>')) {
  console.error(`POST.json does not name a real X post: ${url || '(empty url)'}`);
  process.exit(1);
}

mkdirSync(OUTPUT_DIR, { recursive: true });
copyFileSync(postPath, join(OUTPUT_DIR, 'POST.json'));
console.log(`POST.json OK: ${url}`);
