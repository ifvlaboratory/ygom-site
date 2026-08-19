var version = document.getElementById('version');
var update_time = document.getElementById('update_time');
var download_button = document.getElementById('downloadButton');
fetch('/ver_code.json').then(i => i.json()).then(i => {
    version.innerText = i.versionname
    update_time.innerText = i.update_time
    download_button.href = i.download_link
});