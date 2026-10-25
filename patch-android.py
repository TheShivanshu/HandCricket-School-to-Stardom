# Small, tolerant edits to the generated Android project: portrait only, brown status/navigation bars.
import re, pathlib
m = pathlib.Path('android/app/src/main/AndroidManifest.xml')
t = m.read_text()
if 'screenOrientation' not in t:
    t = t.replace('android:name=".MainActivity"', 'android:name=".MainActivity" android:screenOrientation="portrait"', 1)
m.write_text(t)
print('manifest ok:', 'screenOrientation' in t)
s = pathlib.Path('android/app/src/main/res/values/styles.xml')
x = s.read_text()
bars = '<item name="android:statusBarColor">#241309</item><item name="android:navigationBarColor">#241309</item>'
x2 = re.sub(r'(<style name="AppTheme\.NoActionBar"[^>]*>)', r'\1' + bars, x, count=1)
s.write_text(x2)
print('styles ok:', x2 != x)
