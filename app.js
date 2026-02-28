// App State
let questions = [];
let userAnswers = new Array(120).fill(null);
let currentQuestionIndex = 0;
let timerInterval;
let timeRemaining = 130 * 60; // 130 minutes in seconds

// DOM Elements
let views, dom;

// Initialize App
document.addEventListener('DOMContentLoaded', () => {
    // Select elements after DOM is loaded to ensure they exist
    views = {
        splash: document.getElementById('splash-screen'),
        main: document.getElementById('main-app'),
        exam: document.getElementById('exam-interface'),
        result: document.getElementById('result-screen')
    };

    dom = {
        timer: document.getElementById('timer-box'),
        timeDisplay: document.getElementById('time-display'),
        progress: document.getElementById('question-progress'),
        qCategory: document.getElementById('q-category'),
        qNumber: document.getElementById('q-number'),
        qText: document.getElementById('q-text'),
        optionsContainer: document.getElementById('options-container'),
        prevBtn: document.getElementById('prev-btn'),
        nextBtn: document.getElementById('next-btn'),
        finishBtn: document.getElementById('finish-btn'),
        drawer: document.getElementById('optic-drawer'),
        drawerBackdrop: document.getElementById('drawer-backdrop'),
        opticGrid: document.getElementById('optic-grid'),
        modal: document.getElementById('custom-modal')
    };

    // Splash Screen Simulation
    setTimeout(() => {
        views.splash.classList.remove('active');
        views.main.classList.add('active');
    }, 2000);

    // Fetch default questions immediately so they are ready
    fetchQuestions();

    // Event Delegation for Options
    dom.optionsContainer.addEventListener('click', (e) => {
        const optionBtn = e.target.closest('.opt-btn');
        if (optionBtn) {
            selectOption(parseInt(optionBtn.dataset.index));
        }
    });

    // Navigation Buttons
    dom.prevBtn.addEventListener('click', () => navigateQuestion(-1));
    dom.nextBtn.addEventListener('click', () => navigateQuestion(1));

    // Modal
    document.getElementById('modal-cancel').addEventListener('click', hideModal);
    document.getElementById('modal-confirm').addEventListener('click', () => {
        hideModal();
        finishExam();
    });
});

async function fetchQuestions() {
    try {
        const res = await fetch('questions.json');
        if (!res.ok) throw new Error("Network issue or file:// protocol");
        questions = await res.json();
    } catch (error) {
        console.warn("JSON fetch fails on file:// protocol. Local demo modülüne geçiliyor...");
        generateFallbackQuestions();
    }
}

function generateFallbackQuestions() {
    questions = [];

    // --- Genel Yetenek (60 Soru) ---
    // Türkçe (30 Soru)
    for (let i = 1; i <= 30; i++) {
        questions.push({
            id: i, category: "Genel Yetenek - Türkçe",
            question: `Türkçe Sorusu ${i}: Aşağıdaki cümlelerin hangisinde yazım yanlışı vardır?`,
            options: ["Herkes buraya toplanmış.", "Bugün de mi gelmeyeceksin?", "Bir çok insan bu sorunu yaşıyor.", "Oysaki her şeyi planlamıştık.", "Sırtında ağır bir çanta vardı."],
            answer: 2
        });
    }

    // Matematik (30 Soru)
    for (let i = 31; i <= 60; i++) {
        questions.push({
            id: i, category: "Genel Yetenek - Matematik",
            question: `Matematik Sorusu ${i - 30}: 2x + 5 = 15 denkleminde x kaçtır?`,
            options: ["3", "4", "5", "6", "7"],
            answer: 2
        });
    }

    // --- Genel Kültür (60 Soru) ---
    // Tarih (27 Soru)
    for (let i = 61; i <= 87; i++) {
        questions.push({
            id: i, category: "Genel Kültür - Tarih",
            question: `Tarih Sorusu ${i - 60}: Osmanlı Devleti'nin kurucusu kimdir?`,
            options: ["Orhan Gazi", "Osman Gazi", "Ertuğrul Gazi", "I. Murat", "Yıldırım Bayezid"],
            answer: 1
        });
    }

    // Coğrafya (18 Soru)
    for (let i = 88; i <= 105; i++) {
        questions.push({
            id: i, category: "Genel Kültür - Coğrafya",
            question: `Coğrafya Sorusu ${i - 87}: Türkiye'nin en yüksek dağı hangisidir?`,
            options: ["Erciyes", "Süphan", "Ağrı Dağı", "Uludağ", "Kaçkar Dağı"],
            answer: 2
        });
    }

    // Vatandaşlık (9 Soru)
    for (let i = 106; i <= 114; i++) {
        questions.push({
            id: i, category: "Genel Kültür - Vatandaşlık",
            question: `Vatandaşlık Sorusu ${i - 105}: Türkiye Cumhuriyeti'nin yönetim şekli nedir?`,
            options: ["Monarşi", "Oligarşi", "Teokrasi", "Cumhuriyet", "Meşrutiyet"],
            answer: 3
        });
    }

    // Güncel Bilgiler (6 Soru)
    for (let i = 115; i <= 120; i++) {
        questions.push({
            id: i, category: "Genel Kültür - Güncel Bilgiler",
            question: `Güncel Bilgiler Sorusu ${i - 114}: 2024 Yaz Olimpiyatları hangi şehirde düzenlenmiştir?`,
            options: ["Tokyo", "Paris", "Londra", "Los Angeles", "Roma"],
            answer: 1
        });
    }
}

