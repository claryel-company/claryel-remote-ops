# CLARYEL RemoteOps guided installer for Windows 10/11.
# Installs into the current user's LocalAppData directory. It does not disable
# Defender, UAC, BitLocker, SmartScreen or other Windows security controls.

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$AppRoot = Join-Path $env:LOCALAPPDATA 'CLARYEL\RemoteOps'
$AppDir = Join-Path $AppRoot 'app'
$StateDir = Join-Path $AppRoot 'state'
$BinDir = Join-Path $AppRoot 'bin'
$RepositoryUrl = 'https://github.com/claryel-company/claryel-remote-ops.git'

function Confirm-Action([string]$Message) {
    $answer = Read-Host "$Message [y/N]"
    return $answer -match '^[Yy]$'
}

function Get-PythonInvocation {
    if (Get-Command py -ErrorAction SilentlyContinue) { return @('py', '-3') }
    if (Get-Command python -ErrorAction SilentlyContinue) { return @('python') }
    return $null
}

$python = Get-PythonInvocation
$git = Get-Command git -ErrorAction SilentlyContinue

if (-not $python -or -not $git) {
    Write-Host "Required tools are missing." -ForegroundColor Yellow
    if (Get-Command winget -ErrorAction SilentlyContinue) {
        if (-not $python -and (Confirm-Action 'Install Python 3 with winget now?')) {
            winget install --id Python.Python.3.12 --exact --source winget --accept-package-agreements --accept-source-agreements
        }
        if (-not $git -and (Confirm-Action 'Install Git for Windows with winget now?')) {
            winget install --id Git.Git --exact --source winget --accept-package-agreements --accept-source-agreements
        }
        $env:PATH = [Environment]::GetEnvironmentVariable('PATH', 'Machine') + ';' + [Environment]::GetEnvironmentVariable('PATH', 'User')
        $python = Get-PythonInvocation
        $git = Get-Command git -ErrorAction SilentlyContinue
    }
}

if (-not $python) { throw 'Python 3 is required. Install Python 3, reopen PowerShell and run this installer again.' }
if (-not $git) { throw 'Git for Windows is required. Install Git, reopen PowerShell and run this installer again.' }

New-Item -ItemType Directory -Force -Path $AppRoot, $BinDir | Out-Null

if (Test-Path (Join-Path $AppDir '.git')) {
    Write-Host 'Updating the public RemoteOps application...'
    git -C $AppDir fetch --depth 1 origin main
    git -C $AppDir reset --hard origin/main
} elseif (Test-Path $AppDir) {
    throw "$AppDir exists but is not a RemoteOps checkout."
} else {
    Write-Host 'Downloading the public RemoteOps application...'
    git clone --depth 1 --branch main $RepositoryUrl $AppDir
}

$pythonCommand = $python -join ' '
$wrapper = @"
@echo off
$pythonCommand "$AppDir\src\remoteops.py" %*
"@
Set-Content -Path (Join-Path $BinDir 'remoteops.cmd') -Value $wrapper -Encoding Ascii

if (-not (Test-Path (Join-Path $StateDir '.git'))) {
    Write-Host 'Creating your private local configuration workspace...'
    if ($python.Count -eq 2) {
        & $python[0] $python[1] (Join-Path $AppDir 'src\remoteops.py') init --path $StateDir
    } else {
        & $python[0] (Join-Path $AppDir 'src\remoteops.py') init --path $StateDir
    }
}

if ($python.Count -eq 2) {
    & $python[0] $python[1] (Join-Path $AppDir 'src\remoteops.py') doctor
    & $python[0] $python[1] (Join-Path $AppDir 'src\remoteops.py') status --path $StateDir
} else {
    & $python[0] (Join-Path $AppDir 'src\remoteops.py') doctor
    & $python[0] (Join-Path $AppDir 'src\remoteops.py') status --path $StateDir
}

$userPath = [Environment]::GetEnvironmentVariable('PATH', 'User')
if (($userPath -split ';') -notcontains $BinDir) {
    if (Confirm-Action 'Add the RemoteOps command to your user PATH?') {
        $newPath = if ([string]::IsNullOrWhiteSpace($userPath)) { $BinDir } else { "$userPath;$BinDir" }
        [Environment]::SetEnvironmentVariable('PATH', $newPath, 'User')
        $env:PATH = "$env:PATH;$BinDir"
    }
}

Write-Host ''
Write-Host 'CLARYEL RemoteOps is installed.' -ForegroundColor Green
Write-Host "Application: $AppDir"
Write-Host "Your private local workspace: $StateDir"
Write-Host "Command: $BinDir\remoteops.cmd"
Write-Host ''
Write-Host 'IMPORTANT PRIVACY BOUNDARY' -ForegroundColor Cyan
Write-Host '- Personal files, passwords, keys, chats, raw logs and backups are not placed in Git by this installer.'
Write-Host '- RemoteOps contacts GitHub only when you explicitly create or connect your private repository.'
Write-Host '- RemoteOps contacts an AI provider only when you choose to use that provider.'
Write-Host '- Installing or updating software may contact package sources you approve.'
Write-Host '- This installer does not disable Defender, UAC, BitLocker or SmartScreen.'
Write-Host ''
Write-Host 'NEXT STEP'
Write-Host "Open: $AppDir\docs\PRIVATE_REPOSITORY_SETUP.md"
Write-Host ''
Write-Host 'After installing GitHub CLI, create your private repository with:'
Write-Host "  remoteops connect --path `"$StateDir`" --create-private remoteops-my-computer"
Write-Host ''
Write-Host 'Verify privacy later with:'
Write-Host "  remoteops privacy-check --path `"$StateDir`""
