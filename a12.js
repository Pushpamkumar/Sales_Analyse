document.addEventListener("DOMContentLoaded", function () {
    fetch("/leads")
        .then(response => response.json())
        .then(data => {
            let leadsList = document.getElementById("leads-list");
            data.forEach(lead => {
                let li = document.createElement("li");
                li.textContent = `${lead.name} (${lead.company}) - ${lead.status} - Score: ${lead.score}`;
                leadsList.appendChild(li);
            });
        });
});
