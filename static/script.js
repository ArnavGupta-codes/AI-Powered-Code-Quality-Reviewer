const fileInput = document.getElementById('fileInput');
const analyzeBtn = document.getElementById('analyzeBtn');
const newFileBtn = document.getElementById('newFileBtn');

fileInput.addEventListener('change', handleFileSelect);
analyzeBtn.addEventListener('click', analyzeCode);
newFileBtn.addEventListener('click', resetForm);

// Drag and drop support
const uploadLabel = document.querySelector('.upload-label');

uploadLabel.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadLabel.style.borderColor = '#764ba2';
    uploadLabel.style.background = '#f0f2ff';
});

uploadLabel.addEventListener('dragleave', () => {
    uploadLabel.style.borderColor = '#667eea';
    uploadLabel.style.background = '#f8f9ff';
});

uploadLabel.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadLabel.style.borderColor = '#667eea';
    uploadLabel.style.background = '#f8f9ff';
    
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        fileInput.files = files;
        handleFileSelect();
    }
});

function handleFileSelect() {
    if (fileInput.files.length > 0) {
        analyzeBtn.disabled = false;
        const fileName = fileInput.files[0].name;
        const uploadText = document.querySelector('.upload-text');
        uploadText.textContent = `Selected: ${fileName}`;
    }
}

async function analyzeCode() {
    if (fileInput.files.length === 0) {
        showError('Please select a file');
        return;
    }

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    showLoading();

    try {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (!response.ok) {
            showError(data.error || 'Analysis failed');
            return;
        }

        displayResults(data);
    } catch (error) {
        showError('Failed to connect to server. Please try again.');
        console.error('Error:', error);
    }
}

function displayResults(data) {
    const results = data.results;
    
    // Update filename
    document.getElementById('filename').textContent = data.filename;
    
    // Update scores
    updateScore('readability', results.readability);
    updateScore('maintainability', results.maintainability);
    updateScore('complexity', results.complexity, true); // Complexity is inverse (lower is better)
    updateScore('security', results.security);
    
    // Update overall score
    const overall = results.overall;
    document.getElementById('overallScore').textContent = overall.toFixed(1);
    
    if (overall >= 80) {
        document.getElementById('overallMessage').textContent = 'Excellent code quality!';
        document.getElementById('overallMessage').style.color = '#4CAF50';
    } else if (overall >= 70) {
        document.getElementById('overallMessage').textContent = 'Good code quality.';
        document.getElementById('overallMessage').style.color = '#2196F3';
    } else if (overall >= 60) {
        document.getElementById('overallMessage').textContent = 'Acceptable, but improvements needed.';
        document.getElementById('overallMessage').style.color = '#FF9800';
    } else {
        document.getElementById('overallMessage').textContent = 'Significant improvements recommended.';
        document.getElementById('overallMessage').style.color = '#F44336';
    }
    
    // Update metrics
    const metrics = results.metrics;
    document.getElementById('metricsLOC').textContent = metrics.loc || '-';
    document.getElementById('metricsCyclomatic').textContent = metrics.cyclomatic_complexity || '-';
    document.getElementById('metricsComments').textContent = metrics.comment_density ? metrics.comment_density.toFixed(1) + '%' : '-';
    document.getElementById('metricsIssues').textContent = metrics.issues || '-';
    
    hideLoading();
    showResults();
}

function updateScore(metric, score, isInverse = false) {
    const scoreEl = document.getElementById(metric + 'Score');
    const fillEl = document.getElementById(metric + 'Fill');
    
    scoreEl.textContent = score.toFixed(1);
    
    // For complexity, inverse the percentage (100 - score)
    const percentage = isInverse ? Math.max(0, 100 - score) : Math.min(100, score);
    fillEl.style.width = percentage + '%';
}

function showLoading() {
    document.getElementById('loading').style.display = 'block';
    document.getElementById('results').style.display = 'none';
    document.getElementById('error').style.display = 'none';
}

function hideLoading() {
    document.getElementById('loading').style.display = 'none';
}

function showResults() {
    document.getElementById('results').style.display = 'block';
    document.getElementById('error').style.display = 'none';
}

function showError(message) {
    document.getElementById('errorMessage').textContent = message;
    document.getElementById('error').style.display = 'block';
    document.getElementById('results').style.display = 'none';
    document.getElementById('loading').style.display = 'none';
}

function resetForm() {
    fileInput.value = '';
    analyzeBtn.disabled = true;
    document.querySelector('.upload-text').textContent = 'Click to upload or drag and drop';
    document.getElementById('results').style.display = 'none';
    document.getElementById('error').style.display = 'none';
}
