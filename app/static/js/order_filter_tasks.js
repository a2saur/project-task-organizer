const projectFilterButton = document.getElementById("project-filter-button");
const projectFilterMenu = document.getElementById("project-filter-menu");

projectFilterButton.addEventListener("click", () => {
    projectFilterMenu.style.display =
        projectFilterMenu.style.display === "block"
            ? "none"
            : "block";
});

function updateProjectFilterButton() {
    const totalProjects =
        document.querySelectorAll(".project-filter-option").length;

    const selected = document.querySelectorAll(
        ".project-filter-option:checked"
    );

    if (selected.length === 0) {
        projectFilterButton.innerHTML =
            'Projects (All) <span class="filter-arrow">▾</span>';
    } else {
        projectFilterButton.innerHTML =
            `Projects (${totalProjects-selected.length}) <span class="filter-arrow">▾</span>`;
    }
}
updateProjectFilterButton();

document.querySelectorAll(".project-filter-option").forEach(option => {
    option.addEventListener("change", () => {
        updateProjectFilterButton();
        updateTaskDisplay();
    });
});

const taskSort = document.getElementById("task-sort");
const allTaskCards = [...document.querySelectorAll(".overall-task-card")];

function sortTasks(cards) {
    const sortType = taskSort.value;

    cards.sort((a, b) => {

        if (sortType === "project") {
            return a.dataset.project.localeCompare(b.dataset.project);
        }

        if (sortType === "due-asc" || sortType === "due-desc") {
            const aDate = a.dataset.dueDate;
            const bDate = b.dataset.dueDate;

            // Tasks without dates go to the end
            if (!aDate && !bDate) return 0;
            if (!aDate) return 1;
            if (!bDate) return -1;

            const result = new Date(aDate) - new Date(bDate);

            return sortType === "due-asc" ? result : -result;
        }
        return 0;
    });

    return cards;
}

function getDueGroup(card) {
    const dateString = card.dataset.dueDate;

    if (!dateString) {
        return {
            key: "none",
            label: "No due date",
            order: Infinity
        };
    }

    const due = new Date(dateString);
    const now = new Date();

    due.setHours(0, 0, 0, 0);
    now.setHours(0, 0, 0, 0);

    const daysUntil = Math.floor(
        (due - now) / (1000 * 60 * 60 * 24)
    );

    if (daysUntil < 0) {
        return {
            key: "overdue",
            label: "Overdue",
            order: -1
        };
    }

    // Find the Sunday of the current week
    const currentSunday = new Date(now);
    currentSunday.setDate(
        now.getDate() - now.getDay()
    );

    currentSunday.setHours(0, 0, 0, 0);

    // Find the Sunday of the task's week
    const dueSunday = new Date(due);
    dueSunday.setDate(
        due.getDate() - due.getDay()
    );

    dueSunday.setHours(0, 0, 0, 0);

    const weeksAway = Math.round(
        (dueSunday - currentSunday) /
        (1000 * 60 * 60 * 24 * 7)
    );

    if (weeksAway === 0) {
        return {
            key: "this-week",
            label: "This week",
            order: 0
        };
    }

    if (weeksAway === 1) {
        return {
            key: "next-week",
            label: "Next week",
            order: 1
        };
    }

    return {
        key: `week-${weeksAway}`,
        label: `In ${weeksAway} weeks`,
        order: weeksAway
    };
}

function groupByDueDate(cards) {
    const groups = {};

    cards.forEach(card => {
        const group = getDueGroup(card);

        if (!groups[group.key]) {
            groups[group.key] = {
                label: group.label,
                order: group.order,
                cards: []
            };
        }

        groups[group.key].cards.push(card);
    });

    return Object.values(groups)
        .sort((a, b) => a.order - b.order);
}

function groupByProject(cards) {
    const groups = {};

    cards.forEach(card => {
        const projectId = card.dataset.projectId;
        const projectName = card.dataset.project;

        if (!groups[projectId]) {
            groups[projectId] = {
                label: projectName,
                cards: []
            };
        }

        groups[projectId].cards.push(card);
    });

    return Object.values(groups);
}

function groupTasks(cards) {
    const sortType = taskSort.value;
    if (sortType === "due-asc" || sortType === "due-desc"){
        return groupByDueDate(cards);
    } else {
        return groupByProject(cards);
    }
}

function renderGroups(container, groups) {
    container.innerHTML = "";

    groups.forEach(group => {
        const groupElement = document.createElement("div");
        groupElement.classList.add("task-grouping");

        const heading = document.createElement("h3");
        heading.classList.add("task-group-heading");
        heading.textContent = group.label;

        const cardsContainer = document.createElement("div");
        cardsContainer.classList.add("task-group");

        group.cards.forEach(card => {
            cardsContainer.appendChild(card);
        });

        groupElement.appendChild(heading);
        groupElement.appendChild(cardsContainer);

        container.appendChild(groupElement);
    });
}

function renderUngrouped(container, cards) {
    container.innerHTML = "";

    const groupElement = document.createElement("div");
    groupElement.classList.add("task-group");

    cards.forEach(card => {
        groupElement.appendChild(card);
    });

    container.appendChild(groupElement);
}

// ---Toggle completed tasks---
const showCompleted = document.getElementById("show-completed");

function updateCompletedVisibility() {
    document.querySelectorAll(".overall-task-card").forEach(card => {
        if (card.dataset.progress === "Done") {
            card.style.display = showCompleted.checked ? "" : "none";
        }
    });
}

showCompleted.addEventListener("change", updateCompletedVisibility);

// Filter Tasks
const projectFilterOptions = document.querySelectorAll(".project-filter-option");

function filterTasks(cards) {
    const selectedProjects = [
        ...document.querySelectorAll(".project-filter-option:not(:checked)")
    ].map(option => option.value);

    cards.forEach(card => {
        const shouldHide =
            selectedProjects.length > 0 &&
            !selectedProjects.includes(card.dataset.projectId);

        card.style.display = shouldHide ? "none" : "";
    });

    return cards;
}


// Main display
const groupTasksToggle = document.getElementById("group-tasks");

function updateTaskDisplay() {
    let todayCards = [
        ...todayTasks.querySelectorAll(".overall-task-card")
    ];

    let futureCards = [
        ...futureTasks.querySelectorAll(".overall-task-card")
    ];

    filterTasks(todayCards);
    filterTasks(futureCards);

    todayCards = sortTasks(todayCards);
    futureCards = sortTasks(futureCards);

    const todayGroups = groupTasks(todayCards);
    const futureGroups = groupTasks(futureCards);

    if (groupTasksToggle.checked) {
        renderGroups(todayTasks, todayGroups);
        renderGroups(futureTasks, futureGroups);
    } else {
        renderUngrouped(todayTasks, todayCards);
        renderUngrouped(futureTasks, futureCards);
    }

    updateCompletedVisibility();
}
taskSort.addEventListener("change", updateTaskDisplay);
groupTasksToggle.addEventListener("change", updateTaskDisplay);
projectFilterOptions.forEach(option => {
    option.addEventListener("change", updateTaskDisplay);
});
updateTaskDisplay();