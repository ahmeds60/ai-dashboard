async function loadMisinformationAlerts() {
    try {
        const response = await fetch("https://your-api-url.onrender.com/misinformation_alerts");
        const data = await response.json();

        if (data.error) {
            document.getElementById("alertList").innerText = "Error loading alerts.";
            return;
        }

        const alertList = document.getElementById("alertList");
        alertList.innerHTML = "";
        data.alerts.forEach(alert => {
            let listItem = document.createElement("li");
            listItem.innerHTML = `<strong>${alert.title}</strong>: ${alert.alert}`;
            alertList.appendChild(listItem);
        });
    } catch (error) {
        console.error("Error fetching misinformation alerts:", error);
        document.getElementById("alertList").innerText = "Failed to load alerts.";
    }
}

async function loadSentimentChart() {
    try {
        const response = await fetch("https://your-api-url.onrender.com/news_sentiment");
        const data = await response.json();

        if (data.error) {
            document.getElementById("sentimentChart").innerText = "Error loading data.";
            return;
        }

        const ctx = document.getElementById("sentimentChart").getContext("2d");
        new Chart(ctx, {
            type: "pie",
            data: {
                labels: Object.keys(data.sentiment_distribution),
                datasets: [{
                    label: "Sentiment Distribution",
                    data: Object.values(data.sentiment_distribution),
                    backgroundColor: ["#4CAF50", "#FF5733", "#C0C0C0"]
                }]
            }
        });
    } catch (error) {
        console.error("Error fetching sentiment data:", error);
        document.getElementById("sentimentChart").innerText = "Failed to load sentiment data.";
    }
}

document.addEventListener("DOMContentLoaded", () => {
    loadMisinformationAlerts();
    loadSentimentChart();
});
