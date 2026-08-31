const progressColors = {
    "Not started": "#ffd4d4",
    "In progress": "#feffd4",
    "Almost done": "#e7ffc2",
    "Done": "#c6ffc4"
};

document.querySelectorAll(".task-progress").forEach(select => {
    select.addEventListener("change", async function () {
        const taskCard = this.closest(".overall-task-card");
        const taskId = taskCard.dataset.taskId;
        const progressVal = this.value;

        const response = await fetch(`/tasks/${taskId}/progress`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                newProgress: progressVal
            })
        });

        if (!response.ok) {
            console.error("Failed to update task");
        } else {
            // Change only the background color variable
            const color = progressColors[progressVal] || "#e8d4ff";
            taskCard.style.setProperty("--bgColor", color);

            taskCard.dataset.progress = progress;
        }
    });
});

const showCompleted = document.getElementById("show-completed");
const taskCards = document.querySelectorAll(".overall-task-card");

function updateCompletedVisibility() {
    taskCards.forEach(card => {
        if (card.dataset.progress === "Done") {
            card.style.display = showCompleted.checked ? "" : "none";
        }
    });
}

showCompleted.addEventListener("change", updateCompletedVisibility);

// Hide completed tasks initially
updateCompletedVisibility();