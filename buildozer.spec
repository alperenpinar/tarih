[app]

# (str) Title of your application
title = KPSS Master Pro

# (str) Package name
package.name = kpssmaster

# (str) Package domain (needed for android/ios packaging)
package.domain = org.alperen

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (list) Pattern to whitelist for the whole project
android.whitelist = sqlite3/*

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Supported architectures
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backups (Android API >=23)
android.allow_backup = True

# (str) The format used to package the app for release mode (aab or apk or aar).
# Play Store requires AAB!
android.release_artifact = aab
android.debug_artifact = apk

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
