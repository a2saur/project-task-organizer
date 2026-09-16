const progressColors = {
    "Not started": "#ffd4d4",
    "In progress": "#feffd4",
    "Almost done": "#e7ffc2",
    "Done": "#c6ffc4"
};

const todayTasks = document.getElementById("today-tasks");
const futureTasks = document.getElementById("future-tasks");
document.querySelectorAll('.pin-task-btn').forEach(button => {
    button.addEventListener('click', async function(event) {
        const taskId = this.dataset.taskId;
        const doToday = todayTasks.contains(this);

        const response = await fetch(`/tasks/${taskId}/pin`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            // body: JSON.stringify({
            //     newProgress: progressVal
            // })
        });

        // TODO: move task to today's tasks or not
        if (!response.ok) {
            console.error("Failed to update task");
        } else {
            if (doToday){
                // event.target.setAttribute('data-do-today', "False");
                futureTasks.prepend(event.target.closest('.overall-task-card'));
            } else {
                // event.target.setAttribute('data-do-today', "True");
                todayTasks.prepend(event.target.closest('.overall-task-card'));
            }
        }
    });
});

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