function switchView(viewName) {
    Object.values(views).forEach(v => v.classList.remove('active'));
    views[viewName].classList.add('active');
}

// Exam Flow
async function startExam(examId) {
    if (questions.length === 0) {
        await fetchQuestions();
    }

    // Güvenlik: Hala boşsa hata dön
    if (questions.length === 0) {
        alert("Soru tabanı yüklenemedi. Lütfen sayfayı yenileyin.");
        return;
    }

    // Reset State
    currentQuestionIndex = 0;
    userAnswers.fill(null);
    timeRemaining = 130 * 60;

    // UI Update
    switchView('exam');
    views.exam.classList.add('slide-up');

    startTimer();
    renderQuestion();
    renderOpticGrid();
}

function startTimer() {
    clearInterval(timerInterval);
    dom.timer.classList.remove('danger');

    timerInterval = setInterval(() => {
        timeRemaining--;
        if (timeRemaining <= 0) {
            clearInterval(timerInterval);
            finishExam();
            return;
        }

        const m = Math.floor(timeRemaining / 60);
        const s = timeRemaining % 60;
        dom.timeDisplay.textContent = `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;

        if (timeRemaining < 300) { // Last 5 mins
            dom.timer.classList.add('danger');
        }
    }, 1000);
}

function renderQuestion() {
    if (!questions[currentQuestionIndex]) return;
    const q = questions[currentQuestionIndex];

    // Animations for smooth transition
    dom.qText.parentElement.style.opacity = '0';

    setTimeout(() => {
        dom.qCategory.textContent = q.category;
        dom.qNumber.textContent = `Soru ${currentQuestionIndex + 1} / 120`;
        dom.qText.textContent = q.question;

        dom.optionsContainer.innerHTML = '';
        const letters = ['A', 'B', 'C', 'D', 'E'];

        q.options.forEach((opt, index) => {
            const isSelected = userAnswers[currentQuestionIndex] === index;
            const btn = document.createElement('button');
            btn.className = `opt-btn ${isSelected ? 'selected' : ''}`;
            btn.dataset.index = index;

            btn.innerHTML = `
                <div class="opt-circle">${letters[index]}</div>
                <div class="opt-text">${opt}</div>
            `;
            dom.optionsContainer.appendChild(btn);
        });

        // Update Nav Buttons
        dom.prevBtn.disabled = currentQuestionIndex === 0;

        if (currentQuestionIndex === questions.length - 1) {
            dom.nextBtn.classList.add('hide');
            dom.finishBtn.classList.remove('hide');
        } else {
            dom.nextBtn.classList.remove('hide');
            dom.finishBtn.classList.add('hide');
        }

        // Update Progress Bar
        const progressPercent = ((currentQuestionIndex + 1) / questions.length) * 100;
        dom.progress.style.width = `${progressPercent}%`;

        // Update Optic Highlights
        updateOpticHighlights();

        // Restore opacity
        dom.qText.parentElement.style.opacity = '1';
        dom.qText.parentElement.style.transition = 'opacity 0.2s';
    }, 150);
}

function selectOption(index) {
    if (userAnswers[currentQuestionIndex] === index) {
        userAnswers[currentQuestionIndex] = null; // Toggle off
    } else {
        userAnswers[currentQuestionIndex] = index;
    }

    // Re-render options to show selection
    const buttons = dom.optionsContainer.querySelectorAll('.opt-btn');
    buttons.forEach((btn, i) => {
        if (i === userAnswers[currentQuestionIndex]) {
            btn.classList.add('selected');
        } else {
            btn.classList.remove('selected');
        }
    });

    updateOpticHighlights();
}

function navigateQuestion(direction) {
    const newIdx = currentQuestionIndex + direction;
    if (newIdx >= 0 && newIdx < questions.length) {
        currentQuestionIndex = newIdx;
        renderQuestion();
    }
}

// Drawer / Optic Form
function toggleOpticForm() {
    dom.drawer.classList.toggle('active');
    dom.drawerBackdrop.classList.toggle('active');
}

function renderOpticGrid() {
    dom.opticGrid.innerHTML = '';
    for (let i = 0; i < 120; i++) {
        const btn = document.createElement('button');
        btn.className = 'grid-cell';
        btn.textContent = i + 1;
        btn.id = `grid-cell-${i}`;
        btn.onclick = () => {
            currentQuestionIndex = i;
            renderQuestion();
            toggleOpticForm(); // close drawer
        };
        dom.opticGrid.appendChild(btn);
    }
    updateOpticHighlights();
}

function updateOpticHighlights() {
    for (let i = 0; i < 120; i++) {
        const cell = document.getElementById(`grid-cell-${i}`);
        if (!cell) continue;

        cell.className = 'grid-cell';
        if (userAnswers[i] !== null) cell.classList.add('answered');
        if (i === currentQuestionIndex) cell.classList.add('active-q');
    }
}

// Finishing Exam
function quitExamPrompt() {
    dom.modal.classList.add('active');
    document.getElementById('modal-title').textContent = "Sınavdan Çıkılacak";
    document.getElementById('modal-desc').textContent = "Sınavı yarıda bırakmak istiyor musunuz? İlerlemeniz kaydedilmeyecek.";
}

function finishExamPrompt() {
    // Check if any blank questions
    const blanks = userAnswers.filter(a => a === null).length;
    dom.modal.classList.add('active');

    if (blanks > 0) {
        document.getElementById('modal-title').textContent = "Sınavı Bitir";
        document.getElementById('modal-desc').textContent = `${blanks} adet boş sorunuz var. Sınavı yine de bitirmek istiyor musunuz?`;
    } else {
        document.getElementById('modal-title').textContent = "Tebrikler";
        document.getElementById('modal-desc').textContent = "Tüm soruları işaretlediniz. Sınavı bitirmek istiyor musunuz?";
    }
}

function hideModal() {
    dom.modal.classList.remove('active');
}

function finishExam() {
    clearInterval(timerInterval);

    dom.drawer.classList.remove('active');
    dom.drawerBackdrop.classList.remove('active');

    // Calculate Score
    let trueCount = 0;
    let falseCount = 0;

    for (let i = 0; i < questions.length; i++) {
        if (userAnswers[i] !== null) {
            if (userAnswers[i] === questions[i].answer) {
                trueCount++;
            } else {
                falseCount++;
            }
        }
    }

    const blanks = questions.length - (trueCount + falseCount);
    // KPSS 4 wrong removes 1 right
    const net = trueCount - (falseCount / 4);

    // Update Result UI
    document.getElementById('res-true').textContent = trueCount;
    document.getElementById('res-false').textContent = falseCount;
    document.getElementById('res-blank').textContent = blanks;

    const netScoreEl = document.getElementById('net-score');

    // Animate Number
    animateValue(netScoreEl, 0, net, 1000, true);

    // Animate Circle (max net 120)
    const percentage = Math.max(0, (net / 120) * 100);
    setTimeout(() => {
        document.getElementById('result-circle').setAttribute('stroke-dasharray', `${percentage}, 100`);
    }, 100);

    // Set Congrats Text based on score
    const congratsEl = document.getElementById('congrats-text');
    if (net >= 90) congratsEl.textContent = "Mükemmel Bir Başarı! 🏆";
    else if (net >= 70) congratsEl.textContent = "Çok İyisin! 🚀";
    else if (net >= 50) congratsEl.textContent = "İyi Yoldasın, Devam Et! 💪";
    else congratsEl.textContent = "Daha Fazla Pratik Gerekli! 📚";

    switchView('result');
}

// Utilities
function animateValue(obj, start, end, duration, isDecimal = false) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        const currentVal = progress * (end - start) + start;
        obj.innerHTML = isDecimal ? currentVal.toFixed(2) : Math.floor(currentVal);
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}

function returnHome() {
    switchView('main');
    // reset result circle
    document.getElementById('result-circle').setAttribute('stroke-dasharray', '0, 100');
}

function viewAnswers() {
    alert("Pro Sürüm: Cevapları inceleme ve detaylı konu analizi özellik olarak eklenecektir.");
}
