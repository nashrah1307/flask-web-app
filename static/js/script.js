// Toggle task form visibility
function toggleForm() {
    const form = document.getElementById('taskForm');
    if (form.style.display === 'none' || form.style.display === '') {
        form.style.display = 'block';
        // Focus on first input
        document.getElementById('title').focus();
    } else {
        form.style.display = 'none';
    }
}

// Add animation to task cards on load
document.addEventListener('DOMContentLoaded', function() {
    const taskCards = document.querySelectorAll('.task-card');
    taskCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        setTimeout(() => {
            card.style.transition = 'all 0.5s ease-out';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });
    
    // Animate stat cards
    const statCards = document.querySelectorAll('.stat-card');
    statCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'scale(0.9)';
        setTimeout(() => {
            card.style.transition = 'all 0.5s ease-out';
            card.style.opacity = '1';
            card.style.transform = 'scale(1)';
        }, index * 150);
    });
});

// Add confirmation for delete actions
const deleteButtons = document.querySelectorAll('.btn-delete');
deleteButtons.forEach(button => {
    button.addEventListener('click', function(e) {
        if (!confirm('Are you sure you want to delete this task?')) {
            e.preventDefault();
        }
    });
});

// Success message animation (if you add flash messages later)
function showMessage(message, type = 'success') {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message message-${type}`;
    messageDiv.textContent = message;
    messageDiv.style.cssText = `
        position: fixed;
        top: 80px;
        right: 20px;
        padding: 15px 25px;
        background: ${type === 'success' ? '#10b981' : '#ef4444'};
        color: white;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        z-index: 1000;
        animation: slideIn 0.5s ease-out;
    `;
    
    document.body.appendChild(messageDiv);
    
    setTimeout(() => {
        messageDiv.style.animation = 'slideOut 0.5s ease-out';
        setTimeout(() => {
            messageDiv.remove();
        }, 500);
    }, 3000);
}

// Add CSS animations for messages
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
