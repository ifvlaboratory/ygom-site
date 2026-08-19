var version = document.getElementById('version');
var update_time = document.getElementById('update_time');
fetch('/ver_code.json').then(i => i.json()).then(i => {
    version.innerText=i.versionname
    update_time.innerText = i.update_time
});