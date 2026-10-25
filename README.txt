HandCricket: School to Stardom - Android app project
=====================================================

This is the whole game wrapped as an Android app. GitHub builds the APK for you, so you
need nothing installed on your computer.

STEP 1  Make a free GitHub account (github.com) and click "New repository".
        Name it handcricket, keep it Private, tick nothing else, press Create.

STEP 2  Unzip this file. On the new repository page click "uploading an existing file".
        Drag in EVERYTHING from the unzipped folder: the folders  src  assets  and the files
        package.json  capacitor.config.json  build-www.js  patch-android.py  .gitignore
        Press "Commit changes".

STEP 3  The build script is a hidden folder (.github) and some systems skip hidden folders
        when you drag. So add it by hand:
          - In the repository click  Add file > Create new file
          - In the name box type exactly:   .github/workflows/build-apk.yml
            (typing the slashes creates the folders)
          - Open build-apk.yml from this zip in Notepad, copy all of it, paste it into the big box
          - Press "Commit changes"

STEP 4  Click the "Actions" tab. If it asks, press "I understand my workflows, enable them".
        Click "Build APK" on the left, then "Run workflow" > "Run workflow".
        (It also starts by itself after step 3.)

STEP 5  Wait about 5-8 minutes until the run shows a green tick.
        Click the run, scroll down to "Artifacts", click  HandCricket-APK  to download a zip.
        Unzip it: app-debug.apk is your game.

STEP 6  Send app-debug.apk to your phone (WhatsApp to yourself, Google Drive, USB cable).
        Open it on the phone. Android will ask to allow "Install unknown apps" for that app:
        allow it, then press Install.

If the run shows a red cross, open it, click the red step, copy the last 30 lines of the log
and send them to Claude. Do not guess.

This APK is a DEBUG build. It is fine for playing and testing. The Play Store needs a signed
release build and a Play Console account (one-time 25 dollars). That is a separate step.
