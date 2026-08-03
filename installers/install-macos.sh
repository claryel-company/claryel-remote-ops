#!/usr/bin/env bash
set -Eeuo pipefail

# CLARYEL RemoteOps guided installer for macOS.
# Installs into the current user's Library and does not weaken Gatekeeper,
# FileVault, SIP, privacy controls or other macOS protections.

APP_ROOT="$HOME/Library/Application Support/CLARYEL/RemoteOps"
APP_DIR="$APP_ROOT/app"
STATE_DIR="$APP_ROOT/state"
BIN_DIR="$HOME/.local/bin"
REPOSITORY_URL="https://github.com/claryel-company/claryel-remote-ops.git"

say() { printf '\n%s\n' "$*"; }
fail() { printf '\nERROR: %s\n' "$*" >&2; exit 1; }

[[ "$(uname -s)" == "Darwin" ]] || fail "This installer is for macOS."

command -v python3 >/dev/null 2>&1 || fail "Python 3 is required. Install it from python.org or Homebrew, then run this installer again."
command -v git >/dev/null 2>&1 || fail "Git is required. Run 'xcode-select --install', then run this installer again."

mkdir -p "$APP_ROOT" "$BIN_DIR"
chmod 700 "$APP_ROOT"

if [[ -d "$APP_DIR/.git" ]]; then
  say "Updating the public RemoteOps application..."
  git -C "$APP_DIR" fetch --depth 1 origin main
  git -C "$APP_DIR" reset --hard origin/main
else
  [[ ! -e "$APP_DIR" ]] || fail "$APP_DIR exists but is not a RemoteOps checkout."
  say "Downloading the public RemoteOps application..."
  git clone --depth 1 --branch main "$REPOSITORY_URL" "$APP_DIR"
fi

cat >"$BIN_DIR/remoteops" <<EOF
#!/usr/bin/env bash
exec python3 "$APP_DIR/src/remoteops.py" "\$@"
EOF
chmod 755 "$BIN_DIR/remoteops"

if [[ ! -d "$STATE_DIR/.git" ]]; then
  say "Creating your private local configuration workspace..."
  "$BIN_DIR/remoteops" init --path "$STATE_DIR"
fi

say "Checking the installation..."
"$BIN_DIR/remoteops" doctor
"$BIN_DIR/remoteops" status --path "$STATE_DIR"

cat <<EOF

CLARYEL RemoteOps is installed.

Application: $APP_DIR
Your private local workspace: $STATE_DIR
Command: $BIN_DIR/remoteops

IMPORTANT PRIVACY BOUNDARY
- Your personal files, passwords, keys, chats, raw logs and backups are not
  placed in Git by this installer.
- RemoteOps contacts GitHub only when you explicitly create or connect your
  private repository, and contacts an AI provider only when you choose to use it.
- Installing or updating software may contact the package sources you approve.
- This installer does not disable Gatekeeper, FileVault, SIP or macOS privacy controls.

NEXT STEP
Open the detailed private-repository guide:
$APP_DIR/docs/PRIVATE_REPOSITORY_SETUP.md

To create a private GitHub repository automatically after installing GitHub CLI:
  remoteops connect --path "$STATE_DIR" --create-private remoteops-my-computer

To verify privacy later:
  remoteops privacy-check --path "$STATE_DIR"
EOF

if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
  say "Add $BIN_DIR to PATH, for example:"
  printf '  echo '\''export PATH="%s:$PATH"'\'' >> "$HOME/.zprofile"\n' "$BIN_DIR"
fi
