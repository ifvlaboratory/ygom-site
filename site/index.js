var version = document.getElementById('version');
fetch('/ver_code.json').then(i => i.json()).then(i => version.innerText=i.versionname)