"""Transport an already validated payload; matching and duplicate checks are in SKILL.md."""
import argparse
import json
import os
from pathlib import Path
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('payload', type=Path)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--dry-run', action='store_true')
group.add_argument('--yes', action='store_true')
args = parser.parse_args()
config_path = Path(__file__).resolve().parents[1] / 'references/target.json'
if not config_path.is_file():
    parser.error('Missing references/target.json; copy target.example.json and configure your team target first')
target = json.loads(config_path.read_text())
if not isinstance(target.get('share_token'), str) or not target['share_token'].startswith('shr'):
    parser.error('Configure a valid form share_token in references/target.json')
payload = json.loads(args.payload.read_text())
if not isinstance(payload.get('fields'), dict) or not payload['fields']:
    parser.error('payload must contain a nonempty fields object')
result = subprocess.run([
    'lark-cli', 'base', '+form-submit', '--share-token', target['share_token'],
    '--json', json.dumps(payload, ensure_ascii=False), '--as', 'user',
    '--dry-run' if args.dry_run else '--yes', '--format', 'json',
], env=dict(os.environ, LARKSUITE_CLI_NO_UPDATE_NOTIFIER='1', LARKSUITE_CLI_NO_SKILLS_NOTIFIER='1'))
raise SystemExit(result.returncode)
