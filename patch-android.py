
import re
import pathlib
import xml.etree.ElementTree as ET

# Configure Android manifest
m = pathlib.Path("android/app/src/main/AndroidManifest.xml")
t = m.read_text()

# Force portrait orientation
if "android:screenOrientation" not in t:
    t = t.replace(
        'android:name=".MainActivity"',
        'android:name=".MainActivity" android:screenOrientation="portrait"',
        1
    )

# Add AdMob App ID
app_id = "ca-app-pub-4042250734159630~3586575455"

if "com.google.android.gms.ads.APPLICATION_ID" not in t:
    meta = (
        '<meta-data '
        'android:name="com.google.android.gms.ads.APPLICATION_ID" '
        f'android:value="{app_id}" />'
    )
    t = t.replace("</application>", meta + "\n    </application>", 1)

# Validate XML before saving
ET.fromstring(t)
m.write_text(t)
print("Android manifest configured")

# Preserve brown status and navigation bars
s = pathlib.Path("android/app/src/main/res/values/styles.xml")
x = s.read_text()

bars = (
    '<item name="android:statusBarColor">#241309</item>'
    '<item name="android:navigationBarColor">#241309</item>'
)

pattern = r'(<style name="AppTheme\.NoActionBar"[^>]*>)'

if not re.search(pattern, x):
    raise RuntimeError("AppTheme.NoActionBar style not found")

x = re.sub(
    pattern,
    lambda match: match.group(1) + bars,
    x,
    count=1
)

s.write_text(x)
print("Theme colours configured")
