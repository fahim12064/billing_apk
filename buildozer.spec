[app]
title = Billing
package.name = billing
package.domain = org.fatech
source.dir = .
source.include_exts = py,kv,png,jpg
version = 0.1
requirements = python3,kivy==2.3.1,kivymd==1.2.0,pillow
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE
android.api = 36
android.minapi = 21
android.sdk = 36
android.ndk = 23b
android.ndk_api = 21
fullscreen = 0
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1
