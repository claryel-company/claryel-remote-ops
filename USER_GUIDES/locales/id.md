# CLARYEL RemoteOps — instalasi dan penyiapan privat

RemoteOps mengelola komputer Windows, Ubuntu/Linux, atau macOS milik Anda melalui chat AI yang Anda pilih.

## 1. Instal

- [Installer Windows](../../installers/install-windows.ps1)
- [Installer macOS](../../installers/install-macos.sh)
- [Installer Ubuntu](../../installers/install-ubuntu.sh)

Jalankan berkas yang diunduh. RemoteOps dipasang di profil pengguna Anda, membuat ruang kerja lokal privat, dan tidak menonaktifkan keamanan sistem operasi.

## 2. Buat repositori pribadi berstatus Private

Pasang GitHub CLI, jalankan `gh auth login`, lalu jalankan perintah yang ditampilkan installer:

```text
remoteops connect --path JALUR-PRIVAT-ANDA --create-private remoteops-komputer-saya
```

Repositori dibuat di akun GitHub Anda dengan visibilitas `Private`. RemoteOps tidak menjadikannya publik dan tidak menambahkan kolaborator.

Private berarti tersembunyi dari publik. Anda, orang atau aplikasi yang Anda izinkan secara tegas, dan GitHub sebagai operator layanan tetap dapat mengakses sesuai izin. Lindungi akun dengan passkey atau autentikasi dua faktor.

Jangan pernah menyimpan kata sandi, token, kunci privat, kode pemulihan, berkas pribadi, chat, log mentah, basis data, atau cadangan di Git.

## 3. Periksa privasi

```text
remoteops privacy-check --path JALUR-PRIVAT-ANDA
```

Lanjutkan hanya bila hasil menunjukkan `"ok": true`, `"visibility": "PRIVATE"`, dan tidak ada temuan.

## 4. Hubungkan ChatGPT

1. Buka **ChatGPT > Settings > Apps > GitHub**.
2. Pilih **Only select repositories**.
3. Pilih hanya `remoteops-komputer-saya`.
4. Tinjau izin sebelum menyetujui.
5. Tinjau **Settings > Data Controls > Improve the model for everyone**.
6. Jangan pernah menempelkan rahasia atau berkas pribadi ke chat.

Ketersediaan aplikasi GitHub dan kemampuan menulis bergantung pada paket dan mode ChatGPT. Koneksi baca-saja tidak dapat menerapkan perubahan.

## Batas komunikasi

RemoteOps menghubungi GitHub hanya saat Anda menghubungkan atau menyinkronkan repositori privat, ChatGPT hanya saat Anda memilih menggunakannya, dan sumber paket hanya untuk operasi perangkat lunak yang disetujui. Installer tidak menambahkan iklan atau analitik yang tidak terkait.

Panduan lengkap: [repositori privat](../../docs/PRIVATE_REPOSITORY_SETUP.md), [ChatGPT](../../docs/CHATGPT_SETUP.md), [privasi dan jaringan](../../docs/PRIVACY_AND_NETWORK.md).
