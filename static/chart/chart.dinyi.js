var popCanvas = $("#popChart");
var barChart = new Chart(popCanvas, {
  type: 'bar',
  data: {
    labels: ["python", "java", "php", "c", "c++", "c#"],
    datasets: [{
      label: 'python',
      data: [6000, 5000, 3000, 2000, 1000, 500],
      backgroundColor: [
        'rgba(255, 99, 132, 0.6)',
        'rgba(54, 162, 235, 0.6)',
        'rgba(255, 206, 86, 0.6)',
        'rgba(75, 192, 192, 0.6)',
        'rgba(153, 102, 255, 0.6)',
        'rgba(255, 159, 64, 0.6)',
        'rgba(255, 99, 132, 0.6)'
      ]
    }]
  }
});