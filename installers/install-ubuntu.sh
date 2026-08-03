#!/usr/bin/env bash
set -Eeuo pipefail

# CLARYEL RemoteOps guided installer for Ubuntu.
# This script installs only into the current user's home directory unless it
# explicitly asks permission to install missing operating-system packages.

APP_ROOT="${XDG_DATA_HOME:-$HOME/.local/share}/claryel-remoteops"
APP_DIR="$APP_ROOT/app"
STATE_DIR="$APP_ROOT/state"
BIN_DIR="${XDG_BIN_HOME:-$HOME/.local/bin}"
REPOSITORY_URL="https://github.com/claryel-company/claryel-remote-ops.git"

say() { printf '\n%s\n' "$*"; }
fail() { printf '\nERROR: %s\n' "$*" >&2; exit 1; }
confirm() {
  local answer
  read -r -p "$1 [y/N] " answer || true
  [[ "$answer" =~ ^[Yy]$ ]]
}

[[ "$(uname -s)" == "Linux" ]] || fail "This installer is for Ubuntu Linux."

missing=()
for command in python3 git curl; do
  command -v "$command" >/dev/null 2>&1 || missing+=("$command")
done

if ((${#missing[@]})); then
  say "Missing required tools: ${missing[*]}"
  if command -v apt-get >/dev/null 2>&1 && confirm "Install the missing tools with apt now?"; then
    sudo apt-get update
    sudo apt-get install -y python3 git curl ca-certificates
  else
    fail "Install Python 3, Git and curl, then run this installer again."
  fi
fi

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
  printf '  echo '\''export PATH="%s:$PATH"'\'' >> "$HOME/.profile"\n' "$BIN_DIR"
fi
