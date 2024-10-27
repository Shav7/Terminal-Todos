document.addEventListener('DOMContentLoaded', function() {
    const taskForm = document.getElementById('task-form');
    const taskInput = document.getElementById('task-input');
    const taskList = document.getElementById('task-list');
    const progress = document.getElementById('progress');
    const progressText = document.getElementById('progress-text');
    const timer = document.getElementById('timer');

    let seconds = 0;
    setInterval(updateTimer, 1000);

    function updateTimer() {
        seconds++;
        const minutes = Math.floor(seconds / 60);
        const remainingSeconds = seconds % 60;
        timer.textContent = `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
    }

    function updateProgress() {
        const tasks = document.querySelectorAll('.task');
        const completedTasks = document.querySelectorAll('.task.completed');
        const percentage = tasks.length ? Math.round((completedTasks.length / tasks.length) * 100) : 0;
        
        progress.style.width = `${percentage}%`;
        progressText.textContent = `${percentage}% COMPLETE`;
    }

    taskForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        const content = taskInput.value.trim();
        
        if (!content) return;

        const formData = new FormData();
        formData.append('content', content);

        try {
            const response = await fetch('/tasks', {
                method: 'POST',
                body: formData
            });
            
            if (response.ok) {
                const task = await response.json();
                const taskElement = createTaskElement(task);
                taskList.insertBefore(taskElement, taskList.firstChild);
                taskInput.value = '';
                updateProgress();
            }
        } catch (error) {
            console.error('Error adding task:', error);
        }
    });

    function createTaskElement(task) {
        const div = document.createElement('div');
        div.className = `task ${task.completed ? 'completed' : ''}`;
        div.dataset.id = task.id;
        
        const span = document.createElement('span');
        span.className = 'task-content';
        span.textContent = task.content;
        
        div.appendChild(span);
        
        div.addEventListener('click', toggleTask);
        return div;
    }

    async function toggleTask() {
        const taskId = this.dataset.id;
        
        try {
            const response = await fetch(`/tasks/${taskId}/toggle`, {
                method: 'POST'
            });
            
            if (response.ok) {
                const task = await response.json();
                this.classList.toggle('completed');
                updateProgress();
            }
        } catch (error) {
            console.error('Error toggling task:', error);
        }
    }

    // Add click handlers to existing tasks
    document.querySelectorAll('.task').forEach(task => {
        task.addEventListener('click', toggleTask);
    });

    // Initial progress update
    updateProgress();
});