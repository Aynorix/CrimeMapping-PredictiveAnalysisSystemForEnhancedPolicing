document.addEventListener("DOMContentLoaded", function () {
    // Load Crime Alerts
    let alertsList = document.getElementById("crime-alerts-list");
    if (alertsList) {
        const crimeAlerts = [
            "🔴 Armed robbery reported near Central Market - Stay cautious!",
            "🚨 Break-in at Downtown Mall, avoid the area.",
            "⚠️ Suspicious activity reported in Green Park - Be vigilant!",
            "🚔 Police operation in South Avenue, follow traffic diversions.",
            "🆘 Assault case reported in City Square - Stay safe!"
        ];
        alertsList.innerHTML = crimeAlerts.map(alert => `<li>${alert}</li>`).join("");
    }

    // Contact Form Submission
    let contactForm = document.getElementById("contactForm");
    if (contactForm) {
        contactForm.addEventListener("submit", function (event) {
            event.preventDefault();
            
            let name = document.getElementById("name").value.trim();
            let email = document.getElementById("email").value.trim();
            let message = document.getElementById("message").value.trim();

            if (!name || !email || !message) {
                alert("Please fill in all fields.");
                return;
            }

            console.log("Message Sent:", { name, email, message });
            alert("Your message has been sent successfully!");
            contactForm.reset();
        });
    }

    // Crime Report Checker
    let crimeReportBtn = document.getElementById("checkCrimeReport");
    if (crimeReportBtn) {
        crimeReportBtn.addEventListener("click", function () {
            let location = document.getElementById("locationInput").value.trim();
            if (!location) {
                alert("Please enter a valid location.");
                return;
            }

            const crimeDatabase = {
                "Delhi": "High crime rate: 150 incidents last month.",
                "Mumbai": "Moderate crime rate: 85 incidents.",
                "Bangalore": "Low crime rate: 40 incidents.",
                "Chennai": "Low crime rate: 30 incidents.",
                "Kolkata": "Moderate crime rate: 70 incidents."
            };

            alert(crimeDatabase[location] ? `Crime Report for ${location}: ${crimeDatabase[location]}` : "No crime data found for this location.");
        });
    }
});
