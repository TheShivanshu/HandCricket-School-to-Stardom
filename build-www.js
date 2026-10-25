// Builds www/index.html from src/game.html:
//  - swaps the online Google Fonts link for fonts embedded in the file (so the app works offline)
//  - wraps the game in a full HTML document
//  - adds the Android back-button handling
const fs = require('fs');
const path = require('path');

function fontFace(family, pkg) {
  const dir = path.join('node_modules', '@fontsource', pkg, 'files');
  const file = fs.readdirSync(dir).find(f => /latin-400-normal\.woff2$/.test(f));
  if (!file) throw new Error('font file not found for ' + pkg);
  const b64 = fs.readFileSync(path.join(dir, file)).toString('base64');
  return "@font-face{font-family:'" + family + "';font-style:normal;font-weight:400;font-display:swap;src:url(data:font/woff2;base64," + b64 + ") format('woff2')}";
}

let html = fs.readFileSync('src/game.html', 'utf8');
const link = /<link rel="stylesheet" href="https:\/\/fonts\.googleapis\.com[^>]*>/;
if (!link.test(html)) throw new Error('Google Fonts link not found in src/game.html');
html = html.replace(link, '<style>' + fontFace('Patrick Hand', 'patrick-hand') + fontFace('Permanent Marker', 'permanent-marker') + '</style>');

const backButton = `
<script>
(function(){
  var C = window.Capacitor; if (!C || !C.Plugins || !C.Plugins.App) return;
  function vis(id){ var e = document.getElementById(id); return !!e && !e.hidden; }
  C.Plugins.App.addListener('backButton', function(){
    if (vis('scr-home')){ C.Plugins.App.exitApp(); return; }
    if (vis('scr-match') || vis('scr-sim')) return;          // never leave a match by accident
    var v = document.getElementById('veil'); if (v && !v.hidden) return;
    var h = document.querySelector('[data-act="home"]'); if (h) h.click();
  });
})();
</script>`;

const out = '<!doctype html><html lang="en"><head><meta charset="utf-8">' +
  '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover,user-scalable=no">' +
  '<meta name="theme-color" content="#241309">' + html + backButton + '</html>';
fs.mkdirSync('www', { recursive: true });
fs.writeFileSync('www/index.html', out);
console.log('www/index.html written,', Math.round(out.length / 1024), 'KB');
