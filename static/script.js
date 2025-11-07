let points = [];
const canvas = document.getElementById("mapCanvas");
const ctx = canvas.getContext("2d");

// 🎯 Dibuja el polígono y muestra el área visualmente
function drawPolygon() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  if (points.length < 2) return;

  // Calcular límites para escalar al canvas
  const xs = points.map(p => p.x);
  const ys = points.map(p => p.y);
  const minX = Math.min(...xs);
  const maxX = Math.max(...xs);
  const minY = Math.min(...ys);
  const maxY = Math.max(...ys);

  const margin = 20;
  const scaleX = (canvas.width - 2 * margin) / (maxX - minX || 1);
  const scaleY = (canvas.height - 2 * margin) / (maxY - minY || 1);
  const scale = Math.min(scaleX, scaleY);

  // Convertir puntos escalados
  const scaledPoints = points.map(p => ({
    x: margin + (p.x - minX) * scale,
    y: canvas.height - (margin + (p.y - minY) * scale)
  }));

  // Dibujar el terreno
  ctx.beginPath();
  ctx.moveTo(scaledPoints[0].x, scaledPoints[0].y);
  for (let i = 1; i < scaledPoints.length; i++) {
    ctx.lineTo(scaledPoints[i].x, scaledPoints[i].y);
  }
  ctx.closePath();

  // Estilo visual del terreno
  ctx.strokeStyle = "#00FF00";
  ctx.lineWidth = 2;
  ctx.stroke();
  ctx.fillStyle = "rgba(0, 255, 0, 0.3)";
  ctx.fill();

  // Calcular área en coordenadas reales
  const area = calculateArea(points);
  const centerX = (Math.min(...xs) + Math.max(...xs)) / 2;
  const centerY = (Math.min(...ys) + Math.max(...ys)) / 2;

  // Convertir centro a coordenadas escaladas
  const centerScaled = {
    x: margin + (centerX - minX) * scale,
    y: canvas.height - (margin + (centerY - minY) * scale)
  };

  // Mostrar texto del área dentro del terreno
  ctx.fillStyle = "black";
  ctx.font = "bold 16px Arial";
  ctx.fillText(`Área total: ${area.toFixed(2)} m²`, centerScaled.x - 60, centerScaled.y);
}

// 📐 Calcular el área total del polígono (fórmula Shoelace)
function calculateArea(points) {
  let area = 0;
  for (let i = 0; i < points.length; i++) {
    const j = (i + 1) % points.length;
    area += points[i].x * points[j].y;
    area -= points[j].x * points[i].y;
  }
  return Math.abs(area / 2);
}

// 📏 Calcular el perímetro
function calculatePerimeter(points) {
  let perimeter = 0;
  for (let i = 0; i < points.length; i++) {
    const j = (i + 1) % points.length;
    const dx = points[j].x - points[i].x;
    const dy = points[j].y - points[i].y;
    perimeter += Math.sqrt(dx * dx + dy * dy);
  }
  return perimeter;
}

// ➕ Agregar puntos
document.getElementById("addPoint").addEventListener("click", () => {
  const x = parseFloat(document.getElementById("xVal").value);
  const y = parseFloat(document.getElementById("yVal").value);
  if (!isNaN(x) && !isNaN(y)) {
    points.push({ x, y });
    const row = document.createElement("tr");
    row.innerHTML = `<td>${x}</td><td>${y}</td>`;
    document.getElementById("coordTable").appendChild(row);
    drawPolygon();
  }
});

// 🧮 Calcular y mostrar área total + perímetro
document.getElementById("calculate").addEventListener("click", () => {
  if (points.length < 3) {
    document.getElementById("result").innerText = "Debes ingresar al menos 3 puntos.";
    return;
  }

  const area = calculateArea(points);
  const perimeter = calculatePerimeter(points);

  document.getElementById("result").innerText =
    `Área total: ${area.toFixed(2)} m² | Perímetro: ${perimeter.toFixed(2)} m`;

  // Redibujar el polígono con el texto en el canvas
  drawPolygon();
});

