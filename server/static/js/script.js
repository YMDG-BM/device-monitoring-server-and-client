function createProgressBar(category, label, percent) {
    return `
        <div class="progress-item ${category}">
            <div class="progress-title">
                <span>${label}</span>
                <span>${percent.toFixed(1)}%</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: ${percent}%"></div>
            </div>
        </div>
    `;
}
function renderActiveWindowMessage(){
    fetch('/client_data')
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById('active-window');
        if (data.error) {
            container.innerHTML = '<div class="Offline" style="font-size: 14px;"></div>';
        }
        else {
            container.innerHTML = `<div class="active_window"><h3>当前激活窗口</h3>${data.active_window.title}</div>`;
        }
});
}

function renderProgressBars() {
    fetch('/client_data')
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                const container = document.getElementById('progressBars');
                container.innerHTML = '<div class="Offline" style="font-size: 14px;">计算机已离线</div>';
            }
            else{
            const container = document.getElementById('progressBars');
            container.innerHTML = [
                createProgressBar('cpu', 'CPU 使用率', data.cpu.usage),
                createProgressBar('memory', '内存使用率', data.memory.percent),
                createProgressBar('disk', '硬盘使用率', data.disk.percent),
                createProgressBar('gpu-load', 'GPU 使用率', data.gpu.load),
                createProgressBar('gpu-mem', '显存使用率', data.gpu.memory_percent),
            //`<div class="active_window">当前激活的窗口为：${data.active_window.title}</div>`
    ].join('');}
    });
}

setInterval(renderProgressBars, 5000); // 每5秒更新一次数据
renderProgressBars(); // 页面加载时立即获取一次数据
setInterval(renderActiveWindowMessage, 5000);
renderActiveWindowMessage();