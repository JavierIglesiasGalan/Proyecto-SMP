const API_URL = "http://localhost:8000";

let charts = {};

//Cargar servidores
async function loadServers() {
    const res = await fetch(`${API_URL}/servers`);
    const servers = await res.json();

    const select = document.getElementById("serverSelect");

    //Guardar selección actual
    const currentValue = select.value;

    //Limpiar opciones
    select.innerHTML = "";

    servers.forEach(server => {
        const option = document.createElement("option");
        option.value = server.id;
        option.text = server.name;
        select.appendChild(option);
    });

    //Restaurar selección si existe
    if (currentValue) {
        select.value = currentValue;
    }

    //Si no hay selección, coger el primero
    if (!select.value && servers.length > 0) {
        select.value = servers[0].id;
    }
}

//Cargar métricas
async function loadMetrics() {
    const serverId = document.getElementById("serverSelect").value;

    if (!serverId) return;

    const res = await fetch(`${API_URL}/servers/${serverId}/metrics`);
    const data = await res.json();

    const cpuData = data.map(m => m.cpu);
    const ramData = data.map(m => m.ram);
    const diskData = data.map(m => m.disk);
    const labels = data.map(m => new Date(m.timestamp).toLocaleTimeString());

    const cpuColors = data.map(m => getColor(m.cpu, "cpu"));
    const ramColors = data.map(m => getColor(m.ram, "ram"));
    const diskColors = data.map(m => getColor(m.disk, "disk"));

    createChart("cpuChart", "CPU (%)", cpuData, labels, cpuColors);
    createChart("ramChart", "RAM (%)", ramData, labels, ramColors);
    createChart("diskChart", "Disk (%)", diskData, labels, diskColors);

    showAlert(data);
}

//Refresh completo
async function refreshAll() {
    await loadServers();
    await loadMetrics();
}

//Colores según uso
function getColor(value, type) {
    if (type === "cpu" && value > 80) return "red";
    if (type === "ram" && value > 80) return "orange";
    if (type === "disk" && value > 90) return "red";
    return "blue";
}

//Crear o actualizar gráfica
function createChart(canvasId, label, data, labels, colors) {
    if (charts[canvasId]) {
        charts[canvasId].data.labels = labels;
        charts[canvasId].data.datasets[0].data = data;
        charts[canvasId].data.datasets[0].borderColor = colors;
        charts[canvasId].update();
    } else {
        charts[canvasId] = new Chart(document.getElementById(canvasId), {
            type: "line",
            data: {
                labels: labels,
                datasets: [{
                    label: label,
                    data: data,
                    borderColor: colors,
                    fill: false,
                    tension: 0.3
                }]
            },
            options: {
                responsive: true,
                animation: false
            }
        });
    }
}

//Mostrar alerta global
function showAlert(data) {
    const alertBox = document.getElementById("alertBox");
    const latest = data[data.length - 1];

    if (!latest) return;

    if (latest.cpu > 80 || latest.ram > 80 || latest.disk > 90) {
        alertBox.style.display = "block";
        alertBox.style.backgroundColor = "red";
        alertBox.innerText = "⚠️ High resource usage detected!";
    } else {
        alertBox.style.display = "none";
    }
}

//Auto refresh cada 5s
setInterval(refreshAll, 5000);

//Eventos
document.getElementById("serverSelect").addEventListener("change", loadMetrics);

//Inicialización
refreshAll();